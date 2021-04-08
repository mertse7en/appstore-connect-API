import json, time, requests

from datetime import datetime, timedelta
from authlib.jose import jwt

if __name__ == '__main__':

    ISSUER_ID = "****"
    KEY_ID = "****"
    EXPIRATION_TIME = int(round(time.time() + (20.0 * 60.0)))
    PATH = "Path/to/authkey.... .p8"
    with open(PATH, 'r') as keyfile:
        PRIVATE_KEY = keyfile.read()

    header = {
        "alg": "ES256",
        "kid": KEY_ID,
        "typ": "JWT"
    }
    payload = {
            "iss": ISSUER_ID,
            "exp": EXPIRATION_TIME, 
            "aud": "appstoreconnect-v1"
            }

    token = jwt.encode(header, payload, PRIVATE_KEY)

    JWT = 'Bearer ' + token.decode()
    URL = 'https://api.appstoreconnect.apple.com/v1/users'
    HEAD = {'Authorization': JWT}

    r = requests.get(URL, params={'limit': 200}, headers=HEAD)

    with open('output.json', 'w') as out:
        out.write(json.dumps(r.json(), indent=4))




