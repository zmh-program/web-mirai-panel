import re
import json
import base64
import hashlib
import os.path
from .config import CONFIG_FOLDER
from .file import path_safe

SETTING_PATH = os.path.join(path_safe(CONFIG_FOLDER), "settings.data")

urls = []


def read_setting() -> dict:
    try:
        with open(SETTING_PATH, "rb") as fp:
            content = base64.b64decode(fp.read()).decode('utf-8')
        return json.loads(content)
    except FileNotFoundError:
        return {}


def read_setting_safe() -> dict:
    resp = read_setting()
    if 'password' in resp:
        del resp['password']
    return resp


def write_setting(data: dict) -> None:
    global password
    data['password'] = password = hashlib.md5(data['password'].encode('utf-8')).hexdigest()
    content = base64.b64encode(json.dumps(data).encode('utf-8'))
    with open(SETTING_PATH, "wb") as fp:
        fp.write(content)


def validate(key: str):
    return (hashlib.md5(key.encode('utf-8')).hexdigest() == password) if password else True


def register(url: str) -> str:
    global urls
    urls.append(re.sub('<[^>]+>', '', url))
    return url


def conform(path: str) -> bool:
    for url in urls:
        if path.startswith(url):
            return True
    return False


password = read_setting().get('password', '')
