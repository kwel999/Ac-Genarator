import base64
import hashlib
import hmac
from uuid import uuid4

# tapjoy = "https://ads.tapdaq.com/v4/analytics/reward"
api = "https://service.narvii.com/api/v1{}".format
webApi = "https://aminoapps.com/api{}".format


def generateSig(data: str):
    return base64.b64encode(
        bytes.fromhex("42") + hmac.new(bytes.fromhex("f8e7a61ac3f725941e3ac7cae2d688be97f30b93"),
        data.encode(),
        hashlib.sha1).digest()
    ).decode()

def generateDevice():
    data = uuid4().bytes
    return (
        "42" + data.hex() +
        hmac.new(bytes.fromhex("02b258c63559d8804321c5d5065af320358d366f"),
        bytes.fromhex("42") + data,
        hashlib.sha1).hexdigest()
        ).upper()

def uuidString():
    return str(uuid4())
