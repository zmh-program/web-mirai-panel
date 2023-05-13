import requests
import platform
import json
import re
import os
import toml
import psutil
import docker
from typing import Generator, Dict, Union
from copy import deepcopy
from subprocess import Popen, PIPE, STDOUT

UPLOADS_FOLDER = 'uploads'
CONFIG_FOLDER = 'config'
GLOBAL_CONFIG = 'config.cfg'
BYTE_TO_GB = 1024 ** 3
PART_CONFIGS = [
    "ai.bak.cfg",
    "chat.bak.cfg",
    "other.bak.cfg",
    "response.bak.cfg"
]


def empty_field(value) -> bool:
    return not (value.strip() if isinstance(value, str) else (True if isinstance(value, bool) else value))


def clean_config(data: dict) -> dict:
    for key, value in deepcopy(data).items():
        if isinstance(value, dict):
            data[key] = clean_config(value)
        if isinstance(value, (list, tuple, set)):
            data[key] = [clean_config(element) if isinstance(element, dict) else element for element in value]
        elif empty_field(value):
            del data[key]
    return data


def execute_command(command: str) -> Generator[str, None, None]:
    process = Popen(command, stdout=PIPE, stderr=STDOUT, shell=True, text=True, bufsize=1)
    for line in process.stdout:
        yield line
    process.stdout.close()
    process.wait()


def read_conf(filename: str) -> dict:
    path = os.path.join(CONFIG_FOLDER, filename)
    if os.path.isfile(path):
        with open(path, "r") as fp:
            return toml.load(fp)
    return {}


def save_conf(filename: str, data: dict, override=True) -> str:
    """
    保存配置文件
    :param filename: 配置文件名
    :param data: 内容
    :param override: 是否覆盖全局配置 config.cfg
    :return: 配置文件路径
    """

    path = os.path.join(CONFIG_FOLDER, filename)
    if filename in [*PART_CONFIGS, GLOBAL_CONFIG]:
        with open(path, "w") as fp:
            toml.dump(clean_config(data), fp)
        if override is True:
            save_global_conf()
    return path


def save_global_conf() -> str:
    """拼接文件并写入 config.cfg"""
    return save_conf(
        GLOBAL_CONFIG,
        {k: v for conf in PART_CONFIGS for k, v in read_conf(conf).items()},
        override=False,  # 防止递归
    )


def handle_upload(file) -> None:
    if not os.path.exists(UPLOADS_FOLDER):
        os.makedirs(UPLOADS_FOLDER)
    file.save(os.path.join(UPLOADS_FOLDER, file.filename))


def upload_to_pastebin(text: str) -> str:
    # 使用request把文本上传到paste bin
    resp = requests.post('https://pastebin.mozilla.org/api/', data={
        'expires': '86400',
        'format': 'url',
        'lexer': '_markdown',
        'content': text
    })
    return resp.text if resp.status_code == 200 else f"上传失败：{resp.status_code}"


def get_nickname(qq_number: int) -> str:
    # 使用request获取QQ昵称返回值
    response = requests.get(f"http://users.qzone.qq.com/fcg-bin/cgi_get_portrait.fcg?uins={qq_number}")
    json_str = re.search(r'\{.*\}', response.text).group(0)
    data = json.loads(json_str)
    nickname = data[str(qq_number)][6]
    return nickname.encode('utf-8').decode('unicode_escape')


def get_system_info() -> dict:
    """获取系统信息 (常量)"""
    cpu_count = psutil.cpu_count()  # CPU 核心
    memory = round(psutil.virtual_memory().total / BYTE_TO_GB, 2)  # 内存
    disk = round(psutil.disk_usage('/').total / BYTE_TO_GB, 2)  # 磁盘容量
    system, release, version, host = platform.system(), platform.release(), platform.version(), platform.node()  # 杂项

    try:
        with open('config.cfg', 'r') as file:  # 读取config.cfg中的manager_qq
            config = toml.load(file)
            qq = (config.get('onebot', {}) or config.get('mirai', {})).get('manager_qq')
            nickname = get_nickname(qq)  # QQ 昵称
    except FileNotFoundError:
        qq = None
        nickname = "未知"

    try:
        with open('gocqhttp/device.json', 'r') as file:  # 读取gocqhttp的设备代号
            protocol = json.load(file).get('protocol')
    except FileNotFoundError:
        protocol = None

    return {
        'cpu_count': cpu_count,
        'memory': memory,
        'disk': disk,
        'system': system,
        'release': release,
        'version': version,
        'host': host,
        'qq': qq,
        'nickname': nickname,
        'device': protocol,
    }


def get_status_info() -> dict:
    """获取系统状态 (动态)"""
    # CPU使用率
    cpu_percent = psutil.cpu_percent()

    # 磁盘容量
    disk = psutil.disk_usage('/')
    used_disk, available_disk = round(disk.used / BYTE_TO_GB, 2), round(disk.free / BYTE_TO_GB, 2)

    # 内存容量
    memory = psutil.virtual_memory()
    used_memory, available_memory = round(memory.used / BYTE_TO_GB, 2), round(memory.available / BYTE_TO_GB, 2)

    # Docker
    docker_client = docker.from_env()
    containers = docker_client.containers.list()
    desired_container_names = [
        'chatgpt-qq-mirai-1', 'chatgpt-qq-gocqhttp-1',
        'chatgpt-qq-watchtower-1', 'chatgpt-qq-chatgpt-1',
    ]

    status_info = {
        'cpu_percent': cpu_percent,
        'used_memory': used_memory,
        'available_memory': available_memory,
        'used_disk': used_disk,
        'available_disk': available_disk,
        'containers': [
            {'name': container.name, 'status': container.status}
            for container in containers
            if container.name in desired_container_names
        ],
    }

    return status_info
