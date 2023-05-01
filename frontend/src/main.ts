import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import './assets/style/main.css'

const app = createApp(App)

app.use(router)
app.use(ElementPlus)
app.mount('#app')
for (const [key, component] of Object.entries(ElementPlusIconsVue)) app.component(key, component)
