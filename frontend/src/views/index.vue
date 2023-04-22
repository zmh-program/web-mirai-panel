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
  // plus: true,
  // model: "",
  api_key: "",
  api_endpoint: "https://api.openai.com/v1"  // outside account
})
const bing = reactive({
  cookie_content: '',  // 注意单引号
  wss_link: "wss://chatgpt-qq.lss233.com/sydney/ChatHub",
  bing_endpoint: "https://chatgpt-qq.lss233.com/edgesvc/turing/conversation/create",
  proxy: "",
  show_suggestions: false,
  show_references: false,
  show_remaining_count: false,
  use_drawing: false
})
const bard = reactive({
  cookie_content: '',
  proxy: ""
})
const yiyan = reactive({
  BDUSS: '',
  BAIDUID: '',
  proxy: ""
})
const chatglm = reactive({
  api_endpoint: "http://127.0.0.1:8000",
  max_turns: 10,
  timeout: 360
})
const poe = reactive({
  p_b: "",
  proxy: ""
})
</script>

<template>
  <main>
    <el-card class='card'>
      <el-collapse v-model='collapse' id='collapse'>
        <el-collapse-item name='chat' title='📫 接入聊天平台'>
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
        <el-collapse-item name='ai' title='✨ 接入AI平台'>
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
              <template v-else>
                <el-form-item label='API Key'><el-input placeholder='sk-*****' v-model='chatgpt.api_key' /></el-form-item>
                <el-form-item label='接入点'><el-input placeholder='API版 ChatGPT 接入点' v-model='chatgpt.api_endpoint' /></el-form-item>
              </template>
              <el-form-item label='Proxy'><el-input placeholder='可选, 留空默认系统设置' v-model='chatgpt.proxy' /></el-form-item>
              <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/jie-ru-ai-ping-tai/jie-ru-openai-de-chatgpt' target='_blank'>
                <el-link type='primary'>chatGPT 文档</el-link>
              </a>
            </el-form>
            <el-form :model='bing' v-else-if='aiModel == "bing"'>
              <el-form-item label='Cookie'><el-input placeholder='[{"domain": ".bing.com", ...}]' v-model='bing.cookie_content' /></el-form-item>
              <el-form-item label='Proxy'><el-input placeholder='可选, 留空默认系统设置或者使用接入点' v-model='bing.proxy' /></el-form-item>
              <el-form-item label='WebSocket 接入点'><el-input placeholder='https://' v-model='bing.wss_link' /></el-form-item>
              <el-form-item label='会话创建接入点'><el-input placeholder='wss://' v-model='bing.bing_endpoint' /></el-form-item>
              <el-form-item label='显示建议'><el-switch v-model='bing.show_suggestions' /></el-form-item>
              <el-form-item label='显示引用资料'><el-switch v-model='bing.show_references' /></el-form-item>
              <el-form-item label='显示剩余次数'><el-switch v-model='bing.show_remaining_count' /></el-form-item>
              <el-form-item label='Bing 绘图'><el-switch v-model='bing.use_drawing' /></el-form-item>
              <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/jie-ru-ai-ping-tai/jie-ru-new-bing-sydney' target='_blank'>
                <el-link type='primary'>Bing 文档</el-link>
              </a>
            </el-form>
            <el-form :model='bard' v-else-if='aiModel == "bard"'>
              <el-form-item label='Cookie'><el-input placeholder='Bard Cookie' v-model='bard.cookie_content' /></el-form-item>
              <el-form-item label='Proxy'><el-input placeholder='可选, 留空默认系统设置' v-model='bard.proxy' /></el-form-item>
              <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/jie-ru-ai-ping-tai/jie-ru-google-bard' target='_blank'>
                <el-link type='primary'>Bard 文档</el-link>
              </a>
            </el-form>
            <el-form :model='yiyan' v-else-if='aiModel == "yiyan"'>
              <el-form-item label='BDUSS'><el-input placeholder='Baidu USS' v-model='yiyan.BDUSS' /></el-form-item>
              <el-form-item label='BAIDUID'><el-input placeholder='Baidu ID' v-model='yiyan.BAIDUID' /></el-form-item>
              <el-form-item label='Proxy'><el-input placeholder='可选' v-model='yiyan.proxy' /></el-form-item>
              <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/jie-ru-ai-ping-tai/jie-ru-wen-xin-yi-yan' target='_blank'>
                <el-link type='primary'>文心一言 文档</el-link>
              </a>
            </el-form>
            <el-form :model='chatglm' v-else-if='aiModel == "chatglm"'>
              <el-form-item label='接入点'><el-input placeholder='ChatGLM 接口地址' v-model='chatglm.api_endpoint' /></el-form-item>
              <el-form-item label='单会话最大轮数'><el-input placeholder='最大记忆的对话轮数 (类似于ReplayBuffer大小)' v-model='chatglm.max_turns' /></el-form-item>
              <el-form-item label='请求超时时间 (s)'><el-input placeholder='可选' v-model='chatglm.timeout' /></el-form-item>
              <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/jie-ru-ai-ping-tai/jie-ru-chatglm' target='_blank'>
                <el-link type='primary'>ChatGLM 文档</el-link>
              </a>
            </el-form>
            <el-form :model='poe' v-else-if='aiModel == "poe"'>
              <el-form-item label='p_b'><el-input placeholder='Cookie中的 p_b 字段' v-model='poe.p_b' /></el-form-item>
              <el-form-item label='Proxy'><el-input placeholder='可选, 留空默认系统设置' v-model='poe.proxy' /></el-form-item>
              <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/jie-ru-ai-ping-tai/jie-ru-poe.com' target='_blank'>
                <el-link type='primary'>Poe 文档</el-link>
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