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

const text_to_speech = reactive({
  engine: "",
  default: ""
})
const azure = reactive({
  tts_speech_key: "",
  tts_speech_service_region: ""
})
const vits = reactive({
  api_url: "",
  speed: 1.4,
  lang: "zh",
  timeout: 30,
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
            <el-radio label='wechat'>个人微信</el-radio>
            <el-radio label='wecom'>企业微信</el-radio>
          </el-radio-group>
          <br><br>
          <el-alert type='info' v-if='chatModel == "mirai"' :closable='false' show-icon>
            推荐使用&nbsp;<el-link class='link' type='primary' @click='chatModel = "cqhttp"'>CQHttp</el-link>
          </el-alert>
          <el-alert type='info' v-else-if='chatModel == "wechat"' :closable='false' show-icon>
            我们建议将本项目部署在国外服务器上，减少网络错误发生的概率。<br>
            Docker 用户别忘了将此处配置中的<strong style='font-weight: bold'>端口号</strong>映射出来，以便被访问到。
          </el-alert>
          <br>
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
            <el-form :model='wechat' v-else-if='chatModel == "wechat"'>
              <el-form-item label='主机名'><el-input placeholder='服务端开放的主机名' v-model='wechat.host' /></el-form-item>
              <el-form-item label='端口'><el-input placeholder='服务端开放的端口' v-model='wechat.port' /></el-form-item>
              <el-form-item label='开启调试'><el-switch v-model='wechat.debug' /></el-form-item>
              <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/dui-jie-liao-tian-ping-tai/dui-jie-ge-ren-wei-xin' target='_blank'>
                <el-link type='primary'>微信 文档</el-link>
              </a>
            </el-form>
            <el-form :model='wecom' v-else-if='chatModel == "wecom"'>
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
            <template v-if='aiModel == "bard"'><el-alert type='warning' :closable='false' show-icon>Bard 目前仅允许美国的 IP 访问，所以你很有可能需要设置代理。</el-alert><br></template>
            <template v-else-if='aiModel == "yiyan"'><el-alert type='warning' :closable='false' show-icon>请注意：该方法有封号风险(但是过一段时间就会解封)，具体原因未知，请自行取舍。</el-alert><br></template>
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
        <el-collapse-item name='ai' title='🎃 其他功能'>
          <el-card>
            <h3>🔊 文字转语音</h3><br>
            <el-radio-group v-model='text_to_speech.engine'>
              <el-radio label='azure'>Azure TTS</el-radio>
              <el-radio label='vits'>VITS</el-radio>
              <el-radio label='edge'>Edge TTS</el-radio>
            </el-radio-group><br><br>
          </el-card>
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

.link {
    transform: translateY(-3px);
}
</style>