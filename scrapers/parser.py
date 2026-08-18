import json
import os
import re

import pdfplumber


SECTIONS = {
    "Affiliate",
    "Principal Entity",
    "Institutional Investor",
    "Principal",
}

STATUSES = [
    "Approved for Licensure",
    "Administrative Withdrawal",
    "Surrendered License",
    "Withdrawn",
    "Inactive",
    "Pending",
    "Denied",
    "Revoked",
]


def parse_record(line):
    """
    Convert one line from the PDF into structured fields.
    """

    for status in STATUSES:
        if status in line:
            parts = line.split(status, 1)

            entity = parts[0].strip()
            remainder = parts[1].strip()

            dates = re.findall(r"\d{2}/\d{2}/\d{4}", remainder)

            status_date = dates[0] if len(dates) > 0 else ""
            expiration_date = dates[1] if len(dates) > 1 else ""

            return {
                "entity": entity,
                "status": status,
                "status_date": status_date,
                "expiration_date": expiration_date,
            }

    return {
        "entity": line,
        "status": "",
        "status_date": "",
        "expiration_date": "",
    }


def parse_igaming(pdf_path):
    """
    Parse the PGCB iGaming Application Status Report.
    """

    records = []

    current_applicant = None
    current_section = None

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if not text:
                continue

            for line in text.split("\n"):

                line = line.strip()

                if not line:
                    continue

                # Skip report headers
                if line.startswith("Pennsylvania Gaming"):
                    continue

                if line.startswith("Application Status"):
                    continue

                if line.startswith("As of"):
                    continue

                if line.startswith("Applicant Name"):
                    continue

                if line == "iGaming Operator Application":
                    continue

                # Detect section headers
                if line in SECTIONS:
                    current_section = line
                    continue

                # Before we hit a section header we're reading the applicant
                if current_section is None:
                    current_applicant = line
                    continue

                record = parse_record(line)

                record["applicant"] = current_applicant
                record["section"] = current_section

                records.append(record)

    return records


def save_json(records, filename):

    os.makedirs("snapshots", exist_ok=True)

    with open(
        os.path.join("snapshots", filename),
        "w",
        encoding="utf-8",
    ) as f:

        json.dump(records, f, indent=2)
