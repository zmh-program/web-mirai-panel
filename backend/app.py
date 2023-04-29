import os
import time
from gevent import monkey
from gevent.pywsgi import WSGIServer
from flask import Flask, request, jsonify, render_template, url_for
from flask_socketio import SocketIO, emit
from functions import (
    execute_command,
    handle_upload,
    read_config_file,
    join_files_and_save,
)
from docker import DockerClient

monkey.patch_all()
client = DockerClient(base_url='unix://var/run/docker.sock')

app = Flask(__name__, template_folder='dist')

socketio = SocketIO(app, async_mode='gevent')

# 处理命令
@app.route('/api/command', methods=['POST'])
def handle_command_input():
    command = request.json['command']
    socketio.emit('command_input', command)
    return jsonify({'status': True})

@socketio.on('command_input')
def handle_command_input_socket(command):
    output_generator = execute_command(command)
    for output in output_generator:
        emit('command_output', output)

# 上传文件
@app.route('/api/upload', methods=['POST'])
def handle_uploaded_file():
    file = request.files['file']
    handle_upload(file)
    return jsonify({'status': True})

# 加载文件
@app.route('/api/loadconfig', methods=['POST'])
def load_config():
    config_path = 'config.cfg'
    if os.path.exists(config_path):
        with open(config_path, 'r') as file:
            config_data = toml.load(file)
        return jsonify(config_data)
    else:
        return jsonify({'status': False})

# 保存 chat 配置
@app.route("/api/savechat", methods=["POST"])
def save_chat():
    data = request.json
    chat_data = data["chat"]
    save_config_file(chat_data, "chat.bak.cfg")
    final_config_path = join_files_and_save(["chat.bak.cfg", "ai.bak.cfg", "other.bak.cfg"], "config.cfg")
    download_url = url_for("static", filename=final_config_path)
    return jsonify({"status": True, "download_url": download_url})

# 保存 ai 配置
@app.route("/api/saveai", methods=["POST"])
def save_ai():
    data = request.json
    ai_data = data["ai"]
    save_config_file(ai_data, "ai.bak.cfg")
    final_config_path = join_files_and_save(["chat.bak.cfg", "ai.bak.cfg", "other.bak.cfg"], "config.cfg")
    download_url = url_for("static", filename=final_config_path)
    return jsonify({"status": True, "download_url": download_url})

# 保存 other 配置
@app.route("/api/saveother", methods=["POST"])
def save_other():
    data = request.json
    other_data = data["other"]
    save_config_file(other_data, "other.bak.cfg")
    final_config_path = join_files_and_save(["chat.bak.cfg", "ai.bak.cfg", "other.bak.cfg"], "config.cfg")
    download_url = url_for("static", filename=final_config_path)
    return jsonify({"status": True, "download_url": download_url})

# 容器运行状态
@app.route('/api/containerstatus', methods=['POST'])
def get_container_status():
    containers = client.containers.list(all=True)
    container_statuses = []

    for container in containers:
        container_statuses.append({
            'id': container.short_id,
            'name': container.name
            'status': container.status
        })

    return jsonify(container_statuses)

if __name__ == '__main__':
    socketio.run(app)