import json

from app.graph\_builder import graph\_builder



\# Load JSON data

with open("data/sample\_data.json", "r") as f:

&#x20;   data = json.load(f)



\# Clear old data

graph\_builder.clear\_graph()

print("🗑️ Cleared old data")



\# Load assets

for asset in data\["assets"]:

&#x20;   graph\_builder.create\_asset(

&#x20;       asset\_id=asset\["asset\_id"],

&#x20;       asset\_type=asset\["asset\_type"],

&#x20;       name=asset\["name"],

&#x20;       ip\_address=asset.get("ip\_address")

&#x20;   )

&#x20;   print(f"✅ Asset added: {asset\['name']}")



\# Load vulnerabilities

for vuln in data\["vulnerabilities"]:

&#x20;   graph\_builder.create\_vulnerability(

&#x20;       cve\_id=vuln\["cve\_id"],

&#x20;       severity=vuln\["severity"],

&#x20;       cvss\_score=vuln\["cvss\_score"],

&#x20;       description=vuln\["description"]

&#x20;   )

&#x20;   print(f"✅ Vulnerability added: {vuln\['cve\_id']}")



\# Load attackers

for att in data\["attackers"]:

&#x20;   graph\_builder.create\_attacker(

&#x20;       attacker\_id=att\["attacker\_id"],

&#x20;       name=att\["name"],

&#x20;       threat\_level=att\["threat\_level"]

&#x20;   )

&#x20;   print(f"✅ Attacker added: {att\['name']}")



\# Load relationships

for rel in data\["relationships"]:

&#x20;   if rel\["type"] == "HAS\_VULNERABILITY":

&#x20;       graph\_builder.link\_asset\_vulnerability(rel\["source"], rel\["target"])

&#x20;   elif rel\["type"] == "CONNECTS\_TO":

&#x20;       graph\_builder.link\_asset\_to\_asset(rel\["source"], rel\["target"])

&#x20;   elif rel\["type"] == "EXPLOITS":

&#x20;       graph\_builder.link\_attacker\_vulnerability(rel\["source"], rel\["target"])

&#x20;   print(f"✅ Relationship: {rel\['source']} → {rel\['target']}")



print("\\n🎉 All data loaded successfully!")

