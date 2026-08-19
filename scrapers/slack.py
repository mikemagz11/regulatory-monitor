import os
import requests
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")


def send_slack(message):
    if not WEBHOOK_URL:
        raise Exception("SLACK_WEBHOOK_URL not found in .env")

    response = requests.post(
        WEBHOOK_URL,
        json={"text": message},
        timeout=30,
    )

    response.raise_for_status()