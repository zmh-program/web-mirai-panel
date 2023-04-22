<script setup lang="ts">
import { ref } from 'vue'
import type { Ref } from 'vue'

const collapse: Ref<string[]> = ref(['chat']);
const chatModel: Ref<string> = ref('cqhttp');
</script>

<template>
  <main>
    <el-card class='card'>
      <el-collapse v-model='collapse'>
        <el-collapse-item name='chat' title='聊天平台'>
          <el-radio-group v-model='chatModel'>
            <el-radio label='cqhttp'>OneBot (CQHttp)</el-radio>
            <el-radio label='mirai'>Mirai</el-radio>
            <el-radio label='telegram'>Telegram</el-radio>
            <el-radio label='discord'>Discord</el-radio>
          </el-radio-group>
          <div>
            
          </div>
        </el-collapse-item>
      </el-collapse>
    </el-card>
  </main>
</template>

<style scoped>
.card {
    width: 100%;
    min-width: 280px;
    height: max-content;
    min-height: 120px;
}
</style>