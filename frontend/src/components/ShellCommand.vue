<script setup lang='ts'>
import { socket } from '@/assets/script/socket'
import { ref } from 'vue'
import type { Ref } from 'vue'

const buffer: Ref<string[]> = ref([]);
const input: Ref<string> = ref("");


function listener(ev: KeyboardEvent): void {
  if (ev.key === "Enter") submit();
}
function submit() {
  const data: string = input.value;
  if (data) socket.emit("command_input", data);
  input.value = "";
}

socket.on("command_output", function(data: string) {
  if (buffer.value.length > 25) buffer.value.shift();
  return buffer.value.push(data);
})

</script>

<template>
  <div class='console'>
    <span v-for='(data, idx) in buffer' :key='idx'>{{ data }}</span>
  </div><br>
  <el-form :inline='true'>
    <el-form-item style='width: calc(100% - 72px); margin-right: 12px'><el-input v-model='input' /></el-form-item>
    <el-form-item style='width: 60px; margin-right: 0'><el-button type='primary' @click='submit' @keyup='listener'>发送</el-button></el-form-item>
  </el-form>
</template>

<style scoped>
@keyframes fadeInAnimation {
    0% { opacity: 0 }
    100% { opacity: 1 }
}

.console {
    height: max-content;
    min-height: 240px;
    width: 100%;
    color: #fff;
    background: #181818;
    padding: 16px;
    font-size: 12px;
    font-family: 'Open Sans', sans-serif;
    letter-spacing: 0.01cm;
}

.console span {
    animation: fadeInAnimation .5s;
}
</style>
