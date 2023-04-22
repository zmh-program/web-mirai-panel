from gevent import monkey
monkey.patch_all()

from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import cli
import file_transfer
import os
import toml

app = Flask(__name__)
socketio = SocketIO(app, async_mode='gevent')

'''接收需要执行的命令'''
@app.route('/configeditor/api/command', methods=['POST'])
def handle_command_input():
    command = request.json['command']
    socketio.emit('command_input', command)
    return jsonify({'执行命令状态': '成功'})

'''使用cli.py运行命令'''
@socketio.on('command_input')
def handle_command_input_socket(command):
    output_generator = cli.execute_command(command)
    for output in output_generator:
        emit('command_output', output)

'''处理上传文件命令'''
@app.route('/configeditor/api/upload', methods=['POST'])
def handle_upload():
    file = request.files['file']
    file_transfer.handle_upload(file)
    return jsonify({'上传配置文件状态': '成功'})

'''读取配置文件'''
@app.route('/api/loadconfig', methods=['POST'])
def load_config():
    config_path = find_config_file()
    if config_path:
        with open(config_path, 'r') as file:
            config_data = toml.load(file)
        return jsonify(config_data)
    else:
        return jsonify({'读取配置文件状态': '异常'})

'''辅助函数 寻找有没有config.cfg文件'''
def find_config_file():
    config_filename = 'config.cfg'
    chatgpt_directory = 'chatgpt-qq'
    if os.path.exists(config_filename):
        return config_filename
    elif os.path.exists(chatgpt_directory) and os.path.exists(os.path.join(chatgpt_directory, config_filename)):
        return os.path.join(chatgpt_directory, config_filename)
    else:
        return None

'''保存配置文件'''
@app.route('/api/saveconfig', methods=['POST'])
def save_config():
    config_data = request.json
    config_path = find_docker_compose_file()
    if config_path:
        config_dir = os.path.dirname(config_path)
        config_file_path = os.path.join(config_dir, 'config.cfg')
        
        with open(config_file_path, 'w') as file:
            toml.dump(config_data, file)
        return jsonify({'保存配置文件状态': '成功'})
    else:
        return jsonify({'保存配置文件状态': '异常'})
        
'''辅助函数 寻找有没有docker-compose.yaml文件'''
def find_docker_compose_file():
    docker_compose_filename = 'docker-compose.yaml'
    chatgpt_directory = 'chatgpt-qq'
    if os.path.exists(docker_compose_filename):
        return docker_compose_filename
    elif os.path.exists(chatgpt_directory) and os.path.exists(os.path.join(chatgpt_directory, docker_compose_filename)):
        return os.path.join(chatgpt_directory, docker_compose_filename)
    else:
        return None


if __name__ == '__main__':
    socketio.run(app)