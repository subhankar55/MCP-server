import pytest
from clients.ccxt_client import CCXTClient

@pytest.mark.asyncio
async def test_ccxt_exchanges_list():
    client = CCXTClient()
    assert "binance" in client.get_exchanges()
