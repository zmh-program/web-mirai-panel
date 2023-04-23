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

def save_config_commond():
    config_data = request.json
    config_path = 'config.cfg'

    if os.path.exists(config_path):
        backup_path = 'config.cfg.bak.{}'.format(int(time.time()))
        os.rename(config_path, backup_path)

    with open(config_path, 'w') as file:
        toml.dump(config_data, file)
    return jsonify({'status': True})
    
UPLOADS_FOLDER = 'uploads'

def handle_upload(file):
    if not os.path.exists(UPLOADS_FOLDER):
        os.makedirs(UPLOADS_FOLDER)
    filename = file.filename
    file.save(os.path.join(UPLOADS_FOLDER, filename))