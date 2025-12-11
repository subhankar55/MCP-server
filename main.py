from fastapi import FastAPI
from server.api import router as api_router
from server.websocket import router as ws_router
from server.logger import setup_logging

app = FastAPI(title="Crypto MCP Server")

setup_logging()

app.include_router(api_router)
app.include_router(ws_router)


@app.get("/")
def root():
    return {"message": "Crypto MCP Server is running"}
