<script setup lang="ts">
import { RouterView } from 'vue-router'
import router from '@/router'
import { collapse } from '@/assets/script/config'

function route(current: string, path: string[]) {
  const [name, hash] = path;
  if (name === "config") collapse.value = [hash, ];
  router.push("/" + (name === "monitor" ? "" : name));
}
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
        <el-card class='card sidebar'>
          <div class='circle-group'>
            <div class='circle' style='background: rgb(245,49,38)' />
            <div class='circle' style='background: rgb(255,204,0)' />
            <div class='circle' style='background: rgb(76,217,100)' />
          </div>
          <el-divider style='margin-top: 20px' />
          <el-menu @select="route" default-active="monitor" style='border-right: none; font-family: Poppins, sans-serif'>
            <el-menu-item index="monitor">🧨 监控 Monitor</el-menu-item>
            <el-menu-item index="upload">📂 上传 Upload</el-menu-item>
            <el-menu-item index="term">👩‍💻 终端 Terminal</el-menu-item>
            <el-sub-menu index="config">
              <template #title>💻 配置 Configuration</template>
              <el-menu-item index="chat">📫 接入聊天平台</el-menu-item>
              <el-menu-item index="ai">✨ 接入AI平台</el-menu-item>
              <el-menu-item index="other">🎃 其他功能</el-menu-item>
            </el-sub-menu>
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
    .sidebar {
        min-height: max(426px, calc(60vh + 2px))
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
