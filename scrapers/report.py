import os
from datetime import datetime


def generate_report(
    new_items,
    removed_items,
    changed_items,
    monitored_records,
    watchlists,
):
    os.makedirs("reports", exist_ok=True)

    today = datetime.now().strftime("%B %d, %Y")

    lines = []

    lines.append("# Pennsylvania Regulatory Monitor")
    lines.append("")
    lines.append(f"**Run Date:** {today}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Executive Summary")
    lines.append("")
    lines.append(f"- Companies Monitored: **{len(watchlists)}**")
    lines.append(f"- Matching Records Found: **{len(monitored_records)}**")
    lines.append(f"- New Records: **{len(new_items)}**")
    lines.append(f"- Changed Records: **{len(changed_items)}**")
    lines.append(f"- Removed Records: **{len(removed_items)}**")
    lines.append("")

    if (
        len(new_items) == 0
        and len(changed_items) == 0
        and len(removed_items) == 0
    ):
        lines.append("## Result")
        lines.append("")
        lines.append("✅ **No changes detected.**")
        lines.append("")
    else:

        if new_items:
            lines.append("## New Records")
            lines.append("")

            for r in new_items:
                lines.append(f"- **{r['entity']}**")
                lines.append(f"  - Applicant: {r['applicant']}")
                lines.append(f"  - Section: {r['section']}")
                lines.append(f"  - Status: {r['status']}")
                lines.append("")

        if changed_items:
            lines.append("## Updated Records")
            lines.append("")

            for c in changed_items:

                before = c["before"]
                after = c["after"]

                lines.append(f"- **{before['entity']}**")
                lines.append(
                    f"  - {before['status']} → {after['status']}"
                )
                lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Monitored Companies")
    lines.append("")

    for company in watchlists.keys():
        lines.append(f"- {company}")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Current Matching Records")
    lines.append("")

    if monitored_records:

        for r in monitored_records:

            lines.append(
                f"- **{r['watchlist']}** | {r['entity']}"
            )

            if r["status"]:
                lines.append(f"  - {r['status']}")

            lines.append("")

    else:

        lines.append("No monitored entities were found.")

    with open(
        "reports/daily_report.md",
        "w",
        encoding="utf-8",
    ) as f:

        f.write("\n".join(lines))