import { io } from 'socket.io-client';

export const socket = io(`ws://${location.host}/api/command`, {
  reconnectionDelayMax: 10000,

})
