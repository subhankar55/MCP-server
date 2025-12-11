from pydantic import BaseModel

class RealtimeRequest(BaseModel):
    exchange: str
    symbol: str

class HistoricalRequest(BaseModel):
    exchange: str
    symbol: str
    timeframe: str = "1h"
    limit: int = 100

class SymbolResponse(BaseModel):
    symbols: list[str]

class ExchangeResponse(BaseModel):
    exchanges: list[str]
