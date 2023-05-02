from gevent.pywsgi import WSGIServer
from gevent import monkey
import logging
from geventwebsocket.handler import WebSocketHandler
from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit
from utils import (
    GLOBAL_CONFIG,
    execute_command,
    handle_upload,
    read_conf,
    save_conf,
)
from docker import DockerClient, errors
logging.basicConfig(format='[%(asctime)s %(levelname)s]: %(message)s')

monkey.patch_all()

app = Flask(__name__, template_folder='dist', static_folder='dist', static_url_path='')
socketio = SocketIO(app, async_mode='gevent')

try:
    client = DockerClient(base_url='unix://var/run/docker.sock')
except errors.DockerException:
    logging.error("不支持的系统！请使用类Unix系统！")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/command', methods=['POST'])
def handle_command_input():
    """处理命令"""
    socketio.emit('command_input', request.json.get('command'))
    return jsonify({'status': True})


@socketio.on('command_input')
def handle_command_input_socket(command):
    for output in execute_command(command):
        emit('command_output', output)


@app.route('/api/upload', methods=['POST'])
def handle_uploaded_file():
    """上传文件"""
    file = request.files['file']
    handle_upload(file)
    return jsonify({'status': True})


@app.route('/api/load', methods=['GET'])
def load_config():
    """读取全局配置并加载toml数据"""
    data = read_conf(GLOBAL_CONFIG)
    return jsonify({'status': True, 'data': data} if data else {'status': False})


@app.route("/api/save/chat", methods=["POST"])
def save_chat():
    """保存 chat 配置"""
    save_conf("chat.bak.cfg", request.json)
    return jsonify({
        "status": True,
    })


@app.route("/api/save/ai", methods=["POST"])
def save_ai():
    """保存 ai 配置"""
    save_conf("ai.bak.cfg", request.json)
    return jsonify({
        "status": True,
    })


@app.route("/api/save/other", methods=["POST"])
def save_other():
    """保存其他配置"""
    save_conf("other.bak.cfg", request.json)
    return jsonify({
        "status": True,
    })


@app.route('/api/status', methods=['POST'])
def get_container_status():
    """获取容器运行状态"""
    return jsonify({
        'status': True,
        'data': [
            {
                'id': container.short_id,
                'name': container.name,
                'status': container.status,
            } for container in client.containers.list(all=True)
        ]
    })


if __name__ == '__main__':
    server = WSGIServer(('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
