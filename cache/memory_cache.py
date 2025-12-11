import time

class MemoryCache:
    def __init__(self):
        self.store = {}
        self.expiry = {}

    def set(self, key, value, ttl=10):
        self.store[key] = value
        self.expiry[key] = time.time() + ttl

    def get(self, key):
        if key in self.store and time.time() < self.expiry[key]:
            return self.store[key]
        return None

cache = MemoryCache()
