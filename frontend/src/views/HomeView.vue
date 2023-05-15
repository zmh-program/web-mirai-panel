<script setup lang='ts'>
import ProgressBar from '@/components/ProgressBar.vue'
import { ref } from 'vue'
import type { Ref } from 'vue'
import axios from 'axios'
import { message } from '@/assets/script/utils'
import { socket } from '@/assets/script/socket'

const container: Ref<{status: string, name: string, color: string}[]> = ref([]);

const status = ref({
  cpu: 0,
  memory: 0,
  memory_percent: 0,
  disk: 0,
  disk_percent: 0,
  recv: 0,
  sent: 0,
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
  const { cpu, memory, disk, recv, sent, containers } = data;
  const memory_percent = (memory / info.value.memory) * 100, disk_percent = (disk / info.value.disk) * 100;
  status.value = {
    cpu, recv, sent,
    memory, memory_percent,
    disk, disk_percent,
  };
  container.value = containers;
});
setInterval(() => socket.emit("status_input"), 1000);
</script>

<template>
  <el-card class='card'>
    <h1>🧨 监控</h1>
    <el-divider style='padding: 30px 0; transform: translateY(20px)' />
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
      <el-card class='info'>
        <header><h3><i class="fa-brands fa-docker"></i> 容器状态</h3></header>
        <table>
          <template v-if='container.length'>
            <tr v-for='(obj, idx) in container' :key='idx'>
              <td class='status'>
                <div class='circle' :style='{ "background": obj.color }' />
                <span :style='{ "color": obj.color }' >{{ obj.status }}</span>
              </td>
              <td style='text-align: inherit'>{{ obj.name }}</td>
            </tr>
          </template>
          <tr v-else><td style='padding: 20px'>暂无</td></tr>
        </table>
      </el-card>
    </div>
  </el-card>
</template>

<style scoped>
@import "@/assets/style/main.css";
.fa,
.fa::before {
    font-weight: inherit;
}
@media (max-width: 600px) {
    .info {
        width: 100%;
    }
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

.status {
    display: flex;
    flex-direction: row;
    text-align: inherit;
}
.status .circle {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    top: 50%;
    transform: translateY(-50%);
    position: absolute;
}

.status span {
    margin-left: 16px;
}
</style>
