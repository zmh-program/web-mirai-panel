<script setup lang="ts">
import Config from '@/components/Config.vue'
import ShellCommand from '@/components/ShellCommand.vue'
import FileUpload from '@/components/FileUpload.vue'
import Info from '@/components/Info.vue'
</script>

<template>
  <main>
    <el-card class='card'><h1>🧨 监控</h1><el-divider /><Info /></el-card>
    <el-card class='card'><h1>📂 上传文件</h1><el-divider /><FileUpload /></el-card>
    <el-card class='card'><h1>👩‍💻 控制台</h1><el-divider /><ShellCommand /></el-card>
    <el-card class='card'><h1 style='padding-bottom: 8px'>💻 配置</h1><div style='height: 12px; width: 100%' /><Config /></el-card>
  </main>
</template>

<style>
@import "@/assets/style/main.css";
</style>
