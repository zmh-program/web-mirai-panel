#!/bin/bash

# 检测系统
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$NAME
else
    echo "无法检测系统"
    exit 1
fi

# 安装 Python、pip、wget 和 unzip
install_package() {
    package=$1
    if ! command -v $package &> /dev/null; then
        echo "$package 未找到，正在安装..."
        if [[ $OS == "Ubuntu" ]] || [[ $OS == "Debian" ]]; then
            sudo apt-get update
            sudo apt-get install -y $package
        elif [[ $OS == "CentOS Linux" ]]; then
            sudo yum install -y $package
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

# 下载并解压 web-chatgpt-build.zip
wget -O web-chatgpt-build.zip "https://github.com/zmh-program/web-chatgpt-qq-bot/releases/download/1.1/package.zip"
mkdir -p web-chatgpt
unzip web-chatgpt-build.zip -d web-chatgpt

# 安装 requirements.txt
pip3 install -r web-chatgpt/requirements.txt

# 在后台运行 Flask 应用
cd web-chatgpt
nohup python3 app.py >/dev/null 2>&1 &
ip_address=$(hostname -I | awk '{print $1}')
current_dir=$(pwd)
echo -e "Flask 应用正在后台运行\n请前往\e[34m${ip_address}:5000\e[0m进行访问\n请自行开放\e[33m5000\e[0m端口\n生成的配置在${current_dir}/web-chatgpt/config/config.cfg"
