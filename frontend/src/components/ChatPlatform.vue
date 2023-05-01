<script setup lang='ts'>
import { reactive, ref } from 'vue'
import type { Ref } from 'vue'
import axios from 'axios'

const type: Ref<string> = ref('cqhttp');

const cqhttp = reactive({
  qq: "",
  manager_qq: "",
  host: "0.0.0.0",
  port: 8566
})
const mirai = reactive({
  qq: "",
  manager_qq: "",
  key: "1234567890",
  reverse_host: "0.0.0.0",
  reverse_port: 8566,
})
const telegram = reactive({
  token: "",
  proxy: "",
  manager_chat: "1234567890"
})
const discord = reactive({
  token: ""
})
const wechat = reactive({
  host: "0.0.0.0",
  port: 8234,
  debug: false
})
const wecom = reactive({
  host: "0.0.0.0",
  port: 8234,
  debug: false,
  corp_id: "",
  agent_id: "",
  secret: "",
  token: "",
  encoding_aes_key: ""
})

const selector: Record<string, Record<string, string | number | boolean>> = {
  cqhttp,
  mirai,
  telegram,
  discord,
  wechat,
  wecom
}

const loader = ref(false);
function submit() {
  loader.value = true;
  const data = selector[type.value];
  axios.post('/api/save/chat', data)
    .then(() => {
      loader.value = false;
      // @ts-ignore
      // eslint-disable-next-line no-undef
      ElMessage({
        type: 'success',
        message: `保存成功！`,
      });
    })
    .catch(() => {
      loader.value = false;
      // @ts-ignore
      // eslint-disable-next-line no-undef
      ElMessage({
        type: 'error',
        message: `保存时出错！`,
      });
    })
}
</script>

<template>
 <el-radio-group v-model='type'>
   <el-radio label='cqhttp'>OneBot (CQHttp)</el-radio>
   <el-radio label='mirai'>Mirai</el-radio>
   <el-radio label='telegram'>Telegram</el-radio>
   <el-radio label='discord'>Discord</el-radio>
   <el-radio label='wechat'>个人微信</el-radio>
   <el-radio label='wecom'>企业微信</el-radio>
 </el-radio-group>
 <br><br>
 <el-alert type='info' v-if='type == "mirai"' :closable='false' show-icon>
   推荐使用&nbsp;<el-link class='link' type='primary' @click='type = "cqhttp"'>CQHttp</el-link>
 </el-alert>
 <el-alert type='info' v-else-if='type == "wechat"' :closable='false' show-icon>
   我们建议将本项目部署在国外服务器上，减少网络错误发生的概率。<br>
   Docker 用户别忘了将此处配置中的<span class='bold'>端口号</span>映射出来，以便被访问到。
 </el-alert>
 <br>
 <div>
   <el-form :model='cqhttp' v-if='type == "cqhttp"'>
     <el-form-item label='机器人QQ号'><el-input placeholder='请修改为你机器人的QQ号' v-model='cqhttp.qq' /></el-form-item>
     <el-form-item label='管理员QQ号'><el-input placeholder='请修改为机器人管理员的QQ号' v-model='cqhttp.manager_qq' /></el-form-item>
     <el-form-item label='CQHttp 主机'><el-input v-model='cqhttp.host' /></el-form-item>
     <el-form-item label='CQHttp 端口'><el-input v-model='cqhttp.port' /></el-form-item>
     <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/dui-jie-liao-tian-ping-tai/dui-jie-onebot-gocqhttp' target='_blank'>
       <el-link type='primary'>OneBot 文档</el-link>
     </a>
   </el-form>
   <el-form :model='mirai' v-else-if='type == "mirai"'>
     <el-form-item label='机器人QQ号'><el-input placeholder='请修改为你机器人的QQ号' v-model='mirai.qq' /></el-form-item>
     <el-form-item label='管理员QQ号'><el-input placeholder='请修改为机器人管理员的QQ号' v-model='mirai.manager_qq' /></el-form-item>
     <el-form-item label='Mirai API Key'><el-input placeholder='verifyKey' v-model='mirai.key' /></el-form-item>
     <el-form-item label='Mirai 主机'><el-input v-model='mirai.reverse_host' /></el-form-item>
     <el-form-item label='Mirai 端口'><el-input v-model='mirai.reverse_port' /></el-form-item>
     <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/dui-jie-liao-tian-ping-tai/dui-jie-mirai' target='_blank'>
       <el-link type='primary'>Mirai 文档</el-link>
     </a>
   </el-form>
   <el-form :model='telegram' v-else-if='type == "telegram"'>
     <el-form-item label='Bot Token'><el-input placeholder='你的 Bot token' v-model='telegram.token' /></el-form-item>
     <el-form-item label='Proxy'><el-input placeholder='可选, 留空默认系统设置' v-model='telegram.proxy' /></el-form-item>
     <el-form-item label='Chat ID'><el-input placeholder='管理员的 chat id' v-model='telegram.manager_chat' /></el-form-item>
     <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/dui-jie-liao-tian-ping-tai/dui-jie-telegram' target='_blank'>
       <el-link type='primary'>Telegram 文档</el-link>
     </a>
   </el-form>
   <el-form :model='discord' v-else-if='type == "discord"'>
     <el-form-item label='Bot Token'><el-input placeholder='Discord 机器人的 token' v-model='discord.token' /></el-form-item>
     <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/dui-jie-liao-tian-ping-tai/dui-jie-discord' target='_blank'>
       <el-link type='primary'>Discord 文档</el-link>
     </a>
   </el-form>
   <el-form :model='wechat' v-else-if='type == "wechat"'>
     <el-form-item label='主机名'><el-input placeholder='服务端开放的主机名' v-model='wechat.host' /></el-form-item>
     <el-form-item label='端口'><el-input placeholder='服务端开放的端口' v-model='wechat.port' /></el-form-item>
     <el-form-item label='开启调试'><el-switch v-model='wechat.debug' /></el-form-item>
     <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/dui-jie-liao-tian-ping-tai/dui-jie-ge-ren-wei-xin' target='_blank'>
       <el-link type='primary'>微信 文档</el-link>
     </a>
   </el-form>
   <el-form :model='wecom' v-else-if='type == "wecom"'>
     <el-form-item label='主机名'><el-input placeholder='服务端开放的主机名, 企业微信的回调地址, 需要能够被公网访问' v-model='wecom.host' /></el-form-item>
     <el-form-item label='端口'><el-input placeholder='服务端开放的端口' v-model='wecom.port' /></el-form-item>
     <el-form-item label='开启调试'><el-switch v-model='wecom.debug' /></el-form-item>
     <el-form-item label='企业 ID'><el-input placeholder='ww****' v-model='wecom.corp_id' /></el-form-item>
     <el-form-item label='Agent ID'><el-input placeholder='1000001' v-model='wecom.agent_id' /></el-form-item>
     <el-form-item label='Secret'><el-input placeholder='abc***' v-model='wecom.secret' /></el-form-item>
     <el-form-item label='Token'><el-input placeholder='abc***' v-model='wecom.token' /></el-form-item>
     <el-form-item label='Encoding AES Key'><el-input placeholder='abc***' v-model='wecom.encoding_aes_key' /></el-form-item>
     <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/dui-jie-liao-tian-ping-tai/dui-jie-qi-ye-wei-xin' target='_blank'>
       <el-link type='primary'>企业微信 文档</el-link>
     </a>
   </el-form>
   <el-button type='primary' plain class='save-button' @click='submit' :disabled='loader'>保存</el-button>
 </div>
</template>

<style>
@import "@/assets/style/main.css";
</style>