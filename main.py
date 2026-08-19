from datetime import datetime

from scrapers.downloader import download_application_report
from scrapers.parser import parse_application_report
from scrapers.hardrock import find_matches
from scrapers.slack import send_slack

PDF = "downloads/Application_Status_iGaming_Operator.pdf"
SOURCE_URL = "https://gamingcontrolboard.pa.gov/licensing/application-status-report"

run_time = datetime.now().strftime("%B %d, %Y | %I:%M %p")

print("=" * 60)
print("PGCB Competitive Intelligence Monitor")
print("=" * 60)

print("📥 Downloading latest PGCB iGaming report...")
download_application_report()

print("📄 Parsing report...")
records = parse_application_report(PDF)

print(f"✓ Parsed {len(records)} licensing records")

print("🔍 Searching for Hard Rock aliases...")
matches = find_matches(records)

print(f"✓ Found {len(matches)} matching records")

if not matches:

    message = f"""
🟢 *PGCB Competitive Intelligence Monitor*

No Hard Rock-related activity detected.

📄 *Report:* Application Status – iGaming Operator
📊 *Licensing Records Checked:* {len(records)}
🕒 *Run Time:* {run_time} ET

🔗 *Official Source*
{SOURCE_URL}
"""

else:

    message = f"""
🚨 *PGCB COMPETITIVE INTELLIGENCE ALERT*

Hard Rock-related activity detected.

🕒 *Run Time:* {run_time} ET

"""

    for match in matches:

        message += f"""
🏢 *Entity*
{match["entity"]}

🎯 *Matched Alias*
{match["matched_alias"]}

👤 *Applicant*
{match["applicant"]}

📋 *Status*
{match["status"] or "Not Available"}

📂 *Section*
{match["section"]}

"""

        if match.get("status_date"):
            message += f"""📅 *Status Date*
{match["status_date"]}

"""

        if match.get("expiration_date"):
            message += f"""⏳ *Expiration Date*
{match["expiration_date"]}

"""

    message += f"""
🔗 *Official Source*
{SOURCE_URL}
"""

send_slack(message)

print()
print("=" * 60)
print("✅ Competitive Intelligence Monitor completed successfully.")
print("=" * 60)