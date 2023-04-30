<script setup lang="ts">
import { ref } from 'vue'
import type { Ref } from 'vue'
import ChatPlatform from '@/components/ChatPlatform.vue'
import AIPlatform from '@/components/AIPlatform.vue'
import OtherConfig from '@/components/OtherConfig.vue'

const collapse: Ref<string[]> = ref(['chat', 'ai']);
</script>

<template>
  <main>
    <el-card class='card'>
      <el-collapse v-model='collapse' id='collapse'>
        <el-collapse-item name='chat' title='📫 接入聊天平台'><ChatPlatform /></el-collapse-item>
        <el-collapse-item name='ai' title='✨ 接入AI平台'><AIPlatform /></el-collapse-item>
        <el-collapse-item name='other' title='🎃 其他功能'><OtherConfig /></el-collapse-item>
      </el-collapse>
    </el-card>
  </main>
</template>

<style>
@import "@/assets/main.css";
</style>