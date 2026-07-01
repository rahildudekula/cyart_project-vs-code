from app.database import db

class GraphBuilder:
    
    def create_asset(self, asset_id, asset_type, name, ip_address=None):
        query = """
        MERGE (a:Asset {asset_id: $asset_id})
        SET a.type = $asset_type,
            a.name = $name,
            a.ip_address = $ip_address
        RETURN a
        """
        return db.query(query, {
            "asset_id": asset_id,
            "asset_type": asset_type,
            "name": name,
            "ip_address": ip_address
        })
    
    def create_vulnerability(self, cve_id, severity, cvss_score, description):
        query = """
        MERGE (v:Vulnerability {cve_id: $cve_id})
        SET v.severity = $severity,
            v.cvss_score = $cvss_score,
            v.description = $description
        RETURN v
        """
        return db.query(query, {
            "cve_id": cve_id,
            "severity": severity,
            "cvss_score": cvss_score,
            "description": description
        })
    
    def create_attacker(self, attacker_id, name, threat_level):
        query = """
        MERGE (att:Attacker {attacker_id: $attacker_id})
        SET att.name = $name,
            att.threat_level = $threat_level
        RETURN att
        """
        return db.query(query, {
            "attacker_id": attacker_id,
            "name": name,
            "threat_level": threat_level
        })
    
    def link_asset_vulnerability(self, asset_id, cve_id):
        query = """
        MATCH (a:Asset {asset_id: $asset_id})
        MATCH (v:Vulnerability {cve_id: $cve_id})
        MERGE (a)-[r:HAS_VULNERABILITY]->(v)
        RETURN r
        """
        return db.query(query, {"asset_id": asset_id, "cve_id": cve_id})
    
    def link_asset_to_asset(self, source_id, target_id):
        query = """
        MATCH (a1:Asset {asset_id: $source_id})
        MATCH (a2:Asset {asset_id: $target_id})
        MERGE (a1)-[r:CONNECTS_TO]->(a2)
        RETURN r
        """
        return db.query(query, {"source_id": source_id, "target_id": target_id})
    
    def link_attacker_vulnerability(self, attacker_id, cve_id):
        query = """
        MATCH (att:Attacker {attacker_id: $attacker_id})
        MATCH (v:Vulnerability {cve_id: $cve_id})
        MERGE (att)-[r:EXPLOITS]->(v)
        RETURN r
        """
        return db.query(query, {"attacker_id": attacker_id, "cve_id": cve_id})
    
    def find_attack_paths(self, attacker_id, target_asset_id):
        query = """
        MATCH path = (att:Attacker {attacker_id: $attacker_id})
                    -[*1..5]->
                    (target:Asset {asset_id: $target_asset_id})
        RETURN path LIMIT 10
        """
        return db.query(query, {
            "attacker_id": attacker_id,
            "target_asset_id": target_asset_id
        })
    
    def get_full_graph(self):
        query = """
        MATCH (n)-[r]->(m)
        RETURN n, r, m
        """
        return db.query(query)
    
    def clear_graph(self):
        query = "MATCH (n) DETACH DELETE n"
        return db.query(query)


# ⚠️ THIS LINE IS IMPORTANT - DON'T MISS IT!
graph_builder = GraphBuilder()