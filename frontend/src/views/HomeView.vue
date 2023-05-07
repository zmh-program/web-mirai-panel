<script setup lang="ts">
import { ref } from 'vue'
import type { Ref } from 'vue'
import ChatPlatform from '@/components/ChatPlatform.vue'
import AIPlatform from '@/components/AIPlatform.vue'
import OtherConfig from '@/components/OtherConfig.vue'
import ShellCommand from '@/components/ShellCommand.vue'
import FileUpload from '@/components/FileUpload.vue'

const collapse: Ref<string[]> = ref(['chat', 'ai']);
</script>

<template>
  <main>
    <el-card class='card'>
      <h1>📂 上传文件</h1><el-divider />
      <FileUpload />
    </el-card>
    <el-card class='card'>
      <h1>👩‍💻 控制台</h1><el-divider />
      <ShellCommand />
    </el-card>
    <el-card class='card'>
      <h1 style='padding-bottom: 8px'>💻 配置</h1>
      <el-collapse v-model='collapse' id='collapse'>
        <el-collapse-item name='chat' title='📫 接入聊天平台'><ChatPlatform /></el-collapse-item>
        <el-collapse-item name='ai' title='✨ 接入AI平台'><AIPlatform /></el-collapse-item>
        <el-collapse-item name='other' title='🎃 其他功能'><OtherConfig /></el-collapse-item>
      </el-collapse>
    </el-card>
  </main>
</template>

<style>
@import "@/assets/style/main.css";
</style>
