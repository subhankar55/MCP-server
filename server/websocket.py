from fastapi import APIRouter, WebSocket
from services.market_service import MarketService
import asyncio

router = APIRouter(prefix="/ws", tags=["websocket"])

service = MarketService()

@router.websocket("/realtime/{exchange}/{symbol}")
async def ws_realtime(ws: WebSocket, exchange: str, symbol: str):
    await ws.accept()
    while True:
        data = await service.get_realtime(exchange, symbol)
        await ws.send_json(data)
        await asyncio.sleep(1)
