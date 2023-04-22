import subprocess

def execute_command(command):
    '''subprocess.Popen 用于创建一个新的进程并执行命令'''
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, text=True, bufsize=1)
    for line in process.stdout:
        yield line
    process.stdout.close()
    process.wait()
