<script setup lang='ts'>
import { reactive, ref } from 'vue'
import axios from 'axios'
import { message } from '@/assets/script/utils'


let response = reactive({
  mode: "mixed",
  buffer_delay: 15,
  default_ai: "chatgpt-web",
  placeholder: "您好！我是 Assistant，一个由 OpenAI 训练的大型语言模型。我不是真正的人，而是一个计算机程序，可以通过文本聊天来帮助您解决问题。如果您有任何问题，请随时告诉我，我将尽力回答。\\n如果您需要重置我们的会话，请回复`重置会话`。",
  error_format: "出现故障！如果这个问题持续出现，请和我说“重置会话” 来开启一段新的会话，或者发送 “回滚会话” 来回溯到上一条对话，你上一条说的我就当作没看见。\\n{exc}",
  error_network_failure: "网络故障！连接 OpenAI 服务器失败，我需要更好的网络才能服务！\\n{exc}",
  error_session_authenciate_failed: "身份验证失败！无法登录至 ChatGPT 服务器，请检查账号信息是否正确！\\n{exc}",
  error_request_too_many: "糟糕！当前收到的请求太多了，我需要一段时间冷静冷静。你可以选择“重置会话”，或者过一会儿再来找我！\\n{exc}",
  error_server_overloaded: "抱歉，当前服务器压力有点大，请稍后再找我吧！",
  reset: "会话已重置。",
  rollback_success: "已回滚至上一条对话，你刚刚发的我就忘记啦！",
  rollback_fail: "回滚失败，没有更早的记录了！",
  quote: true,
  timeout: 30.0,
  timeout_format: "我还在思考中，请再等一下~",
  max_timeout: 600,
  cancel_wait_too_long: "啊哦，这个问题有点难，让我想了好久也没想明白。试试换个问法？",
  max_queue_size: 10,
  queue_full: "抱歉！我现在要回复的人有点多，暂时没有办法接收新的消息了，请过会儿再给我发吧！",
  queued_notice_size: 3,
  queued_notice: "消息已收到！当前我还有{queue_size}条消息要回复，请您稍等。",
})
const loader = ref(false);
function submit() {
  loader.value = true;
  axios.post('/api/save/response', { response })
    .then(() => {
      loader.value = false;
      message({
        type: 'success',
        message: `保存成功！`,
      });
    })
    .catch(() => {
      loader.value = false;
      message({
        type: 'error',
        message: `保存时出错！`,
      });
    })
}

axios.get("/api/load/response")
  .then((res) => {
    const data = res.data.data.response;  //@ts-ignore
    for (let key in data) response[key] = data[key];
  })
  .catch(() => {
    message({
      type: 'error',
      message: `获取回复内容配置失败！`,
    });
  })
</script>

<template>
  <div>
    <el-form :model='response'>
      <el-form-item label='响应模式'>
        <el-select v-model='response.mode'>
          <el-option value='mixed'>图文混合模式 (mixed)</el-option>
          <el-option value='text'>文字模式 (text)</el-option>
          <el-option value='image'>图片模式 (image)</el-option>
        </el-select>
      </el-form-item>
      <el-text>
        <template v-if='response.mode === "mixed"'>
          在这个模式下，普通文本会以文字形式发送，而 Markdown、公式等富文本会以图片形式发送。
        </template>
        <template v-if='response.mode === "text"'>
          在这个模式下，消息会全部以文字的形式发送。<br>
          需要注意的是，在 QQ 群中，由于腾讯风控比较严格，文字消息可能会发送失败。 此时机器人会尝试使用图片模式来重新发送内容。
        </template>
        <template v-if='response.mode === "image"'>
          在这个模式下，机器人的消息会渲染成图片再发送。
        </template>
        <el-divider />
      </el-text>
      <el-form-item label='分段发送延时'><el-input-number :min='0' v-model='response.buffer_delay' /></el-form-item>
      <el-text>
        有些时候，AI 生成回复所花费的时间过长。 为了避免长时间的等待，我们加入了分段发送功能。<br>
        这个功能会每隔一段时间将 AI 生成的内容发送给用户，参数的单位为秒。<br>
        如果你要开启这个功能，建议把参数设置为 <el-text type='primary'>15</el-text> 或以上，以免出现 BUG 和刷屏。<br>
        如果你把参数设置成 <el-text type='primary'>0</el-text>，即表示关闭分段发送功能，消息会等待 AI 全部生成完毕以后再回复。
        <el-divider />
      </el-text>
      <el-form-item label='默认语言模型'>
        <el-select v-model='response.default_ai'>
          <el-option value="chatgpt-web">网页版 ChatGPT</el-option>
          <el-option value="chatgpt-api">API 版 ChatGPT (GPT3.5-turbo)</el-option>
          <el-option value="bing-c">New Bing (新必应对话风格-创造力)</el-option>
          <el-option value="bing-p">New Bing (新必应对话风格-精确)</el-option>
          <el-option value="bing-b">New Bing (新必应对话风格-平衡)</el-option>
          <el-option value="bard">Google Bard</el-option>
          <el-option value="yiyan">百度 文心一言 网页版</el-option>
          <el-option value="chatglm-api">清华 ChatGLM-API 接口</el-option>
          <el-option value="sage">POE Sage 模型</el-option>
          <el-option value="beaver">POE GPT4 模型</el-option>
          <el-option value="claude2">POE Claude2 模型</el-option>
          <el-option value="claude">POE Claude 模型</el-option>
          <el-option value="chinchilla">POE ChatGPT 模型</el-option>
          <el-option value="nutria">POE Dragonfly 模型</el-option>
        </el-select>
      </el-form-item>
      <el-text>
        默认情况下，程序会根据已经接入的语言模型设置，自动选择语言模型（不要钱的优先）。
        <el-divider />
      </el-text>
      <el-form-item label='引用发送的消息'><el-switch v-model='response.quote' /></el-form-item>
      <el-text>
        你可以设置机器人在回复时引用发送的消息，方便定位上下文。
        <el-divider />
      </el-text>
      <el-text class='title'>
        消息排队
      </el-text><br><br>
      <el-alert :closable='false' show-icon type='info'>
        因为聊天是有上下文的，机器人必须一条一条地处理发送过来的消息，才能保证上下文的连贯性。<br>
        当消息发送过多，机器人还没来得及反应时，后来的消息会加入到一个 <el-text type='primary'>队列</el-text> 中等待。
      </el-alert><br>
      <el-form-item label='最大消息列队长度'><el-input-number :min='0' v-model='response.max_queue_size' /></el-form-item>
      <el-text>
        等待处理的消息的最大数量，如果要关闭此功能，设置为 <el-text type='primary'>0</el-text><br><br>
      </el-text>
      <el-form-item label='列队满时提示'><el-input v-model='response.queue_full' /></el-form-item>
      <el-text>
        队列满时机器人将会发出此提示<br><br>
      </el-text>
      <el-form-item label='发送通知最小值'><el-input-number :min='0' v-model='response.queued_notice_size' /></el-form-item>
      <el-text>
        新消息加入队列会发送通知的长度最小值，具体参见下发配置。<br><br>
      </el-text>
      <el-form-item label='进入列队通知'><el-input v-model='response.queued_notice' /></el-form-item>
      <el-text>
        新消息进入队列时，发送的通知。 <el-text type='primary'>queue_size</el-text> 是当前排队的消息数
        <el-divider />
      </el-text>
      <el-text class='title'>消息等待</el-text><br><br>
      <el-text>如果语言模型太久没有响应，机器人可以发送一段消息安抚用户。</el-text><br><br>
      <el-form-item label='等待时间'><el-input-number :min='0' v-model='response.timeout' /></el-form-item>
      <el-form-item label='等待提醒'><el-input v-model='response.timeout_format' /></el-form-item>
      <el-form-item label='超时时间'><el-input-number :min='0' v-model='response.max_timeout' /></el-form-item>
      <el-form-item label='超时提醒'><el-input v-model='response.cancel_wait_too_long' /></el-form-item>
      <el-divider />
      <el-text class='title'>其他消息提示</el-text><br><br>
      <el-form-item label='回复为空时发送的消息'><el-input v-model='response.placeholder' /></el-form-item>
      <el-form-item label="发生错误时发送的消息"><el-input v-model="response.error_format" /></el-form-item>
      <el-form-item label="发生网络异常时发送的消息"><el-input v-model="response.error_network_failure" /></el-form-item>
      <el-form-item label="重置会话时发送的消息"><el-input v-model="response.reset" /></el-form-item>
      <el-form-item label="回滚成功时发送的消息"><el-input v-model="response.rollback_success" /></el-form-item>
      <el-form-item label="回滚失败时发送的消息"><el-input v-model="response.rollback_fail" /></el-form-item>
      <el-form-item label="服务器提示负载过高时的提示"><el-input v-model="response.error_server_overloaded" /></el-form-item>
      <el-form-item label="OpenAI 账号登录失效时的提示"><el-input v-model="response.error_session_authenciate_failed" /></el-form-item>
      <el-form-item label="OpenAI 提示太多请求时的提示"><el-input v-model="response.error_request_too_many" /></el-form-item>

      <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/hui-fu-nei-rong' target='_blank'>
        <el-link type='primary'>回复内容 文档</el-link>
      </a>
    </el-form>
    <el-button type='primary' plain class='save-button' @click='submit' :disabled='loader'>保存</el-button>
  </div>
</template>

<style>
@import "@/assets/style/main.css";
.title {
  font-weight: bold;
  font-size: 18px !important;
}
</style>
