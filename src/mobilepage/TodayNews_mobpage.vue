<template>
  <div class="mobile-page">
    <Topbar topbartitle="新闻动态"></Topbar>
    <TypewriterDiv v-if="!showDetails" :text="newsText" @click="handleClick"></TypewriterDiv>


    <el-scrollbar>
    <div v-for="(item, index) in paginatedNewsItems" :key="index" v-show="showDetails">
      <NewsItem 
        :item="item"
        :userSelfId="userselfId"
        fromwhere="m新闻动态"
      />
    </div>
    <div style="height: 200px;"></div>
    </el-scrollbar>



          
    <mob_opbar 
      v-show="showDetails"
      fromwhere="m新闻动态"
      :current_number="currentPage"
      :total_number="newsItems.length"
      @prev10="changePage('up')"
      @next10="changePage('down')"
      @post="handlePost"
      @refresh3="reloadNews"
    />
  </div>
</template>

<script setup>
import Topbar from '../mobilecomponents/Topbar.vue';
import TypewriterDiv from '../mobilecomponents/TypewriterDiv.vue';
import { ref, computed, onActivated } from 'vue';
import axios from 'axios';
import NewsItem from '@/mobilecomponents/NewsItem.vue';
import { ElLoading, ElMessage } from 'element-plus';
import mob_opbar from '../mobilecomponents/mob_opbar.vue';

// const newsText = ref('这里显示你关注的用户或知识点的今日动态和互动信息，长按回复附言，ceshiceshi。');
const newsText = ref('这是你关注的用户或知识元素在最近7天内的新闻动态');
const showDetails = ref(false);
const newsItems = ref([]);
const currentPage = ref(1);
const itemsPerPage = 10;
const loadingInstance = ref(null);

const handleClick = async () => {
  try {
    await loadNews();
    showDetails.value = true;

  } catch (e) {
    console.error('请求失败:', e);
    showDetails.value = true;
  }
};

const loadNews = async () => {
  try {
    const response = await axios.post('https://www.aworld.wiki/api/opinfo/get_oplist/', {
      user_id: localStorage.getItem('userid') || '',
      op_type: 'm新闻动态',
    });
    console.log('请求成功:', response.data);
    newsItems.value = response.data;

  } catch (e) {
    console.error('加载新闻失败:', e);
  }
};

const reloadNews = async () => {
  currentPage.value = 1;//这是刷新之后回到第一分页
  handleExpand();
  await loadNews();
  loadingInstance.value.close();
};

const handleExpand = () => {
  loadingInstance.value = ElLoading.service({
    text: '加载中...',
    spinner: 'el-icon-loading',
    background: 'rgba(255, 255, 255, 0.7)',
  });
};

//计算当前页的新闻项
const paginatedNewsItems = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  return newsItems.value.slice(start, start + itemsPerPage);
});
//


//更新当前页
const changePage = (direction) => {
  if (direction === 'up' && currentPage.value > 1) {
    currentPage.value--;
  } else if (direction === 'down' && currentPage.value < Math.ceil(newsItems.value.length / itemsPerPage)) {
    currentPage.value++;
  }
};

const userselfId = ref(Number(localStorage.getItem('userid') || ''));

//添加 activated 钩子
onActivated(() => {
  //当组件被重新激活时，不需要重新加载数据
  console.log('TodayNews_mobpage activated');
});

// 添加发言处理函数
const handlePost = () => {
  console.log('处理发言');
  // 这里添加发言的具体逻辑
};

</script>

<style scoped>
.mobile-page {
  min-height: 100vh;
  padding-bottom: 0px;
  box-sizing: border-box;
}

.news-item {
  /* background-color: #f0f0f0; */
  margin-bottom: 10px;
}

.news-details {
  /* background-color: #ffffff; */
  border-radius: 8px;
}

.custom-avatar {
  display: flex;
  justify-content: center;
  align-items: center;
}

.custom-icon {
  font-size: 45px;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

:deep(.el-scrollbar__wrap) {
  overflow-x: hidden;
}
</style>

