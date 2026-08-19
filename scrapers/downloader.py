import os
import requests
from bs4 import BeautifulSoup

PAGE_URL = "https://gamingcontrolboard.pa.gov/licensing/application-status-report"
DOWNLOAD_DIR = "downloads"
TARGET_FILE = "Application_Status_iGaming_Operator.pdf"


def download_application_report():
    print("Connecting to PGCB...")

    response = requests.get(PAGE_URL, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    for link in soup.find_all("a"):

        href = link.get("href")

        if not href:
            continue

        if TARGET_FILE not in href:
            continue

        if href.startswith("/"):
            href = "https://gamingcontrolboard.pa.gov" + href

        print("Downloading latest iGaming report...")

        pdf = requests.get(href, timeout=60)
        pdf.raise_for_status()

        with open(
            os.path.join(DOWNLOAD_DIR, TARGET_FILE),
            "wb",
        ) as f:

            f.write(pdf.content)

        print("✓ Latest iGaming report downloaded")

        return

    raise Exception("Could not find iGaming report on PGCB website.")