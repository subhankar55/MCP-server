import requests
from server.errors import APIClientError

CMC_URL = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing"

class CMCClient:
    def fetch_global(self):
        try:
            res = requests.get(CMC_URL)
            return res.json()
        except Exception as e:
            raise APIClientError(str(e))
