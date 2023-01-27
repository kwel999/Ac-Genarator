import base64
import hashlib
import hmac
from uuid import uuid4

# tapjoy = "https://ads.tapdaq.com/v4/analytics/reward"
webApi = "https://aminoapps.com/api{}".format
api = "https://service.aminoapps.com/api/v1{}".format


def generateSig(data: str):
    return base64.b64encode(
        bytes.fromhex("19") + hmac.new(bytes.fromhex("DFA5ED192DDA6E88A12FE12130DC6206B1251E44"),
        data.encode(),
        hashlib.sha1).digest()
    ).decode()

def generateDevice():
    data = uuid4().bytes
    return (
        "19" + data.hex() +
        hmac.new(bytes.fromhex("E7309ECC0953C6FA60005B2765F99DBBC965C8E9"),
        bytes.fromhex("19") + data,
        hashlib.sha1).hexdigest()
        ).upper()

def uuidString():
    return str(uuid4())
