import requests

print("Regulatory Monitor")
print("------------------")

url = "https://gamingcontrolboard.pa.gov"

response = requests.get(url)

print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    print("✅ Connected to PGCB!")
else:
    print("❌ Could not connect.")
