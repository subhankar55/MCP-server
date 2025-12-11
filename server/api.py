from fastapi import APIRouter, HTTPException
from services.market_service import MarketService
from server.models import (
    RealtimeRequest, HistoricalRequest,
    SymbolResponse, ExchangeResponse
)

router = APIRouter(prefix="/api", tags=["market"])

service = MarketService()


@router.post("/realtime")
async def realtime(req: RealtimeRequest):
    try:
        return await service.get_realtime(req.exchange, req.symbol)
    except Exception as e:
        raise HTTPException(500, str(e))


@router.post("/historical")
async def historical(req: HistoricalRequest):
    try:
        return await service.get_historical(req.exchange, req.symbol, req.timeframe, req.limit)
    except Exception as e:
        raise HTTPException(500, str(e))


@router.get("/symbols/{exchange}")
async def symbols(exchange: str):
    return SymbolResponse(symbols=await service.get_symbols(exchange))


@router.get("/exchanges")
async def exchanges():
    return ExchangeResponse(exchanges=service.get_exchanges())
