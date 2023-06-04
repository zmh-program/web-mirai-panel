<script setup lang='ts'>
import axios from 'axios'
import { ref } from 'vue'
import { isAuthenticated, settings } from '@/assets/script/config'
import { authenticated, message } from '@/assets/script/utils'
import Lock from '@/components/icons/Lock.vue'
import router from '@/router'


const password = ref(settings.password);

async function validate() {
  const auth: boolean = await authenticated(password.value);
  if (!auth) {
    return message({
      type: 'error',
      message: `授权出错！请输入密码！`,
    });
  }
  message({
    type: 'success',
    message: `授权成功！`,
  });

  settings.password = password.value;
  localStorage.setItem('auth', password.value);

  const data = (await axios.get("/api/setting", { headers: { auth: password.value } })).data.data;
  for (let key in data) settings[key] = data[key];

  isAuthenticated.value = true;
  await router.push("/");
}
</script>

<template>
  <el-card class='card'>
    <el-form label-position='top'>
      <div class='header'>
        <img src='/favicon.ico' alt=''>
        <h1>ChatGPT for QQ</h1>
      </div>
      <p class='text'>登录</p>
      <el-form-item class='input-box'>
        <el-input v-model='password' type='password' placeholder='请输入密码' show-password :prefix-icon='Lock' />
      </el-form-item>
      <el-form-item class='button'>
        <el-button class='login' type='primary' @click='validate'>登录</el-button>
      </el-form-item>
    </el-form>
  </el-card>
</template>

<style scoped>
@import "@/assets/style/main.css";

.card {
  height: 480px;
  background: rgba(255,255,255,.8);
  backdrop-filter: blur(1px);
  max-width: 640px;
  margin: 40px auto;
}
.header {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 80px 0 60px;
  user-select: none;
  flex-direction: row;
  gap: 12px;
}

.header img {
  width: 64px;
  height: 64px;
}

.header h1 {
  font-size: 32px;
  font-weight: 600;
  margin-bottom: 0;
  font-family: "Open Sans", sans-serif;
}

.text {
  font-size: 22px;
  font-family: "Open Sans", sans-serif;
  text-align: center;
  transform: translateY(-56px);
}

.input-box {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  margin-top: 50px;
  width: 300px;
}

.button {
  margin-top: 130px;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
}

.login {
  width: 300px;
  transition: .25s;
}
</style>
