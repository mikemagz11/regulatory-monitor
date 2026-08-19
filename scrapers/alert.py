from datetime import datetime
import os


def build_alert(matches):

    os.makedirs("output", exist_ok=True)

    today = datetime.now().strftime("%B %d, %Y")

    lines = []

    lines.append("# PGCB iGaming Hard Rock Monitor")
    lines.append("")
    lines.append(f"Run Date: {today}")
    lines.append("")
    lines.append("---")
    lines.append("")

    if len(matches) == 0:

        lines.append("## Result")
        lines.append("")
        lines.append("✅ No Hard Rock activity detected.")
        lines.append("")
        lines.append("The following aliases were checked:")
        lines.append("")
        lines.append("- Hard Rock")
        lines.append("- Hard Rock Digital")
        lines.append("- Hard Rock Interactive")
        lines.append("- Seminole Gaming")
        lines.append("- Seminole Hard Rock")

    else:

        lines.append("## 🚨 Hard Rock Activity Detected")
        lines.append("")

        for match in matches:

            lines.append(f"### {match['entity']}")
            lines.append("")
            lines.append(f"Applicant: **{match['applicant']}**")
            lines.append(f"Section: **{match['section']}**")

            if match["status"]:
                lines.append(f"Status: **{match['status']}**")

            if match["status_date"]:
                lines.append(f"Status Date: **{match['status_date']}**")

            if match["expiration_date"]:
                lines.append(
                    f"Expiration: **{match['expiration_date']}**"
                )

            lines.append("")
            lines.append("---")
            lines.append("")

    with open(
        "output/daily_alert.md",
        "w",
        encoding="utf-8",
    ) as f:

        f.write("\n".join(lines))