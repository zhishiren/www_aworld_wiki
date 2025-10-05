<template>
  <div class="subpage3x">
    <el-row class="firstrow">
      <Opline
        variant="none"
        :expand-text="`你共关注了${displayList.length} 个${props.itemType || '全部'}`"
        @expand="handleExpand"
        @refresh-list="fetchList"
      />
    </el-row>
    <el-alert
      v-if="errorMessage"
      :title="errorMessage"
      type="error"
      show-icon
      class="query-alert"
    />

    <div v-if="showList && paginatedList.length" class="op-list">
      <div
        v-for="item in paginatedList"
        :key="item.op_id"
        class="op-item"
      >
        <el-row class="op-title">{{ item.item0title || '未命名' }}</el-row>
        <el-row class="op-meta">
          <span>类型：{{ item.item0type || item.item_type || '未知类型' }}</span>
          <el-divider direction="vertical" />
          <span>关注附言：{{ item.ps_content || '无附言' }}</span>
        </el-row>
      </div>
    </div>

    <el-empty v-else-if="showList && hasFetched && !loading" description="暂无符合条件的记录" />

    <el-pagination
      v-if="showList && displayList.length > pageSize"
      background
      v-model:current-page="currentPage"
      :page-size="pageSize"
      layout="sizes, prev, pager, next, jumper"
      :total="displayList.length"
      class="pagination"
      @current-change="handlePageChange"
      @size-change="handlePageSizeChange"
    />
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import axios from 'axios';
import { ElMessage } from 'element-plus';
import Opline from '@/components/Opline.vue';

const props = defineProps({
  itemType: {
    type: String,
    default: ''
  }
});

const loading = ref(false);
const errorMessage = ref('');
const hasFetched = ref(false);
const oplist = ref([]);
const currentPage = ref(1);
const pageSize = ref(10);
const showList = ref(false);

const displayList = computed(() => {
  if (!props.itemType) {
    return oplist.value;
  }
  return oplist.value.filter((item) => item?.item0type === props.itemType);
});

const paginatedList = computed(() => {
  const start = (currentPage.value - 1) * pageSize.value;
  const end = start + pageSize.value;
  return displayList.value.slice(start, end);
});

const fetchList = async () => {
  if (loading.value) return;
  loading.value = true;
  errorMessage.value = '';

  try {
    const response = await axios.post('https://www.aworld.wiki/api/opinfo/get_oplist/', {
      op_type: 'm关注收藏',
      user_id: localStorage.getItem('userid') || ''
    });

    const payload = Array.isArray(response.data) ? response.data : (response.data?.data || []);
    oplist.value = Array.isArray(payload) ? payload : [];
    currentPage.value = 1;

    if (!oplist.value.length) {
      ElMessage.warning('没有匹配的操作记录');
    }
  } catch (error) {
    const message = error?.response?.data?.message || error?.response?.data?.error || '查询失败，请稍后重试';
    errorMessage.value = message;
    ElMessage.error(message);
  } finally {
    loading.value = false;
    hasFetched.value = true;
  }
};

const handleExpand = () => {
  if (!showList.value) {
    showList.value = true;
  }
  if (!hasFetched.value) {
    fetchList();
  }
};

const handlePageChange = (page) => {
  currentPage.value = page;
};

const handlePageSizeChange = (size) => {
  if (size === pageSize.value) return;
  pageSize.value = size;
  currentPage.value = 1;
};

watch(() => props.itemType, () => {
  currentPage.value = 1;
});

watch(() => displayList.value.length, (length) => {
  const maxPage = Math.max(1, Math.ceil(length / pageSize.value));
  if (currentPage.value > maxPage) {
    currentPage.value = maxPage;
  }
});
</script>

<style scoped>
.subpage3x {
  width: 100%;
  overflow-x: hidden;
  box-sizing: border-box;
  text-align: left;
}

.firstrow {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 0;
  flex-wrap: wrap;
}

.query-alert {
  flex: 1;
  max-width: 360px;
}

.op-item {
  /* padding: 12px 16px; */
  border-bottom: 1px solid #e0e4ef;
  border-radius: 8px;
  background: #fff;
}

.op-title {
  font-weight: 400;
  font-size: 18px;
  margin-bottom: 2px;
  margin-top: 5px;
  color: #1f2d3d;
}

.op-meta {
  font-size: 18px;
  color: #4b5668;
  align-items: center;
}

.pagination {
  margin-top: 16px;
  text-align: right;
}
</style>
