import time

import requests

import constants as C

def apicall(endpoint, method, headers, params=None, data=None):
    session = requests.Session()
    request = requests.Request(method, C.BASE_URL + endpoint, headers=headers, data=data, params=params)
    prep = session.prepare_request(request)
    response = None
    for _ in range(C.RETRY_COUNT):
        try:
            response = session.send(prep, timeout=C.TIMEOUT)
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            time.sleep(C.RETRY_INTERVAL)
            continue
        break
    if response is None:
        raise Exception("I bailed out trying this %s withmethod= %s" %(endpoint, method))
    return response