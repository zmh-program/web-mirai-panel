<script setup lang='ts'>
import { reactive } from 'vue'
import { settings } from '@/assets/script/config'

let timeout = 0;
function submit() {
  clearTimeout(timeout);
  timeout = setTimeout(() => {
  }, 500);
}
</script>

<template>
  <el-card class='card'>
    <h1>🔧 设置</h1>
    <el-divider style='padding: 30px 0; transform: translateY(20px)'/>
    <el-form class='form' :model='settings'>
      <el-form-item label='密码'><el-input v-model='settings.password' @keyup='submit' /></el-form-item>
      <el-text>&nbsp;- 设置你的密码。留空时将不进行校验。</el-text><el-divider />
      <el-form-item label='背景图'><el-input v-model='settings.background' type='url' @keyup='submit' /></el-form-item>
      <el-text>&nbsp;- 设置背景图链接。留空则为纯色背景。</el-text>
    </el-form>
  </el-card>
</template>

<style scoped>

</style>
