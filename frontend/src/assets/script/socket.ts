import { io } from 'socket.io-client';

export const socket = io(`ws://${location.host}`, {
  reconnectionDelayMax: 10000,
})

// @ts-ignore
// eslint-disable-next-line no-undef
socket.on("connect", () => ElNotification({
  title: "连接成功",
  message: "服务器连接成功！",
  type: "success",
  showClose: false,
}))
