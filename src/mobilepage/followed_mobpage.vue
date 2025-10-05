<template>
    <div class="mobile-page">
      <Topbar topbartitle="关注收藏"></Topbar>
      <TypewriterDiv v-if="!showDetails" :text="infoText" @click="handleClick"></TypewriterDiv>

      <el-scrollbar v-show="showDetails">
        <div v-for="(item, index) in paginatedFollows" :key="index">
          <router-link class="a_black"  :to="{ name: 'detail_mobpage', params: { id: item.item0id, subpagetype: '关注收藏-详情' } }">
                <el-row style="text-align: left;font-size: 20px;"><strong>{{ item.item0title }}</strong></el-row>
                <el-row style="text-align: left;font-size: 18px;color:gray">
                  <span style="color: darkblue;">{{ item.item0type }}</span>｜关注于{{ formatTime(item.op_time) }}
                </el-row>
                <el-row style="text-align: left;font-size: 18px;color: gray;border-bottom: 1px solid lightgray;">
                  <span>关注附言:<span style="color: grey;" v-html="item.ps_content"></span></span>
                </el-row>
          </router-link>
        </div>
        <div style="height: 200px;"></div>
      </el-scrollbar>

  

      <mob_opbar 
        v-show="showDetails"
        fromwhere="m关注收藏"
        :current_number="currentPage"
        :total_number="followslist.length"
        @prev10="changePage('up')"
        @next10="changePage('down')"
        @refresh2="loadFollows"
      />

    </div>
  </template>
  
  <script setup>
  import Topbar from '../mobilecomponents/Topbar.vue';
  import TypewriterDiv from '../mobilecomponents/TypewriterDiv.vue';
  import mob_opbar from '../mobilecomponents/mob_opbar.vue';
  import { ref, computed, onActivated } from 'vue'
  import axios from 'axios';
  import { ElLoading } from 'element-plus';

  
  const infoText = ref('这是你关注的知识、用户、组织');
const showDetails = ref(false);
const currentPage = ref(1);
const itemsPerPage = 10;

const followslist = ref([]);
const loadingInstance = ref(null);

const handleClick = async () => {
  try {
    await loadFollows();
    showDetails.value = true;


  } catch (e) {
    console.error('请求失败:', e);
    showDetails.value = true;
  }
};

const handleExpand = () => {
  loadingInstance.value = ElLoading.service({
    text: '加载中...',
    spinner: 'el-icon-loading',
    background: 'rgba(255, 255, 255, 0.7)',
  });
};

const loadFollows = async () => {
  try {
    currentPage.value = 1; //这是刷新之后回到第一分页
    handleExpand(); // 显示加载动画
    const response = await axios.post('https://www.aworld.wiki/api/opinfo/get_oplist/', {
      op_type: 'm关注收藏',
      user_id: localStorage.getItem('userid') || '',
    });
    console.log('请求成功:', response.data);
    followslist.value = response.data;
  } catch (e) {
    console.error('加载列表失败:', e);
  } finally {
    loadingInstance.value.close(); // 关闭加载动画
  }
};



const paginatedFollows = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  return followslist.value.slice(start, start + itemsPerPage); // 修正为使用 followslist
});

const changePage = (direction) => {
  if (direction === 'up' && currentPage.value > 1) {
    currentPage.value--;
  } else if (direction === 'down' && currentPage.value < Math.ceil(followslist.value.length / itemsPerPage)) {
    currentPage.value++;
  }
};


const formatTime = (op_time) => {
    const now = new Date();
    const opDate = new Date(op_time);
    const timeDiff = now - opDate; // 时间差，单位为毫秒

    const hoursDiff = Math.floor(timeDiff / (1000 * 60 * 60)); // 转换为小时
    const daysDiff = Math.floor(hoursDiff / 24); // 转换为天数

    if (hoursDiff < 8) {
        // 如果在8小时内，显示钟点和分钟
        return `${opDate.getHours()}:${opDate.getMinutes().toString().padStart(2, '0')}`;
    } else if (hoursDiff < 24) {
        // 如果在8小时到24小时之间，显示多少小时前
        return `${hoursDiff}小时前`;
    } else if (daysDiff < 30) {
        // 如果在30天内，显示几天前
        return `${daysDiff}天前`;
    } else {
        // 如果超过30天，返回完整的日期格式
        return opDate.toLocaleDateString(); // 或者自定义格式
    }
};

// 添加 activated 钩子
onActivated(() => {
  console.log('followed_mobpage activated');
  // 如果需要在重新激活时刷新数据，可以取消下面的注释
  // if (showDetails.value) {
  //   loadFollows();
  // }
});
  
  // 这里可以添加任何必要的逻辑
  </script>
  
  <style scoped>
  
  .mobile-page {  
    overflow-y: auto; /* 允许垂直滚动 */  
    min-height: 100vh; /* 或者设置一个固定的高度，确保内容超出时可以滚动 */  
    padding-bottom: 0px; /* 根据需要调整，为底部元素留出空间 */  
    box-sizing: border-box; /* 确保padding不会增加元素的总高度 */  
  }  
    

  
  
  </style>
