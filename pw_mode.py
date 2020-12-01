from teslatoken import Token
import sys
import time

import requests

# CONSTANTS

BASE_URL = "https://owner-api.teslamotors.com"
ENERGY_MODES = ["self_consumption", "autonomous"]


def productlists():

    token = Token()
    url = BASE_URL + "/api/1/products"
    response = requests.get(
        url=url, headers={"Authorization": "Bearer " + token.tokenstr}
    )
    if response.status_code != 200:
        raise Exception("Couldn't get auth token. Reason: %s" % (str(response)))
    return response.json().get("response", [])


def getsolarproduct(productlist):

    if not isinstance(productlist, list):
        productlist = []

    energysites = {
        product["energy_site_id"]: product
        for product in productlist
        if "energy_site_id" in product
    }
    return energysites


def updatemode(siteid, mode):

    if mode not in ENERGY_MODES:
        raise Exception("Mode not valid. Mode = %s." % mode)
    if not isinstance(siteid, int):
        siteid = ""

    if siteid:
        token = Token()
        url = BASE_URL + "/api/1/energy_sites/%s/operation" % siteid
        params = {"default_real_mode": mode}
        response = requests.post(
            url=url,
            params=params,
            headers={"Authorization": "Bearer " + token.tokenstr},
        )
        if response.status_code != 200:
            raise Exception("Couldn't get auth token. Reason: %s" % (str(response)))
        print(time.ctime())
        print(response.json())


if len(sys.argv) == 2:
    mode = sys.argv[1]
    energy = getsolarproduct(productlists())
    if energy:
        siteid = list(energy.keys())[0]
        updatemode(siteid, mode)