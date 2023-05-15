<script setup lang='ts'>
import { socket } from '@/assets/script/socket'
import { ref } from 'vue'
import type { Ref } from 'vue'
import Convert from 'ansi-to-html'

const convert = new Convert();
const buffer: Ref<string[]> = ref([]);
const input: Ref<string> = ref("");
const stamp: Ref<number> = ref((new Date()).getTime());

function absolute(n: number): number {
  return n <= 0 ? 0 : n;
}

function submit() {
  const data: string = input.value;
  if (data) {
    socket.emit("command_input", data);
    receive(`> ${data}`);
    input.value = "";
  }
}

function ignore(ev: FormDataEvent): void {
  return ev.preventDefault();
}

function receive(data: string) {
  const current: number = (new Date()).getTime();
  const delay: number = absolute(100 - (current - stamp.value));
  stamp.value = current;
  setTimeout(() => {
    if (buffer.value.length > 20) buffer.value.shift();
    return buffer.value.push(convert.toHtml(data));
  }, delay);
}

socket.on("command_output", receive);

</script>

<template>
  <el-card class='card'>
    <h1>👩‍💻 终端</h1>
    <el-divider style='padding: 30px 0; transform: translateY(20px)'/>
    <div class='console'>
      <span v-for='(data, idx) in buffer' :key='idx' v-html='data' />
    </div><br>
    <el-form :inline='true' @submit.prevent='ignore'>
      <el-form-item style='width: calc(100% - 72px); margin-right: 12px'><el-input v-model='input' @keyup.enter='submit' /></el-form-item>
      <el-form-item style='width: 60px; margin-right: 0'><el-button type='primary' @click='submit'>发送</el-button></el-form-item>
    </el-form>
  </el-card>
</template>

<style scoped>
@import "@/assets/style/main.css";
@keyframes fadeInAnimation {
    0% { opacity: 0 }
    100% { opacity: 1 }
}

.console {
    display: flex;
    flex-direction: column;
    height: max-content;
    min-height: max(416px, 60vh);
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
