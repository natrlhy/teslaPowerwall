# File locations

ACCOUNTS = "accounts.yml"
TOKENFILE = "token.yml"

# URL, endpoints and modes

BASE_URL = "https://owner-api.teslamotors.com"
TOKEN_ENDPOINT = "/oauth/token"
PRODUCTS_ENDPOINT = "/api/1/products"
OPERATION_ENDPOINT = "/api/1/energy_sites/{}/operation"
RESERVE_ENDPOINT = "/api/1/energy_sites/{}/backup"
ENERGY_MODES = ["self_consumption", "autonomous"]

TESLA_CLIENT_ID = "81527cff06843c8634fdc09e8ac0abefb46ac849f38fe1e431c2ef2106796384"
TESLA_CLIENT_SECRET = "c7257eb71a564034f9419ee651c7d0e5f7aa6bfbd18bafb5c5c033b093bb2fa3"
RETRY_COUNT = 3
RETRY_INTERVAL = 5
TIMEOUT = 3
