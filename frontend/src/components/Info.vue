<script setup lang='ts'>
import ProgressBar from '@/components/ProgressBar.vue'
import { ref } from 'vue'
import axios from 'axios'
import { message } from '@/assets/script/utils'
import { socket } from '@/assets/script/socket'

const status = ref({
  cpu: 0,
  memory: 0,
  memory_percent: 0,
  disk: 0,
  disk_percent: 0,
  recv: "",
  sent: ""
})

const info = ref({
  cpu_count: 0,
  disk: 0,
  memory: 0,
  host: "未知",
  system: "未知",
  device: "暂无",
  qq: "未知",
  nickname: "未知",
})

axios.get('/api/info')
.then(res => {
  info.value = res.data;
})
.catch(() => {
  message({
    type: 'error',
    message: `系统信息请求失败！`,
  });
})

socket.on("status_output", (data: Record<string, any>) => {
  const { cpu, memory, disk, recv, sent } = data;
  const memory_percent = (memory / info.value.memory) * 100, disk_percent = (disk / info.value.disk) * 100;
  status.value = {
    cpu, recv, sent,
    memory, memory_percent,
    disk, disk_percent,
  }
});
setInterval(() => socket.emit("status_input"), 500);
</script>

<template>
  <div class='progress-container'>
    <ProgressBar :percent='status.cpu'>
      <template v-slot:header><i class="fa fa-solid fa-microchip" /> CPU </template>
      <template v-slot:footer>{{ info.cpu_count }} 核心</template>
    </ProgressBar>
    <ProgressBar :percent='status.memory_percent' >
      <template v-slot:header><i class="fa fa-solid fa-memory" /> RAM </template>
      <template v-slot:footer>{{ status.memory }} / {{ info.memory }}G</template>
    </ProgressBar>
    <ProgressBar :percent='status.disk_percent' >
      <template v-slot:header><i class="fa fa-solid fa-hard-drive" /> ROM </template>
      <template v-slot:footer>{{ status.disk }} / {{ info.disk }}G</template>
    </ProgressBar>
    <el-card class='info'>
      <header><h3><i class="fa fa-solid fa-circle-info" /> 其他信息</h3></header>
      <table>
        <tr><td>系统</td><td>{{ info.system }}</td></tr>
        <tr><td>主机名</td><td>{{ info.host }}</td></tr>
        <tr><td>上行流量</td><td>{{ status.sent }}G</td></tr>
        <tr><td>下行流量</td><td>{{ status.recv }}G</td></tr>
        <tr><td>CQHttp 设备代号</td><td>{{ info.device }}</td></tr>
        <tr><td>QQ</td><td>{{ info.qq }}</td></tr>
        <tr><td>昵称</td><td>{{ info.nickname }}</td></tr>
      </table>
    </el-card>
  </div>
</template>

<style scoped>
.fa,
.fa::before {
    font-weight: inherit;
}

td {
    padding: 0 4px;
    text-align: center;
}

.progress-container {
    display: flex;
    flex-direction: row;
    gap: 16px;
    flex-wrap: wrap;
}

header h3 {
    font-weight: bold;
    font-family: Poppins, sans-serif;
    text-align: center;
    margin-bottom: 6px;
}

.info {
    font-family: Poppins, sans-serif;
    min-width: 320px;
}

.info table {
    margin: 0 auto;
}
</style>
