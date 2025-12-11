from clients.ccxt_client import CCXTClient
from cache.memory_cache import cache

class MarketService:
    def __init__(self):
        self.ccxt = CCXTClient()

    async def get_realtime(self, exchange, symbol):
        key = f"rt:{exchange}:{symbol}"
        if cached := cache.get(key):
            return cached
        
        data = await self.ccxt.get_ticker(exchange, symbol)
        cache.set(key, data, ttl=2)
        return data

    async def get_historical(self, exchange, symbol, timeframe, limit):
        key = f"hist:{exchange}:{symbol}:{timeframe}:{limit}"
        if cached := cache.get(key):
            return cached
        
        data = await self.ccxt.get_ohlcv(exchange, symbol, timeframe, limit)
        cache.set(key, data, ttl=30)
        return data

    async def get_symbols(self, exchange):
        return await self.ccxt.get_symbols(exchange)

    def get_exchanges(self):
        return self.ccxt.get_exchanges()
