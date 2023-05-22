<script setup lang='ts'>
import { settings } from '@/assets/script/config'
import { reactive } from 'vue'
import axios from 'axios'
import { message } from '@/assets/script/utils'

const form = reactive({
  ...settings,
})

let timeout = 0;
function submit() {
  clearTimeout(timeout);
  timeout = setTimeout(() => {
    axios.post('api/setting', form)
      .then(() => {
        message({
          type: 'success',
          message: `保存成功！`,
        })
      })
    //@ts-ignore
    for (const k in form) settings[k] = form[k];
    localStorage.setItem('auth', form.password);
  }, 500);
}
</script>

<template>
  <el-card class='card'>
    <h1>🔧 设置</h1>
    <el-divider style='padding: 10px 0'/>
    <el-form class='form' :model='form'>
      <el-form-item label='密码'><el-input v-model='form.password' @keyup='submit' type='password' /></el-form-item>
      <el-text>&nbsp;- 设置你的密码。留空时将不进行校验。</el-text><el-divider border-style='dashed' />
      <el-form-item label='背景图'><el-input v-model='form.background' type='url' @keyup='submit' /></el-form-item>
      <el-text>&nbsp;- 设置背景图链接。留空则为纯色背景。</el-text>
    </el-form>
  </el-card>
</template>

<style scoped>

</style>
