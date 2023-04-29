from subprocess import Popen, PIPE, STDOUT
from flask import request
import os
import toml
import time

def execute_command(command):
    process = Popen(command, stdout=PIPE, stderr=STDOUT, shell=True, text=True, bufsize=1)
    for line in process.stdout:
        yield line
    process.stdout.close()
    process.wait()

'''文件读取函数'''
def read_config_file(filename):
    config_path = f"config/{filename}"
    if os.path.isfile(config_path):
        with open(config_path, "r") as file:
            return file.read()
    return ""

'''拼接文件函数'''
def join_files_and_save(filenames, final_filename):
    content = "".join([read_config_file(filename) for filename in filenames])
    config_path = f"config/{final_filename}"
    with open(config_path, "w") as file:
        file.write(content)
    return config_path

UPLOADS_FOLDER = 'uploads'

def handle_upload(file):
    if not os.path.exists(UPLOADS_FOLDER):
        os.makedirs(UPLOADS_FOLDER)
    filename = file.filename
    file.save(os.path.join(UPLOADS_FOLDER, filename))