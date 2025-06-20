"""
IX-PhantomPhreak REST API Server

Provides HTTP interface for networking and communications queries.
Integrates with IX-Gibson orchestrator and external clients.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from core.query_processor import IXPhantomPhreakQueryProcessor

app = FastAPI()
query_processor = IXPhantomPhreakQueryProcessor()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def handle_query(request: QueryRequest):
    if not request.query or request.query.strip() == "":
        raise HTTPException(status_code=400, detail="Query must not be empty.")
    try:
        answer = query_processor.process_query(request.query)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8008)
