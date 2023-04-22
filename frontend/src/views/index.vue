<script setup lang="ts">
import { reactive, ref } from 'vue'
import type { Ref } from 'vue'

const collapse: Ref<string[]> = ref(['chat']);
const chatModel: Ref<string> = ref('cqhttp');

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

</script>

<template>
  <main>
    <el-card class='card'>
      <el-collapse v-model='collapse'>
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
            </el-form>
            <el-form :model='cqhttp' v-else-if='chatModel == "mirai"'>
              <el-form-item label='机器人QQ号'><el-input placeholder='请修改为你机器人的QQ号' v-model='mirai.qq' /></el-form-item>
              <el-form-item label='管理员QQ号'><el-input placeholder='请修改为机器人管理员的QQ号' v-model='mirai.manager_qq' /></el-form-item>
              <el-form-item label='Mirai API Key'><el-input placeholder='verifyKey' v-model='mirai.key' /></el-form-item>
              <el-form-item label='Mirai 主机'><el-input v-model='mirai.reverse_host' /></el-form-item>
              <el-form-item label='Mirai 端口'><el-input v-model='mirai.reverse_port' /></el-form-item>
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