from pydantic import BaseModel
from typing import Optional

class Alert(BaseModel):
    alert_id: str
    title: str
    description: str
    severity: str
    category: str
    asset_id: Optional[str] = None
    cve_id: Optional[str] = None
    attacker_id: Optional[str] = None
    status: str = "open"
    created_at: str = ""
    risk_score: float = 0.0

class AlertRule(BaseModel):
    rule_id: str
    name: str
    condition: str
    severity: str
    enabled: bool = True
