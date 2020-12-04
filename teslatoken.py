import logging
import os
import time

import requests
import yaml

import constants as C
from common import apicall

logging.basicConfig(
    filename="powerwall.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


class Token:
    NOW = time.time()

    def __init__(self):
        self.tokenstr = self.readtoken()
        if self.tokenstr == None:
            self.obtainToken()
            self.tokenstr = self.readtoken()

    def readtoken(self):
        token = None
        if os.path.isfile(C.TOKENFILE):
            conf = yaml.safe_load(open(C.TOKENFILE))
            expires = conf.get("expires_at", 0)
            if self.NOW < expires:
                token = conf.get("access_token")
        return token

    def obtainToken(self):
        """
        This method makes an oauth Tesla API call to obtain an Access Token
        """

        conf = yaml.safe_load(open(C.ACCOUNTS))
        # url = C.BASE_URL + "/oauth/token"
        auth = {
            "grant_type": "password",
            "client_id": C.TESLA_CLIENT_ID,
            "client_secret": C.TESLA_CLIENT_SECRET,
            "email": conf["data"]["email"],
            "password": conf["data"]["password"],
        }
        logging.info("Getting new auth token...")

        response = apicall(C.TOKEN_ENDPOINT, "POST", headers={}, data=auth)
        # response = requests.post(url=url, data=auth, timeout=C.TIMEOUT)
        if response is None or response.status_code != 200:
            logging.error("Couldn't get auth token. Reason: %s" % (str(response)))
            raise Exception("Couldn't get auth token. Reason: %s" % (str(response)))
        expires = response.json().get("created_at", 0) + response.json().get(
            "expires_in", 0
        )
        data = response.json()
        data.update({"expires_at": expires})
        with open(C.TOKENFILE, "w") as writer:
            yaml.dump(data, writer)