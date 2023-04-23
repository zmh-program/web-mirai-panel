import os
import toml
import time
from gevent import monkey
from gevent.pywsgi import WSGIServer
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from functions import execute_command, save_config_commond, handle_upload
from docker import DockerClient

monkey.patch_all()
client = DockerClient(base_url='unix://var/run/docker.sock')

app = Flask(__name__)
socketio = SocketIO(app, async_mode='gevent')

'''处理命令'''
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

'''上传文件'''
@app.route('/api/upload', methods=['POST'])
def handle_uploaded_file():
    file = request.files['file']
    handle_upload(file)
    return jsonify({'status': True})

'''加载文件'''
@app.route('/api/loadconfig', methods=['POST'])
def load_config():
    config_path = 'config.cfg'
    if os.path.exists(config_path):
        with open(config_path, 'r') as file:
            config_data = toml.load(file)
        return jsonify(config_data)
    else:
        return jsonify({'status': False})

'''保存文件'''
@app.route('/api/saveconfig', methods=['POST'])
def save_config():
    return functions.save_config_commond()
'''备用节点'''
@app.route('/api/saveconfig1', methods=['POST'])
def save_config1():
    return functions.save_config_commond()


'''容器运行状态'''
@app.route('/api/containerstatus', methods=['GET'])
def get_container_status():
    containers = client.containers.list(all=True)
    container_statuses = []

    for container in containers:
        container_statuses.append({
            'id': container.short_id,
            'name': container.name,
            'status': container.status
        })

    return jsonify(container_statuses)

if __name__ == '__main__':
    socketio.run(app)
