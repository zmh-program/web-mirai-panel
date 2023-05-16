import { io } from 'socket.io-client';
import { notify } from '@/assets/script/utils'

const enableSecurity: boolean = location.protocol === "https:";
export const socket = io(`${enableSecurity ? "wss" : "ws"}://${location.host}`, {
  reconnectionDelayMax: 10000,
})

socket.on("connect", () => notify({
  title: "连接成功",
  message: "服务器连接成功！",
  type: "success",
  showClose: false,
}))

socket.on("error", () => notify({
  title: "连接失败",
  message: "服务器连接失败！",
  type: "error",
  showClose: false,
}))


socket.on("reconnect_attempt", () => notify({
  title: "断开连接",
  message: "服务器断开连接，正在尝试重新连接",
  type: "info",
  showClose: false,
}))

socket.on("reconnect", () => notify({
  title: "重新连接",
  message: "服务器重新连接成功！",
  type: "success",
  showClose: false,
}))

socket.on("reconnect_error", () => notify({
  title: "重新连接失败",
  message: "服务器重新连接失败！",
  type: "error",
  showClose: false,
}))
