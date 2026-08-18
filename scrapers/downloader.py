import os
import requests
from bs4 import BeautifulSoup

PAGE_URL = "https://gamingcontrolboard.pa.gov/licensing/application-status-report"

DOWNLOAD_DIR = "downloads"


def download_application_reports():
    print("Connecting to PGCB...")

    response = requests.get(PAGE_URL, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a")

    pdfs = []

    for link in links:
        href = link.get("href")

        if href and ".pdf" in href.lower():
            if href.startswith("/"):
                href = "https://gamingcontrolboard.pa.gov" + href

            pdfs.append((link.text.strip(), href))

    print(f"Found {len(pdfs)} PDF links")

    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    for name, url in pdfs:
        filename = url.split("/")[-1]

        print(f"Downloading {filename}")

        pdf = requests.get(url, timeout=60)

        with open(os.path.join(DOWNLOAD_DIR, filename), "wb") as f:
            f.write(pdf.content)

    print("Done!")