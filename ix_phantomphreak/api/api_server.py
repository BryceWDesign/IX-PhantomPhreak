"""
IX-PhantomPhreak API Server

Provides RESTful endpoints to submit inputs for exploit scanning,
retrieve logs, and check system status.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core.exploit_detector import ExploitDetector
from core.event_logger import EventLogger

app = FastAPI()
detector = ExploitDetector()
logger = EventLogger()

class InputData(BaseModel):
    source: str
    content: str

@app.post("/phantomphreak/scan")
async def scan_input(data: InputData):
    try:
        patterns = detector.scan_input(data.content)
        if patterns:
            logger.log_event(data.source, data.content, patterns)
        return {"exploit_detected": bool(patterns), "patterns": patterns}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/phantomphreak/logs")
async def get_logs(limit: int = 10):
    return {"logs": logger.get_recent_events(limit)}

@app.get("/phantomphreak/status")
async def status():
    return {"status": "IX-PhantomPhreak running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8093)
