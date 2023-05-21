import requests
import platform
import json
import re
import psutil
import docker
import toml

BYTE_TO_GB = 1024 ** 3
DESIRED_CONTAINERS = [
    'mirai',
    'gocqhttp',
    'watchtower',
    'chatgpt',
]
CONTAINER_STATUS = {
    "created": "#828282",
    "paused": "#828282",
    "running": "#28A745",
    "restarting": "#FFC107",
    "removing": "#DC3545",
    "dead": "#DC3545"
}


def upload_to_pastebin(text: str) -> str:
    # 使用request把文本上传到paste bin
    resp = requests.post('https://pastebin.mozilla.org/api/', data={
        'expires': '86400',
        'format': 'url',
        'lexer': '_markdown',
        'content': text
    })
    return resp.text if resp.status_code == 200 else f"上传失败：{resp.status_code}"


def convert(size: int, fixed: int = 1) -> float:
    return round(size / BYTE_TO_GB, fixed)


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
    memory = convert(psutil.virtual_memory().total)  # 内存
    disk = convert(psutil.disk_usage('/').total, 0)  # 磁盘容量
    system, release, version, host = platform.system(), platform.release(), platform.version(), platform.node()  # 杂项

    try:
        with open('config.cfg', 'r') as file:  # 读取config.cfg中的manager_qq
            config = toml.load(file)
            qq = (config.get('onebot', {}) or config.get('mirai', {})).get('manager_qq')
            nickname = get_nickname(qq)  # QQ 昵称
    except FileNotFoundError:
        qq = "未知"
        nickname = "未知"

    try:
        with open('gocqhttp/device.json', 'r') as file:  # 读取gocqhttp的设备代号
            protocol = str(json.load(file).get('protocol'))
    except FileNotFoundError:
        protocol = "暂无"

    return {
        'cpu_count': cpu_count,
        'memory': memory,
        'disk': disk,
        'system': f"{system} {release}",
        'host': host,
        'qq': str(qq),
        'nickname': nickname,
        'device': protocol,
    }


def filter_container(container) -> bool:
    return any(
        [desired in container.name for desired in DESIRED_CONTAINERS]
    )


def get_status_info() -> dict:
    """获取系统状态 (动态)"""

    cpu_percent = psutil.cpu_percent()  # CPU使用率
    disk = convert(psutil.disk_usage('/').used, 0)  # 占用磁盘容量
    memory = convert(psutil.virtual_memory().used)  # 占用内存容量
    net = psutil.net_io_counters()
    sent, recv = convert(net.bytes_sent, 2), convert(net.bytes_recv, 2)

    # Docker
    try:
        docker_client = docker.from_env()
        containers = docker_client.containers.list()
    except docker.errors.DockerException:
        containers = []

    status_info = {
        'cpu': cpu_percent,
        'memory': memory,
        'disk': disk,
        'sent': sent,
        'recv': recv,
        'containers': [
            {
                'name': container.name,
                'status': container.status,
                'color': CONTAINER_STATUS.get(str(container.status).lower(), "#6C757D"),
            }
            for container in filter(filter_container, containers)
        ],
    }

    return status_info
