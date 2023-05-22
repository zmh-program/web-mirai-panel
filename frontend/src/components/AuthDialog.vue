<script setup lang='ts'>
import axios from 'axios'
import { ref } from 'vue'
import { settings } from '@/assets/script/config'
import { message } from '@/assets/script/utils'

const visible = ref(false);
const password = ref(settings.password);
function validate(notify=true) {
  axios.get("api/auth", {headers: { auth: password.value }}).then(res => {
    const auth = ! res.data.status;
    visible.value = auth;
    if (auth) {
      if (notify) message({
        type: 'error',
        message: `授权出错！请输入密码！`,
      });
    } else {
      message({
        type: 'success',
        message: `授权成功！`,
      });
      settings.password = password.value;
      localStorage.setItem('auth', password.value);
    }
  })
}

validate(false);
</script>

<template>
  <el-dialog title="授权" v-model='visible'>
    <el-form>
      <el-form-item label="密码">
        <el-input v-model='password' type='password' placeholder='请输入密码' required />
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button type="primary" @click='validate'>校验</el-button>
      </span>
    </template>
  </el-dialog>
</template>

<style scoped>

</style>
