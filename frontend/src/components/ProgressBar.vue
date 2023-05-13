<script setup lang='ts'>

</script>

<template>
  <div class="percent">
    <svg>
      <circle class="percent-chart" stroke="transparent" cx="70" cy="70" r="70" shape-rendering="geometricPrecision" style="stroke: rgb(240, 40, 40); stroke-dashoffset: calc(57px);"></circle>
    </svg>
    <div class="number">
      <h2>
        <span class="percent-value">87</span>
        <span>%</span>
      </h2>
    </div>
  </div>
</template>

<style scoped>
.percent {
    position: relative;
    left: 50%;
    transform: translateX(-50%);
    width: 150px;
    height: 150px;
    border-radius: 50%;
    margin-bottom: 20px;
}
.percent .number {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.percent .number h2 {
    color: #1f1c2e;
    font-weight: 700;
    font-family: Poppins, sans-serif;
}
.percent .number h2 span.percent-value {
    font-size: 50px;
}
.percent .number h2 span {
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
