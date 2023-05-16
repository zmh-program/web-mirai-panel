<script setup lang='ts'>
import { ref } from 'vue'
import type { Ref } from 'vue'
import ChatPlatform from '@/components/ConfigComponents/ChatPlatform.vue'
import OtherConfig from '@/components/ConfigComponents/OtherConfig.vue'
import AIPlatform from '@/components/ConfigComponents/AIPlatform.vue'

const collapse: Ref<string[]> = ref(['chat', 'ai']);
</script>

<template>
  <el-card class='card'>
    <h1 style='padding-bottom: 8px'>💻 配置</h1><div style='height: 12px; width: 100%' />
    <el-collapse v-model='collapse' id='collapse'>
      <el-collapse-item name='chat' id='chat' title='📫 接入聊天平台'><ChatPlatform /></el-collapse-item>
      <el-collapse-item name='ai' id='ai' title='✨ 接入AI平台'><AIPlatform /></el-collapse-item>
      <el-collapse-item name='other' id='other' title='🎃 其他功能'><OtherConfig /></el-collapse-item>
    </el-collapse>
  </el-card>
</template>
<style>
@import "@/assets/style/main.css";
</style>
