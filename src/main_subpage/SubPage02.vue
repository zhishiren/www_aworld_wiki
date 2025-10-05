<template>
  <div>
      <el-row class="firstrow">
        <Opline
            variant="none"
            expand-text="你关注的知识元素在7天内的动态"
            @expand="handleExpand"
            @refresh-list="fetchList"
        />
      </el-row>
      <OpListRow 
          :showprops="'新闻动态-内容动态'"
          ref="opListRowRef"
          :show-list="!showList"
      ></OpListRow>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Opline from '@/components/Opline.vue'
import OpListRow from '@/components/OpListRow.vue'



const showList = ref(true)
const opListRowRef = ref(null)

const fetchList = () => {
  if (opListRowRef.value) {
    opListRowRef.value.fetchList()
  }
}

const handleExpand = () => {
  if (showList.value) {
    showList.value = false
  }
  fetchList()
}
</script>

<style scoped>
.firstrow {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 0;
  flex-wrap: wrap;
}
</style>
