#!/bin/bash

# 检测系统
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$NAME
else
    echo "无法检测系统"
    exit 1
fi

echo "正在检测安装 Python, pip, wget 和 unzip"

install_package() {
    package=$1
    name=$( [ "$package" == "python3-pip" ] && echo "pip3" || echo "$package" )
    if ! command -v "$name" &> /dev/null; then
        echo "$name 未找到，正在安装..."
        if [[ $OS == "Ubuntu" ]] || [[ $OS == "Debian" ]] || [[ $OS == "Debian GNU/Linux" ]]; then
            sudo apt-get update
            sudo apt-get install -y "$package"
        elif [[ $OS == "CentOS Linux" ]] || [[ $OS == "CentOS Stream" ]]; then
            sudo yum install -y "$package"
        else
            echo "不支持的操作系统：$OS"
            exit 1
        fi
    fi
}

# 检查并安装所需软件包
install_package "python3"
install_package "python3-pip"
install_package "wget"
install_package "zip"

echo "正在下载项目中..."
wget -O web-chatgpt-build.zip "https://github.com/zmh-program/web-chatgpt-qq-bot/releases/download/{{version}}/package.zip"
mkdir -p web-chatgpt
unzip web-chatgpt-build.zip -d web-chatgpt

echo "正在安装项目依赖中..."
pip3 install -r web-chatgpt/requirements.txt

echo "正在运行项目中..."
cd web-chatgpt || exit
nohup python3 app.py >/dev/null 2>&1 &
current_dir=$(pwd)
echo -e "Flask 应用正在后台运行! \n请自行开放 \e[33m5000\e[0m 端口并前往 \e[34mhttp://ip:5000\e[0m 进行访问\n - 生成的配置在 \e[33m${current_dir}/config/config.cfg\e[0m\n - 上传的文件在 \e[33m${current_dir}/upload/...\e[0m\n"
