import uuid
from datetime import datetime
from app.graph_builder import graph_builder

class AlertEngine:
    
    def __init__(self):
        self.alerts = []
    
    def calculate_severity(self, cvss_score):
        if cvss_score >= 9.0:
            return "critical"
        elif cvss_score >= 7.0:
            return "high"
        elif cvss_score >= 4.0:
            return "medium"
        elif cvss_score > 0:
            return "low"
        else:
            return "informational"
    
    def generate_alerts_from_vulnerabilities(self):
        query = """
        MATCH (a:Asset)-[r:HAS_VULNERABILITY]->(v:Vulnerability)
        RETURN a.asset_id AS asset_id, a.name AS asset_name, 
               v.cve_id AS cve_id, v.severity AS severity, 
               v.cvss_score AS cvss_score, v.description AS description
        """
        results = graph_builder.db.query(query)
        new_alerts = []
        
        for record in results:
            alert = {
                "alert_id": f"ALERT-{uuid.uuid4().hex[:8].upper()}",
                "title": f"{record['severity'].upper()} Vulnerability Found",
                "description": f"{record['description']} on asset {record['asset_name']}",
                "severity": record['severity'],
                "category": "vulnerability",
                "asset_id": record['asset_id'],
                "cve_id": record['cve_id'],
                "status": "open",
                "created_at": datetime.now().isoformat(),
                "risk_score": record['cvss_score']
            }
            new_alerts.append(alert)
        
        self.alerts = new_alerts
        return new_alerts
    
    def generate_attack_alerts(self):
        query = """
        MATCH path = (att:Attacker)-[*1..5]->(target:Asset)
        RETURN att.attacker_id AS attacker_id, att.name AS attacker_name,
               target.asset_id AS target_id, target.name AS target_name
        """
        results = graph_builder.db.query(query)
        attack_alerts = []
        
        for record in results:
            alert = {
                "alert_id": f"ATTACK-{uuid.uuid4().hex[:8].upper()}",
                "title": "Attack Path Detected",
                "description": f"Attacker {record['attacker_name']} can reach {record['target_name']}",
                "severity": "critical",
                "category": "attack",
                "asset_id": record['target_id'],
                "attacker_id": record['attacker_id'],
                "status": "open",
                "created_at": datetime.now().isoformat(),
                "risk_score": 9.5
            }
            attack_alerts.append(alert)
        
        return attack_alerts
    
    def get_all_alerts(self):
        vuln_alerts = self.generate_alerts_from_vulnerabilities()
        attack_alerts = self.generate_attack_alerts()
        return vuln_alerts + attack_alerts
    
    def get_alerts_by_severity(self, severity):
        all_alerts = self.get_all_alerts()
        return [a for a in all_alerts if a['severity'] == severity]
    
    def get_alert_stats(self):
        all_alerts = self.get_all_alerts()
        stats = {
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
            "informational": 0,
            "total": len(all_alerts)
        }
        for alert in all_alerts:
            sev = alert['severity']
            if sev in stats:
                stats[sev] += 1
        return stats

alert_engine = AlertEngine()
