<script setup lang="ts">
import { RouterView } from 'vue-router'
</script>

<template>
  <el-container class='container'>
    <el-header>
      <el-menu mode='horizontal'>
        <el-menu-item><img src='/favicon.ico' alt='' style='width: 24px'>&nbsp;ChatGPT for QQ</el-menu-item>
        <div style='flex-grow: 1'></div>
        <el-menu-item><a href='https://chatgpt-qq.lss233.com/' target='_blank'><el-link>文档</el-link></a></el-menu-item>
        <el-menu-item><a href='https://github.com/lss233/chatgpt-mirai-qq-bot' target='_blank'><el-link>GitHub</el-link></a></el-menu-item>
      </el-menu>
    </el-header>
    <el-container>
      <el-main><RouterView /></el-main>
    </el-container>
  </el-container>
</template>

<style scoped>
.container {
    max-width: 864px;
    margin: 0 auto;
    gap: 2px;
}
</style>