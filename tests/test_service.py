import pytest
from services.market_service import MarketService

@pytest.mark.asyncio
async def test_symbols_call():
    svc = MarketService()
    exchanges = svc.get_exchanges()
    assert isinstance(exchanges, list)
