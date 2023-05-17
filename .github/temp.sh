#!/bin/bash

# 检测系统
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$NAME
else
    echo "无法检测系统"
    exit 1
fi

echo "正在检测并安装 Conda..."

if ! command -v conda &> /dev/null; then
    echo "Conda 未找到，正在安装..."
    curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda
    rm Miniconda3-latest-Linux-x86_64.sh
fi

export PATH="$HOME/miniconda/bin:$PATH"

echo "正在创建 Conda 环境并安装 Python 3.11 和 pip..."

conda create --name web-chatgpt python=3.11 pip -y

echo "正在激活 Conda 环境..."

source $HOME/miniconda/bin/activate web-chatgpt

echo "正在下载项目中..."
curl -L -o web-chatgpt-build.zip "https://github.com/zmh-program/web-chatgpt-qq-bot/releases/download/{{version}}/package.zip"
mkdir -p web-chatgpt
unzip web-chatgpt-build.zip -d web-chatgpt

echo "正在安装项目依赖中..."
pip install -r web-chatgpt/requirements.txt

echo "正在创建运行脚本中..."
mkdir -p $HOME/.web_chatgpt
cat << EOF > $HOME/.web_chatgpt/run.sh
#!/bin/bash
source $HOME/miniconda/bin/activate web-chatgpt
cd $PWD/web-chatgpt
nohup python app.py >/dev/null 2>&1 &
EOF
chmod +x $HOME/.web_chatgpt/run.sh

echo "正在创建命令别名中..."
echo "alias web-chatgpt='bash $HOME/.web_chatgpt/run.sh'" >> $HOME/.bashrc
source $HOME/.bashrc

echo "安装完成! 输入 web-chatgpt 命令启动项目"
