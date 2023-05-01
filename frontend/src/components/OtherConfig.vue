<script setup lang='ts'>
import { reactive, ref } from 'vue'
import axios from 'axios'

const features = reactive({
  text_to_image: false,
  text_to_speech: false,
  sdwebui: false,
})
const text_to_speech = reactive({
  engine: "azure",
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

const sdwebui = reactive({
  api_url: '',
  prompt_prefix: '',
  negative_prompt: '',
  sampler_index: '',
  filter_nsfw: true,
  timeout: 10.0
})

const text_to_image = reactive({
  always: true,
  font_size: 30,
  width: 700,
  font_path: "fonts/sarasa-mono-sc-regular.ttf",
  offset_x: 50,
  offset_y: 50
})



const loader = ref(false);
function submit() {
  loader.value = true;
  const data: Record<string, Record<string, any>> = {};
  if (features.text_to_image) data['text_to_image'] = text_to_image;
  if (features.text_to_speech) data['text_to_speech'] = text_to_speech;
  if (features.sdwebui) data['sdwebui'] = sdwebui;


  axios.post('/api/save/other', data)
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
  <el-card>
    <h3><el-checkbox v-model='features.text_to_image' />&nbsp;&nbsp;📝 文字转图片</h3><br>
    <el-alert type='success' :closable='false' show-icon>
      机器人可以把文字转成图片，这样可以避免消息发到 QQ 群中被腾讯拦截，或者公式直接输出导致可读性太低的问题。
    </el-alert><br>
    <el-form :model='text_to_image' :disabled='!features.text_to_image'>
      <el-form-item label='强制开启'><el-switch v-model='text_to_image.always' /></el-form-item>
      <el-form-item label='字体大小'><el-input-number v-model='text_to_image.font_size' /></el-form-item>
      <el-form-item label='图片宽度'><el-input-number v-model='text_to_image.width' /></el-form-item>
      <el-form-item label='字体'><el-input v-model='text_to_image.font_path' /></el-form-item>
      <el-form-item label='X坐标 起始点'><el-input-number v-model='text_to_image.offset_x' /></el-form-item>
      <el-form-item label='Y坐标 起始点'><el-input-number v-model='text_to_image.offset_y' /></el-form-item>
      <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/wen-zi-zhuan-tu-pian' target='_blank'>
        <el-link type='primary'>文字转图片 文档</el-link>
      </a><br>
      <el-button type='primary' plain class='save-button' @click='submit' :disabled='loader'>保存</el-button>
    </el-form>
  </el-card><br>
  <el-card>
    <h3><el-checkbox v-model='features.text_to_speech' />&nbsp;&nbsp;🔊 文字转语音</h3><br>
    <el-radio-group v-model='text_to_speech.engine' :disabled='!features.text_to_speech'>
      <el-radio label='azure'>Azure TTS</el-radio>
      <el-radio label='vits'>VITS</el-radio>
      <el-radio label='edge'>Edge TTS</el-radio>
    </el-radio-group><br><br>
    <el-form-item label='引擎'><el-input disabled v-model='text_to_speech.engine' /></el-form-item>
    <el-form :model='azure' v-if='text_to_speech.engine == "azure"' :disabled='!features.text_to_speech'>
      <el-form-item label='音色'><el-input placeholder='zh-CN-XiaoyouNeural' v-model='text_to_speech.default' /></el-form-item>
      <el-form-item label='Key'><el-input placeholder='你的秘钥 (TTS Speech Key)' v-model='azure.tts_speech_key' /></el-form-item>
      <el-form-item label='地域'><el-input placeholder='你的服务地域 (TTS Speech Service Region)' v-model='azure.tts_speech_service_region' /></el-form-item>
      <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/wen-zi-zhuan-yu-yin/azure-tts-yu-yin-jie-ru-jiao-cheng' target='_blank'>
        <el-link type='primary'>Azure TTS 文档</el-link>
      </a>
    </el-form>
    <el-form :model='vits' v-if='text_to_speech.engine == "vits"' :disabled='!features.text_to_speech'>
      <el-form-item label='音色'><el-input placeholder='0' v-model='text_to_speech.default' /></el-form-item>
      <el-form-item label='接口'><el-input placeholder='后端接口地址' v-model='vits.api_url' /></el-form-item>
      <el-form-item label='语音速度'><el-input-number placeholder='语言速度' v-model='vits.speed' /></el-form-item>
      <el-form-item label='目标语言'>
        <el-select v-model='vits.lang'>
          <el-option value='zh' >中文 (zh)</el-option>
          <el-option value='ja' >日文 (ja)</el-option>
          <el-option value='mix' >混合 (mix)</el-option>
        </el-select>
      </el-form-item>
      <el-form-item label='超时时间'><el-input-number placeholder='超时时间' v-model='vits.timeout' /></el-form-item>
      <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/wen-zi-zhuan-yu-yin/vits-yu-yin-jie-ru-jiao-cheng' target='_blank'>
        <el-link type='primary'>VITS 文档</el-link>
      </a>
    </el-form>
    <el-form :model='text_to_speech' v-if='text_to_speech.engine == "edge"' :disabled='!features.text_to_speech'>
      <el-form-item label='音色'><el-input placeholder='zh-CN-XiaoxiaoNeural' v-model='text_to_speech.default' /></el-form-item>
      <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/wen-zi-zhuan-yu-yin/edge-tts-yu-yin-jie-ru-jiao-cheng' target='_blank'>
        <el-link type='primary'>Edge TTS 文档</el-link>
      </a>
    </el-form>
    <el-button type='primary' plain class='save-button' @click='submit' :disabled='loader && features.text_to_speech'>保存</el-button>
  </el-card><br>
  <el-card>
    <h3><el-checkbox v-model='features.sdwebui' />&nbsp;&nbsp;🍒 AI 画图 (Stable Diffusion)</h3><br>
    <el-alert type='info' :closable='false' show-icon>
      Stable Diffusion (如下配置) <br>
      Bing 画图 (请跳转<span class='bold'>Bing</span>开启<span class='bold'>Bing 绘图</span>) <br>
      OpenAI 画图 (请跳转<span class='bold'>ChatGPT</span>) <br>
      文心一言 (请跳转<span class='bold'>文心一言</span>)
    </el-alert><br>
    <el-form :model='sdwebui' :disabled='!features.sdwebui'>
      <el-form-item label='接口'><el-input placeholder='sd-webui 的接口地址' v-model='sdwebui.api_url' /></el-form-item>
      <el-form-item label='内置提示词'><el-input placeholder='所有的画图内容都会加上这些提示词, 如 ‘masterpiece, best quality,’' v-model='sdwebui.prompt_prefix' /></el-form-item>
      <el-form-item label='负面提示词'><el-input placeholder='如‘missing fingers,’' v-model='sdwebui.negative_prompt' /></el-form-item>
      <el-form-item label='取样器索引'><el-input placeholder='Sampler Index, 如‘DPM++ SDE Karras’' v-model='sdwebui.sampler_index' /></el-form-item>
      <el-form-item label='超时时间'><el-input-number v-model='sdwebui.timeout' /></el-form-item>
      <el-form-item label='Filter NSFW'><el-switch v-model='sdwebui.filter_nsfw' /></el-form-item>
      <a href='https://chatgpt-qq.lss233.com/pei-zhi-wen-jian-jiao-cheng/ai-hua-tu' target='_blank'>
        <el-link type='primary'>AI 画图 文档</el-link>
      </a><br>
      <el-button type='primary' plain class='save-button' @click='submit' :disabled='loader'>保存</el-button>
    </el-form>
  </el-card>
</template>

<style>
@import "@/assets/style/main.css";
</style>