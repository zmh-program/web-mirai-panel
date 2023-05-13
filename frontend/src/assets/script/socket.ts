import { io } from 'socket.io-client';
import { ElNotification } from 'element-plus'

export const socket = io(`ws://${location.host}`, {
  reconnectionDelayMax: 10000,
})

socket.on("connect", () => ElNotification({
  title: "连接成功",
  message: "服务器连接成功！",
  type: "success"
}))
