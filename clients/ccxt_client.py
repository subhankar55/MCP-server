import ccxt.async_support as ccxt
from server.errors import APIClientError

class CCXTClient:
    async def get_ticker(self, exchange, symbol):
        try:
            ex = getattr(ccxt, exchange)()
            ticker = await ex.fetch_ticker(symbol)
            await ex.close()
            return ticker
        except Exception as e:
            raise APIClientError(str(e))

    async def get_ohlcv(self, exchange, symbol, timeframe, limit):
        try:
            ex = getattr(ccxt, exchange)()
            data = await ex.fetch_ohlcv(symbol, timeframe, limit=limit)
            await ex.close()
            return data
        except Exception as e:
            raise APIClientError(str(e))

    async def get_symbols(self, exchange):
        ex = getattr(ccxt, exchange)()
        markets = await ex.load_markets()
        await ex.close()
        return list(markets.keys())

    def get_exchanges(self):
        return ccxt.exchanges
