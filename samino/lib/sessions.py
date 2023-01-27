from typing import BinaryIO

from httpx import Client
from json_minify import json_minify
from ujson import dumps

from .exception import CheckExceptions
from .headers import Headers
from .util import *

settings = {
    "sid": None,
    "userId": None,
    "secret": None
}


class Session(Headers):
    def __init__(self, proxies: dict = None, staticDevice: str = None):
        self.proxy = proxies
        self.staticDevice = staticDevice

        self.sid = settings["sid"]
        self.uid = settings["userId"]
        self.secret = settings["secret"]

        Headers.__init__(self, header_device=self.staticDevice)
        self.session = Client(proxies=self.proxy)

        self.deviceId = self.header_device

        if self.sid:
            self.updateHeaders(sid=self.sid)

    def settings(self, settingsSid: str = None, settingsUser: str = None, settingsSecret: str = None):
        settings.update({
            "sid": settingsSid,
            "userId": settingsUser,
            "secret": settingsSecret
        })
        self.sid = settings["sid"]
        self.uid = settings["userId"]
        self.secret = settings["secret"]

    def postRequest(self, url: str, data: (str, dict, BinaryIO) = None, newHeaders: dict = None, webRequest: bool = False, minify: bool = False):
        if newHeaders:
            self.app_headers.update(newHeaders)

        if not isinstance(data, str) and not isinstance(data, BinaryIO):
            data = json_minify(dumps(data)) if minify else dumps(data)

        if isinstance(data, str):
            req = self.session.post(
                url=webApi(url) if webRequest else api(url),
                data=data,
                headers=self.web_headers if webRequest else self.updateHeaders(data=data, sid=self.sid)
            )
        elif isinstance(data, BinaryIO):
            req = self.session.post(
                url=webApi(url) if webRequest else api(url),
                files={"file": data},
                headers=self.web_headers if webRequest else self.updateHeaders(data=data, sid=self.sid)
            )
        return CheckExceptions(req.json()) if req.status_code != 200 else req.json()

    def getRequest(self, url: str):
        req = self.session.get(url=api(url), headers=self.app_headers)
        return CheckExceptions(req.json()) if req.status_code != 200 else req.json()

    def deleteRequest(self, url: str):
        req = self.session.delete(url=api(url), headers=self.app_headers)
        return CheckExceptions(req.json()) if req.status_code != 200 else req.json()
