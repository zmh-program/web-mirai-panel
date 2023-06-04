import os
from typing import Tuple

import toml
import yaml
from .file import path_safe
from copy import deepcopy

CONFIG_FOLDER = 'config'
GLOBAL_CONFIG = 'config.cfg'
PART_CONFIG_TYPES = ["ai", "chat", "other", "response", "command"]
PART_CONFIGS = [".".join(("name", "bak", "cfg")) for name in PART_CONFIG_TYPES]


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


def read_conf(filename: str) -> dict:
    path = filename if filename == GLOBAL_CONFIG else os.path.join(path_safe(CONFIG_FOLDER), filename)
    if os.path.isfile(path):
        with open(path, "r", encoding="utf-8") as fp:
            return toml.load(fp)
    return {}


def auto_read_conf(name: str) -> Tuple[bool, dict]:
    if name in PART_CONFIG_TYPES:
        return True, read_conf(f"{name}.bak.cfg")
    return False, {}


def save_conf(filename: str, data: dict) -> bool:
    if filename in PART_CONFIGS:
        with open(os.path.join(path_safe(CONFIG_FOLDER), filename), "w", encoding="utf-8") as fp:
            toml.dump(clean_config(data), fp)
        save_global_conf()
    elif filename == GLOBAL_CONFIG:
        with open(filename, "w", encoding="utf-8") as fp:
            toml.dump(clean_config(data), fp)
            '''
            暂时作废
            try: 
                with open('gocqhttp/config.yml', 'r') as file: 
                    config = yaml.safe_load(file) 
                    uin = config.get('account', {}).get('uin') 
                    if uin == '{QQ_ACCOUNT}': 
                        replace_qq_number() 
            except Exception as e: 
                print(f"Error: {e}")
            '''
    else:
        return False
    return True


def auto_save_conf(name: str, data: any) -> bool:
    if name in PART_CONFIG_TYPES:
        return save_conf(f"{name}.bak.cfg", data)
    return False


def save_global_conf() -> bool:
    return save_conf(
        GLOBAL_CONFIG,
        {k: v for conf in PART_CONFIGS for k, v in read_conf(conf).items()},
    )


'''
暂时作废
def replace_qq_number():
    config_data = read_conf('config.cfg')
    qq_number = config_data.get('onebot', {}).get('qq')

    config_file = 'gocqhttp/config.yml'
    with open(config_file, 'r') as fp:
        content = fp.read()

    updated_content = re.sub(r'uin: \{QQ_ACCOUNT\}', f'uin: {qq_number}', content)

    with open(config_file, 'w') as fp:
        fp.write(updated_content)
'''
