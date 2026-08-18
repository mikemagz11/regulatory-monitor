from scrapers.parser import parse_igaming, save_json

print("=" * 60)
print("Pennsylvania Regulatory Monitor")
print("=" * 60)

print("Parsing iGaming report...")

records = parse_igaming(
    "downloads/Application_Status_iGaming_Operator.pdf"
)

print(f"✓ Extracted {len(records)} records")

save_json(records, "igaming.json")

print("✓ Saved snapshots/igaming.json")