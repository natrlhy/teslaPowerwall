import logging
import sys
import time

import requests

import constants as C
from common import apicall
from teslatoken import Token

logging.basicConfig(
    filename="powerwall.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


def productlists():

    token = Token()
    response = apicall(
        C.PRODUCTS_ENDPOINT,
        "GET",
        headers={"Authorization": "Bearer " + token.tokenstr},
    )

    if response.status_code != 200:
        raise Exception("Couldn't get products. Reason: %s" % (str(response)))
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

    if mode not in C.ENERGY_MODES:
        raise Exception("Mode not valid. Mode = %s." % mode)
    if not isinstance(siteid, int):
        siteid = ""

    if siteid:
        token = Token()
        params = {"default_real_mode": mode}
        response = apicall(
            C.OPERATION_ENDPOINT.format(siteid),
            "POST",
            headers={"Authorization": "Bearer " + token.tokenstr},
            params=params,
        )
        if response.status_code != 200:
            logging.error("Couldn't change energy mode. Reason: %s" % (str(response)))
            raise Exception("Couldn't change energy mode. Reason: %s" % (str(response)))
        logging.info(response.json() + mode)


if len(sys.argv) == 2:
    mode = sys.argv[1]
    energy = getsolarproduct(productlists())
    if energy:
        siteid = list(energy.keys())[0]
        updatemode(siteid, mode)