```python
import json
import os
from app.graph_builder import graph_builder

# Get full path to JSON file
script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "data", "sample_data.json")

# Load JSON data with BOM-safe encoding
with open(json_path, "r", encoding="utf-8-sig") as f:
    data = json.load(f)

# Clear old data
graph_builder.clear_graph()
print("[CLEAR] Old data cleared")

# Load assets
for asset in data["assets"]:
    graph_builder.create_asset(
        asset_id=asset["asset_id"],
        asset_type=asset["asset_type"],
        name=asset["name"],
        ip_address=asset.get("ip_address")
    )
    print(f"[+] Asset added: {asset['name']}")

# Load vulnerabilities
for vuln in data["vulnerabilities"]:
    graph_builder.create_vulnerability(
        cve_id=vuln["cve_id"],
        severity=vuln["severity"],
        cvss_score=vuln["cvss_score"],
        description=vuln["description"]
    )
    print(f"[+] Vulnerability added: {vuln['cve_id']}")

# Load attackers
for att in data["attackers"]:
    graph_builder.create_attacker(
        attacker_id=att["attacker_id"],
        name=att["name"],
        threat_level=att["threat_level"]
    )
    print(f"[+] Attacker added: {att['name']}")

# Load relationships
for rel in data["relationships"]:

    if rel["type"] == "HAS_VULNERABILITY":
        graph_builder.link_asset_vulnerability(
            rel["source"],
            rel["target"]
        )

    elif rel["type"] == "CONNECTS_TO":
        graph_builder.link_asset_to_asset(
            rel["source"],
            rel["target"]
        )

    elif rel["type"] == "EXPLOITS":
        graph_builder.link_attacker_vulnerability(
            rel["source"],
            rel["target"]
        )

    print(f"[+] Relationship: {rel['source']} -> {rel['target']}")

print("\n*** All data loaded successfully! ***")
```
