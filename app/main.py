from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="ThreatGraph - Attack Path Visualization API",
    description="Team 4 - Graph Data Model for Threat Monitoring",
    version="1.0.0"
)

app.include_router(router, prefix="/api/v1")

@app.get("/")
def home():
    return {
        "message": "ThreatGraph API - Team 4",
        "docs": "/docs"
    }