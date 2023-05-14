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
    <el-container class='main-container'>
      <el-aside id='aside'>
        <el-card class='card'>
          <div class='circle-group'>
            <div class='circle' style='background: rgb(245,49,38)' />
            <div class='circle' style='background: rgb(255,204,0)' />
            <div class='circle' style='background: rgb(76,217,100)' />
          </div>
          <el-divider style='margin-top: 12px' />
          <el-menu default-active="1" style='border-right: none; font-family: Poppins, sans-serif'>
            <el-menu-item index="1">🧨 监控 Monitor</el-menu-item>
            <el-menu-item index="2">📂 上传 Upload</el-menu-item>
            <el-menu-item index="3">👩‍💻 终端 Terminal</el-menu-item>
            <el-menu-item index="4">💻 配置 Configuration</el-menu-item>
          </el-menu>
        </el-card>
      </el-aside>
      <el-main>
        <router-view v-slot="{ Component }">
          <transition name="fade">
            <component :is="Component" />
          </transition>
        </router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<style scoped>
#aside {
    width: max-content;
}
.card {
    margin-top: 6px;
}
.main-container {
    gap: 2px;
    display: flex;
    flex-direction: row;
}

@media (max-width: 600px) {
    .main-container {
        flex-direction: column;
    }
    #aside {
        width: calc(100% - 4px);
        margin: 2px;
    }
}

@media (min-width: 1024px) {
    .container {
        width: calc(100% - 16px);
        margin: 0 8px;
    }
}
.circle-group {
    display: flex;
    flex-direction: row;
    gap: 4px;
}
.circle {
    width: 14px;
    height: 14px;
    border-radius: 50%;
}
.container {
    margin: 0 auto;
}
.fade-enter-active,
.fade-leave-active {
    transition: 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
    filter: blur(10px);
}

.fade-leave-to {
    display: none;
}
</style>
