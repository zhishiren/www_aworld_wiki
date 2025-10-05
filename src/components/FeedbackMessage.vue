<template>
    <transition name="fade">
      <p v-if="visible" :class="['feedback-message', { 'blink': isBlinking }]">
        ---{{ message }}---
      </p>
    </transition>
  </template>
  
  <script setup>
  import { ref, watch } from 'vue';
  
  const props = defineProps({
    message: {
      type: String,
      required: true
    },
    show: {
      type: Boolean,
      default: false
    }
  });
  
  const visible = ref(false);
  const isBlinking = ref(false);
  
  watch(() => props.show, (newValue) => {
    if (newValue) {
      visible.value = true;
      isBlinking.value = true;
      setTimeout(() => {
        isBlinking.value = false;
      }, 3000);
    } else {
      visible.value = false;
    }
  });
  </script>
  
  <style scoped>
  .feedback-message {
    color: red;
    margin-top: 10px;
    font-size: 18px;
    text-align: center;
  }
  
  .blink {
    animation: blink-animation 1.5s linear infinite;
  }
  
  @keyframes blink-animation {
    50% {
      opacity: 0;
    }
  }
  
  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.5s ease;
  }
  
  .fade-enter-from,
  .fade-leave-to {
    opacity: 0;
  }
  </style>