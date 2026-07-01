from fastapi import APIRouter
from app.models import Asset, Vulnerability, Attacker
from app.graph_builder import graph_builder
from app.alert_engine import alert_engine
from app.simulation import simulation_engine

router = APIRouter()

# ===== ASSET APIs =====
@router.post("/asset")
def add_asset(asset: Asset):
    result = graph_builder.create_asset(
        asset.asset_id, asset.asset_type, asset.name, asset.ip_address
    )
    return {"status": "success", "data": result}

@router.post("/vulnerability")
def add_vulnerability(vuln: Vulnerability):
    result = graph_builder.create_vulnerability(
        vuln.cve_id, vuln.severity, vuln.cvss_score, vuln.description
    )
    return {"status": "success", "data": result}

@router.post("/attacker")
def add_attacker(attacker: Attacker):
    result = graph_builder.create_attacker(
        attacker.attacker_id, attacker.name, attacker.threat_level
    )
    return {"status": "success", "data": result}

@router.post("/link/asset-vulnerability")
def link_av(asset_id: str, cve_id: str):
    result = graph_builder.link_asset_vulnerability(asset_id, cve_id)
    return {"status": "linked", "data": result}

@router.post("/link/asset-asset")
def link_aa(source_id: str, target_id: str):
    result = graph_builder.link_asset_to_asset(source_id, target_id)
    return {"status": "linked", "data": result}

@router.post("/link/attacker-vulnerability")
def link_atv(attacker_id: str, cve_id: str):
    result = graph_builder.link_attacker_vulnerability(attacker_id, cve_id)
    return {"status": "linked", "data": result}

@router.get("/attack-paths")
def get_paths(attacker_id: str, target_asset_id: str):
    result = graph_builder.find_attack_paths(attacker_id, target_asset_id)
    return {"status": "success", "paths": result}

@router.get("/graph")
def get_graph():
    result = graph_builder.get_full_graph()
    return {"status": "success", "graph": result}

@router.delete("/clear")
def clear():
    graph_builder.clear_graph()
    return {"status": "cleared"}

# ===== ALERT APIs =====
@router.get("/alerts")
def get_all_alerts():
    alerts = alert_engine.get_all_alerts()
    return {"status": "success", "count": len(alerts), "alerts": alerts}

@router.get("/alerts/critical")
def get_critical_alerts():
    alerts = alert_engine.get_alerts_by_severity("critical")
    return {"status": "success", "count": len(alerts), "alerts": alerts}

@router.get("/alerts/high")
def get_high_alerts():
    alerts = alert_engine.get_alerts_by_severity("high")
    return {"status": "success", "count": len(alerts), "alerts": alerts}

@router.get("/alerts/stats")
def get_alert_stats():
    stats = alert_engine.get_alert_stats()
    return {"status": "success", "stats": stats}

# ===== SIMULATION APIs =====
@router.post("/simulation/port-scan")
def sim_port_scan(asset_id: str):
    return simulation_engine.simulate_port_scan(asset_id)

@router.post("/simulation/sql-injection")
def sim_sql_injection(asset_id: str, cve_id: str):
    return simulation_engine.simulate_sql_injection(asset_id, cve_id)

@router.post("/simulation/data-exfiltration")
def sim_data_exfil(source: str, target: str):
    return simulation_engine.simulate_data_exfiltration(source, target)

@router.post("/simulation/subdomain-takeover")
def sim_subdomain_takeover(asset_id: str):
    return simulation_engine.simulate_subdomain_takeover(asset_id)

@router.post("/simulation/brute-force")
def sim_brute_force(asset_id: str):
    return simulation_engine.simulate_brute_force(asset_id)

@router.post("/simulation/full-attack")
def run_full_simulation():
    return simulation_engine.run_full_simulation()

@router.get("/simulation/log")
def get_simulation_log():
    return {"log": simulation_engine.get_simulation_log()}
