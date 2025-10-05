<!-- 这个组件在手机端首页中下端的欢迎提示 -->
<template>
    <div class="command-line-container">
      <span class="command-line-text"></span>
      <span class="cursor">Ⓐ</span>
    </div>
  </template>
  
  <script setup>
  import { onMounted, ref } from 'vue';
  
  const props = defineProps({
    text: {
      type: String,
      required: true
    }
  });
  
  const element = ref(null);
  
  onMounted(() => {
    element.value = document.querySelector('.command-line-text');
    let index = 0;
  
    function typeText() {
      if (index < props.text.length) {
        element.value.textContent += props.text.charAt(index);
        index++;
        setTimeout(typeText, 100); // 控制打字速度
      }
    }
  
    typeText();
  });
  </script>
  
  <style scoped>
  .command-line-container {
    position: fixed;
    bottom: 20px;
    left: 0;
    width: 100%;
    padding: 10px;
    box-sizing: border-box;
    font-family: 'Courier New', Courier, monospace;
    
  }
  
  .command-line-text {
    font-size: 25px;
  }
  
  .cursor {
    display: inline-block;
    width: 10px;
    height: 30px;
    line-height: 30px;
    font-weight: bolder;
    font-size: 25px;
    animation: blink 0.7s infinite;
    vertical-align: middle;
    margin-left: 2px;
    margin-bottom: 2px;
    font-weight: bolder;
  }
  
  @keyframes blink {
    0% { opacity: 0; }
    50% { opacity: 1; }
    100% { opacity: 0; }
  }
  </style>
