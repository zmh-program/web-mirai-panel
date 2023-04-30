import os
from typing import Generator
from subprocess import Popen, PIPE, STDOUT

UPLOADS_FOLDER = 'uploads'
CONFIG_FOLDER = 'config'
GLOBAL_CONFIG = 'config.cfg'
PART_CONFIGS = ["ai", "chat", "other"]
PART_CONFIGS_PATH = [conf + "bak.cfg" for conf in PART_CONFIGS]  # ["ai.bak.cfg", ...]


def execute_command(command: str) -> Generator[str, None, None]:
    process = Popen(command, stdout=PIPE, stderr=STDOUT, shell=True, text=True, bufsize=1)
    for line in process.stdout:
        yield line
    process.stdout.close()
    process.wait()


def read_conf(filename: str) -> str:
    path = os.path.join(CONFIG_FOLDER, filename)
    if os.path.isfile(path):
        with open(path, "r") as fp:
            return fp.read()
    return ""


def save_conf(filename: str, data: str, override=True) -> str:
    """
    保存配置文件
    :param filename: 配置文件名
    :param data: 内容
    :param override: 是否覆盖全局配置 config.cfg
    :return: 配置文件路径
    """

    path = os.path.join(CONFIG_FOLDER, filename)
    if os.path.isfile(path) and filename in [*PART_CONFIGS_PATH, GLOBAL_CONFIG]:
        with open(path, "w") as fp:
            fp.write(data)
        if override is True:
            save_global_conf()
    return path


def save_global_conf() -> str:
    """拼接文件并写入 config.cfg"""
    return save_conf(
        GLOBAL_CONFIG,
        "".join(tuple(map(read_conf, PART_CONFIGS_PATH))),
        override=False,  # 防止递归
    )


def handle_upload(file) -> None:
    if not os.path.exists(UPLOADS_FOLDER):
        os.makedirs(UPLOADS_FOLDER)
    file.save(os.path.join(UPLOADS_FOLDER, file.filename))
