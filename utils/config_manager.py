import os
import re
import toml
import yaml
from copy import deepcopy

CONFIG_FOLDER = 'config'
GLOBAL_CONFIG = 'config.cfg'
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

def read_conf(filename: str) -> dict:
    path = os.path.join(CONFIG_FOLDER, filename)
    if os.path.isfile(path):
        with open(path, "r") as fp:
            return toml.load(fp)
    return {}

def save_conf(filename: str, data: dict, override=True) -> str:
    path = os.path.join(os.getcwd(), filename)
    if filename in [*PART_CONFIGS, GLOBAL_CONFIG]:
        with open(path, "w") as fp:
            toml.dump(clean_config(data), fp)
        if override is True:
            save_global_conf()
            try:
                with open('gocqhttp/config.yml', 'r') as file:
                    config = yaml.safe_load(file)
                    uin = config.get('account', {}).get('uin')
                    if uin == '{QQ_ACCOUNT}':
                        replace_qq_number()
    return path

def save_global_conf() -> str:
    return save_conf(
        GLOBAL_CONFIG,
        {k: v for conf in PART_CONFIGS for k, v in read_conf(conf).items()},
        override=False,
    )

def replace_qq_number():
    config_data = read_conf('config.cfg')
    qq_number = config_data.get('onebot', {}).get('qq')

    config_file = 'gocqhttp/config.yml'
    with open(config_file, 'r') as fp:
        content = fp.read()

    updated_content = re.sub(r'uin: \{QQ_ACCOUNT\}', f'uin: {qq_number}', content)

    with open(config_file, 'w') as fp:
        fp.write(updated_content)