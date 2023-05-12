import { io } from 'socket.io-client';

export const socket = io(`ws://${location.host}`, {
  reconnectionDelayMax: 10000,
})
