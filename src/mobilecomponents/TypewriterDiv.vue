<template>
    <div style="width: 100%; text-align: left; white-space: pre-wrap;font-size: 20px;" @click="handleExpand">
      <span>{{ currentText }}</span>
      <span v-if="isComplete" :class="{ blink: isComplete }">_展开_</span>
    </div>
</template>

<script>
import { defineComponent, ref, computed, onMounted, watch, onBeforeUnmount } from 'vue';
import { ElLoading } from 'element-plus'; // 引入 Element Plus 的 Loading 组件

export default defineComponent({
    name: 'TypewriterDiv',
    props: {
      text: {
        type: String,
        required: true
      }
    },
    setup(props) {
      const fullText = ref(props.text);
      const currentIndex = ref(0);
      const isComplete = ref(false);
      const loadingInstance = ref(null); // 添加加载实例

      const currentText = computed(() => {
        let text = fullText.value.substring(0, currentIndex.value);
        text = text.replace('{currentTime}', new Date().toLocaleTimeString());
        return text;
      });

      const typewriterEffect = () => {
        if (currentIndex.value < fullText.value.length) {
          currentIndex.value++;
          setTimeout(typewriterEffect, 100);
        } else {
          isComplete.value = true;
        }
      };

      watch(() => props.text, (newText) => {
        fullText.value = newText;
        currentIndex.value = 0;
        isComplete.value = false;
        typewriterEffect();
      });

      onMounted(() => {
        typewriterEffect();
      });

      const handleExpand = () => {
        loadingInstance.value = ElLoading.service({ // 开始加载
          lock: true,
          text: '加载中...', // 增大字体
          spinner: 'el-icon-loading',
          background: 'rgba(0, 0, 0, 0.7)',
          customClass: 'custom-loading-text',
        });
      };

      // 在组件卸载时关闭加载实例
      onBeforeUnmount(() => {
        if (loadingInstance.value) {
          loadingInstance.value.close(); // 关闭加载
        }
      });

      return {
        currentText,
        isComplete,
        handleExpand, // 返回处理函数
      };
    },
});
</script>

<style scoped>
.blink {
  animation: blink-animation 1s steps(5, start) infinite;
}

@keyframes blink-animation {
  to {
    visibility: hidden;
  }
}
</style>
