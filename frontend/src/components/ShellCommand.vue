<script setup lang='ts'>
import { socket } from '@/assets/script/socket'
import { ref } from 'vue'
import type { Ref } from 'vue'

const buffer: Ref<string[]> = ref([]);
const input: Ref<string> = ref("");

function submit() {
  const data: string = input.value;
  if (data) socket.emit("command_input", data);
}

socket.on("command_output", function(data: string) {
  return buffer.value.push(data);
})

</script>

<template>
  <div class='console'>
    <div v-for='(data, idx) in buffer' :key='idx'>{{ data }}</div>
  </div><br>
  <el-form :inline='true'>
    <el-form-item style='width: calc(100% - 72px); margin-right: 12px'><el-input v-model='input' /></el-form-item>
    <el-form-item style='width: 60px; margin-right: 0'><el-button type='primary' @click='submit'>发送</el-button></el-form-item>
  </el-form>
</template>

<style scoped>
.console {
    height: max-content;
    min-height: 240px;
    width: 100%;
    color: #fff;
    background: #181818;
    padding: 12px;
    line-height: 20px;
}
</style>
