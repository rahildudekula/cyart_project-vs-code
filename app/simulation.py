import uuid
from datetime import datetime
from app.graph_builder import graph_builder
from app.alert_engine import alert_engine

class SimulationEngine:
    
    def __init__(self):
        self.scenarios = []
        self.simulation_log = []
    
    def simulate_subdomain_takeover(self, asset_id):
        scenario = {
            "simulation_id": f"SIM-{uuid.uuid4().hex[:8].upper()}",
            "name": "Subdomain Takeover",
            "target_asset": asset_id,
            "attack_type": "DNS Hijacking",
            "severity": "critical",
            "attacker": "APT-29",
            "timestamp": datetime.now().isoformat()
        }
        alert = {
            "alert_id": f"ALERT-{uuid.uuid4().hex[:8].upper()}",
            "title": "CRITICAL: Subdomain Takeover Detected",
            "description": f"Attacker gained control of subdomain on asset {asset_id}",
            "severity": "critical",
            "category": "attack",
            "asset_id": asset_id,
            "attacker_id": "ATT001",
            "status": "open",
            "created_at": datetime.now().isoformat(),
            "risk_score": 9.8
        }
        self.simulation_log.append({
            "event": "Subdomain Takeover Initiated",
            "asset": asset_id,
            "time": datetime.now().isoformat(),
            "status": "detected"
        })
        return {"scenario": scenario, "alert": alert}
    
    def simulate_sql_injection(self, asset_id, cve_id):
        scenario = {
            "simulation_id": f"SIM-{uuid.uuid4().hex[:8].upper()}",
            "name": "SQL Injection Attack",
            "target_asset": asset_id,
            "vulnerability_exploited": cve_id,
            "attack_type": "Code Injection",
            "severity": "critical",
            "attacker": "APT-29",
            "timestamp": datetime.now().isoformat()
        }
        alert = {
            "alert_id": f"ALERT-{uuid.uuid4().hex[:8].upper()}",
            "title": "CRITICAL: SQL Injection Exploit Detected",
            "description": f"Attacker exploited {cve_id} on asset {asset_id}",
            "severity": "critical",
            "category": "vulnerability",
            "asset_id": asset_id,
            "cve_id": cve_id,
            "attacker_id": "ATT001",
            "status": "open",
            "created_at": datetime.now().isoformat(),
            "risk_score": 9.8
        }
        self.simulation_log.append({
            "event": "SQL Injection Attempt",
            "asset": asset_id,
            "cve": cve_id,
            "time": datetime.now().isoformat(),
            "status": "exploited"
        })
        return {"scenario": scenario, "alert": alert}
    
    def simulate_data_exfiltration(self, source_asset, target_asset):
        scenario = {
            "simulation_id": f"SIM-{uuid.uuid4().hex[:8].upper()}",
            "name": "Data Exfiltration",
            "source": source_asset,
            "target": target_asset,
            "attack_type": "Data Theft",
            "severity": "high",
            "attacker": "APT-29",
            "timestamp": datetime.now().isoformat()
        }
        alert = {
            "alert_id": f"ALERT-{uuid.uuid4().hex[:8].upper()}",
            "title": "HIGH: Suspicious Data Transfer",
            "description": f"Large data transfer detected from {source_asset} to {target_asset}",
            "severity": "high",
            "category": "attack",
            "asset_id": target_asset,
            "status": "open",
            "created_at": datetime.now().isoformat(),
            "risk_score": 8.5
        }
        return {"scenario": scenario, "alert": alert}
    
    def simulate_brute_force(self, asset_id):
        scenario = {
            "simulation_id": f"SIM-{uuid.uuid4().hex[:8].upper()}",
            "name": "Brute Force Login",
            "target_asset": asset_id,
            "attack_type": "Credential Attack",
            "severity": "medium",
            "attacker": "Unknown",
            "timestamp": datetime.now().isoformat()
        }
        alert = {
            "alert_id": f"ALERT-{uuid.uuid4().hex[:8].upper()}",
            "title": "MEDIUM: Multiple Failed Login Attempts",
            "description": f"50 failed login attempts detected on {asset_id}",
            "severity": "medium",
            "category": "attack",
            "asset_id": asset_id,
            "status": "open",
            "created_at": datetime.now().isoformat(),
            "risk_score": 5.5
        }
        return {"scenario": scenario, "alert": alert}
    
    def simulate_port_scan(self, asset_id):
        scenario = {
            "simulation_id": f"SIM-{uuid.uuid4().hex[:8].upper()}",
            "name": "Port Scanning",
            "target_asset": asset_id,
            "attack_type": "Reconnaissance",
            "severity": "low",
            "attacker": "Unknown",
            "timestamp": datetime.now().isoformat()
        }
        alert = {
            "alert_id": f"ALERT-{uuid.uuid4().hex[:8].upper()}",
            "title": "LOW: Port Scan Detected",
            "description": f"Network scanning activity detected on {asset_id}",
            "severity": "low",
            "category": "reconnaissance",
            "asset_id": asset_id,
            "status": "open",
            "created_at": datetime.now().isoformat(),
            "risk_score": 3.0
        }
        return {"scenario": scenario, "alert": alert}
    
    def run_full_simulation(self):
        results = {
            "simulation_id": f"FULL-SIM-{uuid.uuid4().hex[:8].upper()}",
            "start_time": datetime.now().isoformat(),
            "events": [],
            "alerts": []
        }
        sim1 = self.simulate_port_scan("A001")
        results["events"].append(sim1["scenario"])
        results["alerts"].append(sim1["alert"])
        sim2 = self.simulate_sql_injection("A001", "CVE-2024-1234")
        results["events"].append(sim2["scenario"])
        results["alerts"].append(sim2["alert"])
        sim3 = self.simulate_data_exfiltration("A001", "A002")
        results["events"].append(sim3["scenario"])
        results["alerts"].append(sim3["alert"])
        sim4 = self.simulate_subdomain_takeover("A003")
        results["events"].append(sim4["scenario"])
        results["alerts"].append(sim4["alert"])
        results["end_time"] = datetime.now().isoformat()
        results["total_alerts"] = len(results["alerts"])
        return results
    
    def get_simulation_log(self):
        return self.simulation_log

simulation_engine = SimulationEngine()
