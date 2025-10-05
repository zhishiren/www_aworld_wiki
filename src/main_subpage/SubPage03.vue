<template>
  <div>
    <el-row class="firstrow">
      <Opline
        variant="none"
        expand-text="根据爱好和热度，为你推送10条段落"
        :expand-loading="loading"
        @expand="handleExpand"
        @refresh-list="loadRS"
      />
    </el-row>
    <Itemlist 
      v-if="!showList" 
      :itemlistData="itemlistData"
      ref="itemlistRef"
    ></Itemlist>
  </div>
</template>

<script>
import Itemlist from '@/components/Itemlist.vue';
import { ref } from 'vue';
import axios from 'axios';
import { ElMessage } from 'element-plus';
import { ElLoading } from 'element-plus';
import Opline from '@/components/Opline.vue';

export default {
  name: 'SubPage03',
  components: {
    Itemlist,
    Opline
  },
  setup() {
    const itemlistData = ref([]);
    const loading = ref(false);
    const showList = ref(true);
    const itemlistRef = ref(null);
    let loadingInstance = null;

    const showLoading = () => {
      loadingInstance = ElLoading.service({
        lock: true,
        text: '加载中...',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)',
        customClass: 'custom-loading-text',
      });
    };

    const hideLoading = () => {
      loadingInstance?.close();
    };

    const loadRS = async () => {
      loading.value = true;
      showLoading();
      try {
        const response = await axios.post('https://www.aworld.wiki/api/iteminfo/show_itemlist/', {
          item_type: 'm推荐阅读',
        });
        itemlistData.value = response.data;
      } catch (e) {
        console.error('加载列表失败:', e);
        ElMessage.error('加载失败');
      } finally {
        loading.value = false;
        hideLoading();
      }
    };

    const handleExpand = async () => {
      if (showList.value) {
        showList.value = false;
      }
      await loadRS();
    };

    return {
      itemlistData,
      loadRS,
      showList,
      handleExpand,
      loading,
      itemlistRef
    };
  }
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

.custom-loading-text .el-loading-mask .el-loading-text {
  font-size: 24px !important;
}
</style>
  
  
  
