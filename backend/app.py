from gevent import monkey
monkey.patch_all()

from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import cli
import file_transfer

app = Flask(__name__)
app.config['SECRET_KEY'] = '1145141918191810'
socketio = SocketIO(app, async_mode='gevent')

'''接收需要执行的命令'''
@app.route('/api/command', methods=['POST'])
def handle_command_input():
    command = request.json['command']
    socketio.emit('command_input', command)
    return jsonify({'status': 'success'})

'''使用cli.py运行命令'''
@socketio.on('command_input')
def handle_command_input_socket(command):
    output_generator = cli.execute_command(command)
    for output in output_generator:
        emit('command_output', output)

'''处理上传文件命令'''
@app.route('/api/upload', methods=['POST'])
def handle_upload():
    file = request.files['file']
    file_transfer.handle_upload(file)
    return 'File uploaded and saved.'

if __name__ == '__main__':
    socketio.run(app)
