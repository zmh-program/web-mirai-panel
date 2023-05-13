<script setup lang='ts'>
import ProgressBar from '@/components/ProgressBar.vue'
import { ref } from 'vue'
import type { Ref } from 'vue'

const percent: Ref<Record<string, number>> = ref({
  cpu: 78,
  ram: 42,
  rom: 12
})

</script>

<template>
  <div class='progress-container'>
    <ProgressBar :percent='percent.cpu'>
      <template v-slot:header><i class="fa fa-solid fa-microchip" /> CPU </template>
      <template v-slot:footer>4 核心</template>
    </ProgressBar>
    <ProgressBar :percent='percent.ram' >
      <template v-slot:header><i class="fa fa-solid fa-memory" /> RAM </template>
      <template v-slot:footer>2.3 / 4G</template>
    </ProgressBar>
    <ProgressBar :percent='percent.rom' >
      <template v-slot:header><i class="fa fa-solid fa-hard-drive" /> ROM </template>
      <template v-slot:footer>12 / 40G</template>
    </ProgressBar>
    <el-card>
      <header><h3><i class="fa fa-solid fa-circle-info" /> 其他信息</h3></header>
      <table class='info'>
        <tr><td>主机名</td><td></td></tr>
        <tr><td>系统</td><td></td></tr>
        <tr><td>版本</td><td></td></tr>
      </table>
    </el-card>
  </div>
</template>

<style scoped>
.fa,
.fa::before {
    font-weight: inherit;
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
}

.info {
    font-family: Poppins, sans-serif;
}
</style>
