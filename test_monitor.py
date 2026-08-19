from datetime import datetime

from scrapers.slack import send_slack

run_time = datetime.now().strftime("%B %d, %Y | %I:%M %p")

message = f"""
🚨 *PGCB COMPETITIVE MONITOR TEST*

━━━━━━━━━━━━━━━━━━━━━━━━━━

📅 *Run Time*
{run_time} ET

🏛️ *Jurisdiction*
Pennsylvania Gaming Control Board (PGCB)

📄 *Report*
Application Status – iGaming Operator

🎯 *Monitored Company*
Hard Rock

⚠️ *TEST ALERT*

This is a test notification.

No live PGCB data is being checked.

━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 *Matched Alias*
Seminole Hard Rock Digital, LLC

🏢 *Entity*
Seminole Hard Rock Digital, LLC

👤 *Applicant*
Hard Rock Interactive LLC

📂 *Section*
Affiliate

📋 *Status*
Pending Investigation

📅 *Status Date*
08/19/2026

━━━━━━━━━━━━━━━━━━━━━━━━━━

🔗 *Official Source*
https://gamingcontrolboard.pa.gov/licensing/application-status-report
"""

send_slack(message)

print("✅ Test Slack message sent successfully.")