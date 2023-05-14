<script setup lang='ts'>
import { ref } from 'vue'
import { message } from '@/assets/script/utils'
import type { UploadUserFile } from 'element-plus'

const files = ref<UploadUserFile[]>([]);
const notification = function() {
  message({
    type: 'error',
    message: `上传时出错！`,
  });
}
</script>

<template>
  <el-card class='card'>
    <h1>📂 上传文件</h1><el-divider />
    <el-upload drag action="/api/upload" multiple v-model:file-list='files' :on-error='notification' method='POST'>
      <img src='../assets/icons/upload.svg' alt='Upload' width='64' height='64'>
      <div class="el-upload__text">
        拖拽文件到此处 或者 <em>点击这里上传</em>
      </div>
    </el-upload>
  </el-card>
</template>
<style>
@import "@/assets/style/main.css";
</style>
