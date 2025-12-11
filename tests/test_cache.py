from cache.memory_cache import cache
import time

def test_cache_set_get():
    cache.set("x", 1, ttl=1)
    assert cache.get("x") == 1
    time.sleep(1.1)
    assert cache.get("x") is None
