from flask import request, abort
import json
import base64
import hashlib
import os.path
from .config import CONFIG_FOLDER
from .file import path_safe

SETTING_PATH = os.path.join(path_safe(CONFIG_FOLDER), "settings.data")


def read() -> dict:
    try:
        with open(SETTING_PATH, "rb") as fp:
            content = base64.b64decode(fp.read()).decode('utf-8')
        return json.loads(content)
    except FileNotFoundError:
        return {}


def write(data: dict) -> None:
    global password
    data['password'] = password = hashlib.md5(data['password'].encode('utf-8')).hexdigest()
    content = base64.b64encode(json.dumps(data).encode('utf-8'))
    with open(SETTING_PATH, "wb") as fp:
        fp.write(content)


def validate(key: str):
    return hashlib.md5(key.encode('utf-8')).hexdigest() == password


def authenticated(func):
    assert callable(func)

    def wrapper(*args, **kwargs) -> any:
        global password
        key = request.headers.get("auth", "")
        if validate(key):
            return func(*args, **kwargs)
        abort(401)

    return wrapper


password = read()['password']
