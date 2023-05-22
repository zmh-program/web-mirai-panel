from flask import request, jsonify, abort
import json
import base64
import hashlib
import os.path
from .config import CONFIG_FOLDER
from .file import path_safe

SETTING_PATH = os.path.join(path_safe(CONFIG_FOLDER), "settings.data")

password = ""


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


def authenticated(func):
    assert callable(func)

    def wrapper(*args, **kwargs) -> any:
        global password
        key = request.headers.get("auth", "")
        if hashlib.md5(key.encode('utf-8')).hexdigest() == password:
            return func(*args, **kwargs)
        abort(401)

    return wrapper

