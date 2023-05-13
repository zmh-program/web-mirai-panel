<template>
  <el-card class='card'>
  <el-result icon="error" title="404" sub-title="Not Found" class='result'>
    <template #extra>
      <router-link to='/'><el-button type="primary">Back</el-button></router-link>
    </template>
  </el-result>
  </el-card>
</template>
<style>
@import "@/assets/style/main.css";
.result {
    min-height: 80dvh;
}
</style>
