from scrapers.downloader import download_application_reports
from scrapers.parser import parse_application_report
from scrapers.hardrock import find_matches
from scrapers.slack import send_slack

PDF = "downloads/Application_Status_iGaming_Operator.pdf"

print("=" * 60)
print("PGCB Hard Rock Monitor")
print("=" * 60)

print("Downloading latest PGCB reports...")
download_application_reports()

print("Parsing iGaming report...")
records = parse_application_report(PDF)

print(f"✓ Parsed {len(records)} records")

print("Searching for Hard Rock aliases...")
matches = find_matches(records)

print(f"✓ Found {len(matches)} matching records")

if len(matches) == 0:

    message = f"""✅ *PGCB Hard Rock Monitor*

Report Checked:
• Application Status – iGaming Operator

Records Parsed:
{len(records)}

Result:
No Hard Rock activity detected.
"""

else:

    message = "🚨 *PGCB HARD ROCK ALERT*\n\n"

    for match in matches:

        message += f"""Entity:
{match['entity']}

Applicant:
{match['applicant']}

Section:
{match['section']}

Status:
{match['status']}

--------------------------------

"""

send_slack(message)

print()
print("Slack notification sent.")
print("=" * 60)