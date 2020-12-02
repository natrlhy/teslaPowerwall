import os
import time

import requests
import yaml

# CONSTANTS

BASE_URL = "https://owner-api.teslamotors.com"
TESLA_CLIENT_ID = "81527cff06843c8634fdc09e8ac0abefb46ac849f38fe1e431c2ef2106796384"
TESLA_CLIENT_SECRET = "c7257eb71a564034f9419ee651c7d0e5f7aa6bfbd18bafb5c5c033b093bb2fa3"


def obtainToken():
    """
    This method makes an oauth Tesla API call to obtain an Access Token
    """
    conf = yaml.safe_load(open("./accounts.yml"))
    url = BASE_URL + "/oauth/token"
    auth = {
        "grant_type": "password",
        "client_id": TESLA_CLIENT_ID,
        "client_secret": TESLA_CLIENT_SECRET,
        "email": conf["data"]["email"],
        "password": conf["data"]["password"],
    }

    response = requests.post(url=url, data=auth)
    if response.status_code != 200:
        raise Exception("Couldn't get auth token. Reason: %s" % (str(response)))

    return response.json()["access_token"]


class Token:
    NOW = time.time()
    ACCOUNTS = "./accounts.yml"
    TOKENFILE = "./token.yml"

    def __init__(self):
        self.tokenstr = self.readtoken()
        if self.tokenstr == None:
            self.obtainToken()
            self.tokenstr = self.readtoken()

    def readtoken(self):
        token = None
        if os.path.isfile(self.TOKENFILE):
            conf = yaml.safe_load(open(self.TOKENFILE))
            expires = conf.get("expires_at", 0)
            if self.NOW < expires:
                token = conf.get("access_token")
        return token

    def obtainToken(self):
        """
        This method makes an oauth Tesla API call to obtain an Access Token
        """

        conf = yaml.safe_load(open(self.ACCOUNTS))
        url = BASE_URL + "/oauth/token"
        auth = {
            "grant_type": "password",
            "client_id": TESLA_CLIENT_ID,
            "client_secret": TESLA_CLIENT_SECRET,
            "email": conf["data"]["email"],
            "password": conf["data"]["password"],
        }
        print("Getting new auth Token...")
        response = requests.post(url=url, data=auth)
        if response.status_code != 200:
            raise Exception("Couldn't get auth token. Reason: %s" % (str(response)))
        expires = response.json().get("created_at", 0) + response.json().get(
            "expires_in", 0
        )
        data = response.json()
        data.update({"expires_at": expires})
        with open(self.TOKENFILE, "w") as writer:
            yaml.dump(data, writer)