import redis
import json

class RedisCache:
    def __init__(self, url="redis://localhost:6379"):
        self.client = redis.Redis.from_url(url)

    def set(self, key, value, ttl=10):
        self.client.set(key, json.dumps(value), ex=ttl)

    def get(self, key):
        data = self.client.get(key)
        return json.loads(data) if data else None
