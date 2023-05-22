<script setup lang='ts'>
import { reactive } from 'vue'

const form = reactive({
  password: "",
  background: ""
})

function submit() {

}
</script>

<template>
  <el-card class='card'>
    <h1>🔧 设置</h1>
    <el-divider style='padding: 30px 0; transform: translateY(20px)'/>
    <el-form class='form' :model='form'>
      <el-form-item label='密码'><el-input v-model='form.password' @keyup='submit' /></el-form-item>
      <el-text>
        &nbsp;- 设置你的密码。留空时将不进行校验。
      </el-text>
    </el-form>
  </el-card>
</template>

<style scoped>

</style>
