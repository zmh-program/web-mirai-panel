import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import VueSocketIO from 'vue-socket.io'
import './assets/style/main.css'

const app = createApp(App)

app.use(router)
app.use(ElementPlus)
app.use(new VueSocketIO({
  connection: `ws://127.0.0.1:5000`,
}))
app.mount('#app')
