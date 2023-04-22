<script setup lang="ts">
import { reactive, ref } from 'vue'
import type { Ref } from 'vue'

const collapse: Ref<string[]> = ref(['chat', 'ai']);
const chatModel: Ref<string> = ref('cqhttp');
const aiModel: Ref<string> = ref('chatgpt');

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

const chatSelector = {
  cqhttp,
  mirai,
  telegram,
  discord,
}


const chatgpt = reactive({
  mode: "web",
  access_token: "",
  browserless_endpoint: "https://chatgpt-proxy.lss233.com/api/",  // outside account
  auto_remove_old_conversations: false,
  title_pattern: "",
  proxy: "",
  plus: true,
  model: "",

  api_key: "",
  api_endpoint: "https://api.openai.com/v1"  // outside account
})

</script>

<template>
  <main>
    <el-card class='card'>
      <el-collapse v-model='collapse' id='collapse'>
        <el-collapse-item name='chat' title='聊天平台'>
          <el-radio-group v-model='chatModel'>
            <el-radio label='cqhttp'>OneBot (CQHttp)</el-radio>
            <el-radio label='mirai'>Mirai</el-radio>
            <el-radio label='telegram'>Telegram</el-radio>
            <el-radio label='discord'>Discord</el-radio>
          </el-radio-group><br><br>
          <div>
            <el-form :model='cqhttp' v-if='chatModel == "cqhttp"'>
              <el-form-item label='机器人QQ号'><el-input placeholder='请修改为你机器人的QQ号' v-model='cqhttp.qq' /></el-form-item>
              <el-form-item label='管理员QQ号'><el-input placeholder='请修改为机器人管理员的QQ号' v-model='cqhttp.manager_qq' /></el-form-item>
              <el-form-item label='CQHttp 主机'><el-input v-model='cqhttp.host' /></el-form-item>
              <el-form-item label='CQHttp 端口'><el-input v-model='cqhttp.port' /></el-form-item>
              <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/dui-jie-liao-tian-ping-tai/dui-jie-onebot-gocqhttp' target='_blank'>
                <el-link type='primary'>OneBot 文档</el-link>
              </a>
            </el-form>
            <el-form :model='mirai' v-else-if='chatModel == "mirai"'>
              <el-form-item label='机器人QQ号'><el-input placeholder='请修改为你机器人的QQ号' v-model='mirai.qq' /></el-form-item>
              <el-form-item label='管理员QQ号'><el-input placeholder='请修改为机器人管理员的QQ号' v-model='mirai.manager_qq' /></el-form-item>
              <el-form-item label='Mirai API Key'><el-input placeholder='verifyKey' v-model='mirai.key' /></el-form-item>
              <el-form-item label='Mirai 主机'><el-input v-model='mirai.reverse_host' /></el-form-item>
              <el-form-item label='Mirai 端口'><el-input v-model='mirai.reverse_port' /></el-form-item>
              <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/dui-jie-liao-tian-ping-tai/dui-jie-mirai' target='_blank'>
                <el-link type='primary'>Mirai 文档</el-link>
              </a>
            </el-form>
            <el-form :model='telegram' v-else-if='chatModel == "telegram"'>
              <el-form-item label='Bot Token'><el-input placeholder='你的 Bot token' v-model='telegram.token' /></el-form-item>
              <el-form-item label='Proxy'><el-input placeholder='可选, 留空默认系统设置' v-model='telegram.proxy' /></el-form-item>
              <el-form-item label='Chat ID'><el-input placeholder='管理员的 chat id' v-model='telegram.manager_chat' /></el-form-item>
              <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/dui-jie-liao-tian-ping-tai/dui-jie-telegram' target='_blank'>
                <el-link type='primary'>Telegram 文档</el-link>
              </a>
            </el-form>
            <el-form :model='discord' v-else-if='chatModel == "discord"'>
              <el-form-item label='Bot Token'><el-input placeholder='Discord 机器人的 token' v-model='discord.token' /></el-form-item>
              <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/dui-jie-liao-tian-ping-tai/dui-jie-discord' target='_blank'>
                <el-link type='primary'>Discord 文档</el-link>
              </a>
            </el-form>
          </div>
        </el-collapse-item>
        <el-collapse-item name='ai' title='AI平台'>
          <el-radio-group v-model='aiModel'>
            <el-radio label='chatgpt'>chatGPT</el-radio>
            <el-radio label='bing'>New Bing</el-radio>
            <el-radio label='bard'>Google Bard</el-radio>
            <el-radio label='yiyan'>文心一言</el-radio>
            <el-radio label='chatglm'>chatGLM</el-radio>
            <el-radio label='poe'>Poe</el-radio>
          </el-radio-group><br><br>
          <div>
            <el-form :model='chatgpt' v-if='aiModel == "chatgpt"'>
              <el-form-item label='接入模式'>
                <el-radio-group v-model='chatgpt.mode'>
                  <el-radio-button label='web'>网页版</el-radio-button>
                  <el-radio-button label='api'>API版</el-radio-button>
                </el-radio-group>
              </el-form-item>
              <template v-if='chatgpt.mode == "web"'>
                <el-form-item label='Token'><el-input placeholder='ey********' v-model='chatgpt.access_token' /></el-form-item>
                <el-form-item label='接入点'><el-input placeholder='网页版 ChatGPT 接入点' v-model='chatgpt.browserless_endpoint' /></el-form-item>
                <el-form-item label='会话标题'><el-input placeholder='qq-{session_id}' v-model='chatgpt.title_pattern' /></el-form-item>
                <el-form-item label='对话记录自动删除'><el-switch v-model='chatgpt.auto_remove_old_conversations' /></el-form-item>
              </template>
              <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/jie-ru-ai-ping-tai/jie-ru-openai-de-chatgpt' target='_blank'>
                <el-link type='primary'>chatGPT 文档</el-link>
              </a>
            </el-form>
            <el-form :model='mirai' v-else-if='chatModel == "mirai"'>
              <el-form-item label='机器人QQ号'><el-input placeholder='请修改为你机器人的QQ号' v-model='mirai.qq' /></el-form-item>
              <el-form-item label='管理员QQ号'><el-input placeholder='请修改为机器人管理员的QQ号' v-model='mirai.manager_qq' /></el-form-item>
              <el-form-item label='Mirai API Key'><el-input placeholder='verifyKey' v-model='mirai.key' /></el-form-item>
              <el-form-item label='Mirai 主机'><el-input v-model='mirai.reverse_host' /></el-form-item>
              <el-form-item label='Mirai 端口'><el-input v-model='mirai.reverse_port' /></el-form-item>
              <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/dui-jie-liao-tian-ping-tai/dui-jie-mirai' target='_blank'>
                <el-link type='primary'>Mirai 文档</el-link>
              </a>
            </el-form>
            <el-form :model='telegram' v-else-if='chatModel == "telegram"'>
              <el-form-item label='Bot Token'><el-input placeholder='你的 Bot token' v-model='telegram.token' /></el-form-item>
              <el-form-item label='Proxy'><el-input placeholder='可选, 留空默认系统设置' v-model='telegram.proxy' /></el-form-item>
              <el-form-item label='Chat ID'><el-input placeholder='管理员的 chat id' v-model='telegram.manager_chat' /></el-form-item>
              <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/dui-jie-liao-tian-ping-tai/dui-jie-telegram' target='_blank'>
                <el-link type='primary'>Telegram 文档</el-link>
              </a>
            </el-form>
            <el-form :model='discord' v-else-if='chatModel == "discord"'>
              <el-form-item label='Bot Token'><el-input placeholder='Discord 机器人的 token' v-model='discord.token' /></el-form-item>
              <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/dui-jie-liao-tian-ping-tai/dui-jie-discord' target='_blank'>
                <el-link type='primary'>Discord 文档</el-link>
              </a>
            </el-form>
          </div>
        </el-collapse-item>
      </el-collapse>
    </el-card>
  </main>
</template>

<style scoped>
.card {
    width: 100%;
    min-width: 280px;
    height: max-content;
    min-height: 120px;
}
</style>