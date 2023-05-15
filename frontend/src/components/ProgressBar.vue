<script setup lang='ts'>
import { ref, watch } from 'vue'

const props = defineProps<{
  percent: number,
}>();

const colors: { level: number, color: string }[] = [
  { level: 80, color: "rgb(240, 40, 40)" },
  { level: 60, color: "rgb(240,100,40)" },
  { level: 40, color: "rgb(247,223,30)" },
  { level: 20, color: "rgb(58,178,18)" },
  { level: 0, color: "rgb(100,100,100)" },
];

function getColor(percent: number): string {
  for (const key of colors) {
    const { level, color } = key;
    if (percent >= level) return color;
  }
  return "rgb(100,100,100)";
}

let style = ref({});
const refresh = () => {
  style.value = {
    stroke: getColor(props.percent),
    strokeDashoffset: `calc(440px - (440px * ${props.percent} / 100))`,
  }
};
watch(props, refresh);
refresh();
</script>

<template>
  <el-card class='progress-card'>
    <header><h3><slot name='header' /></h3></header>
    <div class="percent">
      <svg>
        <circle class="percent-chart" stroke="transparent" cx="70" cy="70" r="70" shape-rendering="geometricPrecision" :style='style'></circle>
      </svg>
      <div class='text'>
        <h2><span class="percent-value">{{ props.percent.toFixed() }}</span>%</h2>
        <footer><h3><slot name='footer' /></h3></footer>
      </div>
    </div>
  </el-card>
</template>

<style scoped>
.progress-card {
    width: max-content;
    padding: 4px;
}
@media (max-width: 600px) {
    .progress-card {
        width: 100%;
    }
}
header h3 {
    font-weight: bold;
    font-family: Poppins, sans-serif;
    text-align: center;
}
.percent {
    position: relative;
    left: 50%;
    transform: translateX(-50%);
    width: 150px;
    height: 150px;
    border-radius: 50%;
    margin-bottom: 20px;
    margin-top: 6px;
}
.percent footer h3 {
    top: -12px;
    font-family: Poppins, sans-serif;
}
.percent .text {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}
.percent .text h2 {
    color: #1f1c2e;
    font-weight: 700;
    font-family: Poppins, sans-serif;
}
.percent .text h2 span.percent-value {
    font-size: 50px;
}
.percent .text h2 span {
    font-size: 25px;
}
.percent svg {
    position: relative;
    width: 150px;
    height: 150px;
    rotate: 270deg;
    transform-origin: center;
}
.percent svg circle {
    width: 100%;
    height: 100%;
    fill: none;
    stroke-width: 10;
    stroke: rgba(255,255,255,0.05);
    transform: translate(5px,5px);
    stroke-linecap: round;
    stroke-dasharray: 440px;
    stroke: rgb(247,223,30);
    stroke-dashoffset: calc(440px - (440px * 65 / 100));
    transition: stroke-dashoffset 1s, stroke-dasharray 1s, stroke 1s;
}
</style>
