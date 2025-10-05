<template>
  <div>
    <div
      ref="contentRef"
      class="pinglunlan"
      contenteditable="true"
      @input="handleInput"
      @blur="handleBlur"
      @focus="handleFocus"
      @paste="handlePaste"
    ></div>

    <span>
      <el-button
        key="bold"
        type="info"
        text
        @click="applyBold"
        style="font-size: 20px;"
      >
        <b>所选加粗</b>
      </el-button>
      <el-button
        key="unbold"
        type="info"
        text
        @click="removeBold"
        style="float:right; font-size: 20px;"
      >
        <b>取消加粗</b>
      </el-button>
    </span>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue';
import { ElButton } from 'element-plus';

const props = defineProps({
  modelValue: String,
  placeholderText: {
    type: String,
    default: '请输入发言或附言，限100字。'
  }
});

const contentRef = ref(null);
const emit = defineEmits(['update:modelValue', 'blur', 'focus']);
const innerValue = ref(props.modelValue || '');

watch(() => props.modelValue, (newVal) => {
  if (newVal !== innerValue.value) {
    innerValue.value = newVal;
    updateContent();
  }
});

onMounted(() => {
  updateContent();
  contentRef.value.addEventListener('focus', () => {
    if (contentRef.value.innerHTML === props.placeholderText) {
      contentRef.value.innerHTML = '';
    }
  });
});

const updateContent = () => {
  if (contentRef.value) {
    contentRef.value.innerHTML = innerValue.value || props.placeholderText;
  }
};

const handleInput = (event) => {
  innerValue.value = event.target.innerHTML;
  emit('update:modelValue', checkAndReplaceDefaultText(innerValue.value));
};

const handleBlur = () => {
  emit('blur', checkAndReplaceDefaultText(innerValue.value));
};

const handleFocus = () => {
  emit('focus', innerValue.value);
};

const handlePaste = (event) => {
  event.preventDefault();
  let text = (event.clipboardData || window.clipboardData).getData('text');
  text = text.replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim();
  document.execCommand('insertText', false, text);
};

const applyBold = () => {
  document.execCommand('bold', false, null);
};

const removeBold = () => {
  let innerHTML = contentRef.value.innerHTML;
  innerHTML = innerHTML.replace(/<b>|<\/b>|<strong>|<\/strong>/g, '');
  contentRef.value.innerHTML = innerHTML;
  innerValue.value = innerHTML;
  emit('update:modelValue', innerValue.value);
};

const checkAndReplaceDefaultText = (value) => {
  return value === props.placeholderText ? '无' : value;
};
</script>

<style scoped>
.pinglunlan {
  width: 100%;
  border: none;
  border-radius: 0;
  border-bottom: black 1px solid;
  box-shadow: 0;
  outline: none;
  text-decoration: none;
  font-size: 20px;
  min-height: 30px;
  padding: 5px 0;
  color: brown;
  font-weight: lighter;
  direction: ltr;
  text-align: left;
  white-space: pre-wrap;
}
</style>