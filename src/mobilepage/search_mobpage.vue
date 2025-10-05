<template>
  <div class="mobile-page">
    <Topbar topbartitle="全站搜索"></Topbar>
    
    <!-- 搜索结果 -->
    <el-scrollbar v-if="searchResults.length > 0">
      <div v-for="(item, index) in searchResults" :key="index">
        <router-link class="a_black" 
          :to="{ name: 'detail_mobpage', params: { id: item.item_id, subpagetype: '搜索-详情' } }">

          <el-row style="text-align: left;font-size: 20px;">
            <span  v-if="item.item_type === '段落'" >{{ item.sparefield1 }}</span>
            <strong>{{ item.item_title }}</strong>
          </el-row>

          <el-row style="text-align: left;font-size: 18px;color:gray">
            <span style="color: darkblue;">{{ item.item_type }}</span>｜{{ formatTime(item.time_create) }}
          </el-row>
          <el-row style="text-align: left;font-size: 18px;color: gray;border-bottom: 1px solid lightgray;">
            <span v-html="highlightKeyword(item.item_content)"></span>
          </el-row>
        </router-link>
      </div>
      <div style="height: 200px;"></div>
    </el-scrollbar>

    <!-- 热门搜索和历史���索 -->
    <el-scrollbar v-else>
      <div style="font-size: 24px;text-align: left;font-weight: bold;">大家热门搜词:</div>
      <div style="font-size: 24px;text-align: left;">
        <div v-for="(item, index) in hotSearches" :key="index">
          {{ item.keyword }}｜<span style="color: gray;">{{ item.desc }}</span>
        </div>
      </div>
      <br>
      <div style="font-size: 24px;text-align: left;font-weight: bold;">我的历史搜词:</div>
      <div style="font-size: 24px;text-align: left;">
        <div v-for="(item, index) in searchHistory" :key="index">
          {{ item }}｜<span style="color: gray;">{{ getSearchCount(item) }}次</span>
        </div>
      </div>
      <div style="height: 200px;"></div>
    </el-scrollbar>

    <mob_opbar 
      fromwhere="m搜索页面"
      @submit="handleSubmit"
      @reset="handleReset"
      v-model:keyword="searchKeyword"
      :current_number="currentPage"
      :total_number="totalResults"
      @prev10="handlePrev10"
      @next10="handleNext10"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Topbar from '../mobilecomponents/Topbar.vue';
import mob_opbar from '../mobilecomponents/mob_opbar.vue';
import axios from 'axios';
import { ElMessage, ElLoading } from 'element-plus';

const searchKeyword = ref('');
const searchResults = ref([]);
const allResults = ref([]);
const searchHistory = ref([]);
const currentPage = ref(1);
const totalResults = ref(0);
const itemsPerPage = 10;
const hotSearches = ref([
  { keyword: '西澳公社', desc: '内容匹配100%' },
  { keyword: '民兵手册', desc: '内容匹配90%' },
  { keyword: '互助保险', desc: '用户匹配80%' },
  { keyword: '马德里公社', desc: '用户匹配70%' },
  { keyword: '巴黎公社', desc: '最热门50%' },
  { keyword: '敖德萨公社', desc: '最热门40%' },
  { keyword: '福岛公社', desc: '最近流行30%' },
  { keyword: '乔姆斯基', desc: '最近流行20%' },
  { keyword: '格雷伯', desc: '随机推荐' },
  { keyword: '司各特', desc: '随机推荐' }
]);
const loadingInstance = ref(null);

// 添加 handleExpand 函数
const handleExpand = () => {
  loadingInstance.value = ElLoading.service({
    lock: true,
    text: '加载中...',
    spinner: 'el-icon-loading',
    background: 'rgba(0, 0, 0, 0.7)',
    customClass: 'custom-loading-text',
  });
};

// 修改 handleSubmit 函数，添加加载动画
const handleSubmit = async (keyword) => {
  if (!keyword) {
    ElMessage.warning('请输入搜索关键词');
    return;
  }

  handleExpand();  // 显示加载动画
  try {
    const response = await axios.post('https://www.aworld.wiki/api/iteminfo/search_items/', {
      keyword: keyword
    });
    
    if (response.data.items) {
      allResults.value = response.data.items;
      totalResults.value = response.data.items.length;
      updateDisplayResults();
      ElMessage.success(response.data.message);
      saveSearchHistory(keyword);
    }
  } catch (error) {
    console.error('搜索失败:', error);
    ElMessage.error(error.response?.data?.error || '搜索失败，请稍后重试');
  } finally {
    // 关闭加载动画
    if (loadingInstance.value) {
      loadingInstance.value.close();
    }
  }
};

// 处理上一页
const handlePrev10 = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
    updateDisplayResults();
  }
};

// 处理下一页
const handleNext10 = () => {
  const maxPage = Math.ceil(totalResults.value / itemsPerPage);
  if (currentPage.value < maxPage) {
    currentPage.value++;
    updateDisplayResults();
  }
};

// 更新显示的结果
const updateDisplayResults = () => {
  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  searchResults.value = allResults.value.slice(start, end);
};

// 修改 handleReset 函数
const handleReset = () => {
  searchKeyword.value = '';  // 清空搜索关键词
  searchResults.value = [];  // 清空搜索结果
  allResults.value = [];     // 清空所有结果
  currentPage.value = 1;     // 重置页码
  totalResults.value = 0;    // 重置总数
};

// 高亮关键词并只返回包含关键词的第一行
const highlightKeyword = (content) => {
  if (!content || !searchKeyword.value) return '';
  
  // 将内容按行分割
  const lines = content.split(/\n|。/);
  
  // 查找包含关键词的第一行
  const targetLine = lines.find(line => line.includes(searchKeyword.value)) || content;
  
  // 如果行太长，截取关键词前后的一部分内容
  const keyword = searchKeyword.value;
  const keywordIndex = targetLine.indexOf(keyword);
  const maxLength = 100; // 设置最大长度
  
  let truncatedContent = targetLine;
  if (targetLine.length > maxLength) {
    const start = Math.max(0, keywordIndex - 40);
    const end = Math.min(targetLine.length, keywordIndex + keyword.length + 40);
    truncatedContent = (start > 0 ? '...' : '') + 
                      targetLine.slice(start, end) + 
                      (end < targetLine.length ? '...' : '');
  }
  
  // 高亮关键词
  const regex = new RegExp(keyword, 'gi');
  return truncatedContent.replace(regex, match => `<span style="color: #f56c6c">${match}</span>`);
};

// 格式化时间
const formatTime = (time) => {
  if (!time) return '';
  const date = new Date(time);
  return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`;
};

// 保存搜索历史
const saveSearchHistory = (keyword) => {
  const history = JSON.parse(localStorage.getItem('searchHistory') || '[]');
  const counts = JSON.parse(localStorage.getItem('searchCounts') || '{}');
  
  // 更新搜索次数
  counts[keyword] = (counts[keyword] || 0) + 1;
  
  // 更新搜索历史
  if (!history.includes(keyword)) {
    history.unshift(keyword);
    if (history.length > 10) history.pop();
  }
  
  localStorage.setItem('searchHistory', JSON.stringify(history));
  localStorage.setItem('searchCounts', JSON.stringify(counts));
  searchHistory.value = history;
};

// 获取搜索次数
const getSearchCount = (keyword) => {
  const counts = JSON.parse(localStorage.getItem('searchCounts') || '{}');
  return counts[keyword] || 0;
};

// 初始化加载搜索历史
onMounted(() => {
  searchHistory.value = JSON.parse(localStorage.getItem('searchHistory') || '[]');
});
</script>

<style scoped>
.mobile-page {
  height: 100vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.a_black {
  text-decoration: none;
  color: inherit;
}

:deep(.el-scrollbar__wrap) {
  overflow-x: hidden;
}
</style>
