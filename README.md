<div align="center">

# Web ChatGPT Mirai BOT
#### web 图形化界面一键配置 ChatGPT Mirai Bot 聊天机器人

[» 主项目地址 »](https://github.com/lss233/chatgpt-mirai-qq-bot)
</div>

> [!note]
> 由于 ChatGPT Mirai Bot 主项目停止支持，此项目生命周期面临结束！

## 功能一览
- 🎃 **一键安装脚本**
- ✨ **Web UI 一键配置**
- 🎄 **上传文件**
- 🔥 **Web 终端**
- 🍒 **Docker 容器监控**
- 🎍 **Electron App**
- 🍏 **自定义设置**

## 编译
运行成功后将在 http://localhost:5000 开始服务。
```shell
pip install -r requirements.txt
python app.py
```
如果服务器开启防火墙，请将 `5000` 端口开启白名单。

### 后台运行
```shell
nohup python app.py &
```

### 停止服务
```shell
sudo kill -9 $(sudo lsof -t -i :5000)
```

## 开源协议
[MIT](https://github.com/zmh-program/web-chatgpt-qq-bot/blob/main/LICENSE)
