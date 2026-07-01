from pydantic import BaseModel
from typing import Optional

class Asset(BaseModel):
    asset_id: str
    asset_type: str
    name: str
    ip_address: Optional[str] = None

class Vulnerability(BaseModel):
    cve_id: str
    severity: str
    cvss_score: float
    description: str

class Attacker(BaseModel):
    attacker_id: str
    name: str
    threat_level: str