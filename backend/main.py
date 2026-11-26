import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/api/health")
async def health():
    instance = os.getenv("INSTANCE_ID", "unknown")
    return {"health": instance}

