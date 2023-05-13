<script setup lang='ts'>
import ProgressBar from '@/components/ProgressBar.vue'
import { ref } from 'vue'

const percent = ref(12);
setInterval(() => percent.value = Math.round(Math.random() * 100), 500)
</script>

<template>
  <ProgressBar :percent='percent' />
</template>

<style scoped>

</style>
