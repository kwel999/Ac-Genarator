from httpx import get

from .client import Client
from .lib.exception import CheckExceptions
from .local import Local

version = "2.4.6"
newest = get("https://pypi.org/pypi/samino/json").json()["info"]["version"]

if version != newest:
    print(f"\033[1;33mSAmino New Version!: {newest} (Your Using {version})\033[1;0m")
