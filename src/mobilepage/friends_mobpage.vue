<template>
  <div class="mobile-page">
    <Topbar topbartitle="朋友组织"></Topbar>
    <TypewriterDiv v-if="!showDetails" :text="infoText" @click="handleClick"></TypewriterDiv>
    
    <el-scrollbar v-show="showDetails">
      <div v-for="(item, index) in paginatedUsers" :key="index" class="news-item">
        <router-link class="a_black" :to="{ name: 'detail_mobpage', params: { id: item.item_id, subpagetype: '人物群组-详情' } }">
          <div class="news-details"
            style="display: flex; align-items: flex-start; padding: 10px; border-bottom: 0.5px dotted grey;">
            <div style="flex: 0 0 auto; margin-right: 10px; display: flex; align-items: center; height: 100%;">
              <el-avatar :size="50" class="custom-avatar" shape="square">
                <div class="custom-icon" style="font-weight: bolder;">{{ item.item_title.charAt(0) }}</div>
              </el-avatar>
            </div>
            <div style="flex: 1; text-align: left;">
              <div>
                <span style="font-size: 20px;font-weight: bold;">{{ item.item_title }}</span>
              </div>
              <div>
                <span :style="{ color: getColor(item.item_subtype) }">{{ item.item_subtype }}</span>
                <span style="color: gray;">｜最近更新</span>
                <!-- 此外还有最新注册和匹配推荐 -->
              </div>
            </div>
          </div>
        </router-link>
      </div>
      <div style="height: 200px;"></div>
    </el-scrollbar>
    


    <mob_opbar 
      v-show="showDetails"
      fromwhere="m朋友组织"
      :current_number="currentPage"
      :total_number="users.length"
      @prev10="changePage('up')"
      @next10="changePage('down')"
      @search="handleSearch"
      @followed="handleFollowed"
      @refresh1="handleRefresh"
    />
  </div>
</template>

<script setup>
import Topbar from '../mobilecomponents/Topbar.vue';
import TypewriterDiv from '../mobilecomponents/TypewriterDiv.vue';
import mob_opbar from '../mobilecomponents/mob_opbar.vue';
import { ref, computed, onActivated } from 'vue';
import axios from 'axios';
import { ElLoading } from 'element-plus';

const infoText = ref('向您推送30个朋友或组织');
const showDetails = ref(false);
const currentPage = ref(1);
const itemsPerPage = 10;

const users = ref([]);
const loadingInstance = ref(null);

const handleClick = async () => {
  try {
    
    await loadUsers();
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

const loadUsers = async () => {
  handleExpand();
  try {
    const response = await axios.post('https://www.aworld.wiki/api/iteminfo/show_itemlist/', {
      item_type: 'm朋友组织',
    });
    console.log('请求成功:', response.data);
    users.value = response.data;
  } catch (e) {
    console.error('加载列表失败:', e);
  } finally {
    if (loadingInstance.value) {
      loadingInstance.value.close();
    }
  }
};

const paginatedUsers = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  return users.value.slice(start, start + itemsPerPage);
});

const changePage = (direction) => {
  if (direction === 'up' && currentPage.value > 1) {
    currentPage.value--;
  } else if (direction === 'down' && currentPage.value < Math.ceil(users.value.length / itemsPerPage)) {
    currentPage.value++;
  }
};

const getColor = (itemType) => {
  if (itemType === '现实组织' || itemType === '自建小组') {
    return 'darkblue'; // 黄金色
  } else if (itemType === '现实人物') {
    return 'brown'; // 橙色
  } else if (itemType === '注册用户') {
    return 'gray'; // 灰色
  }
  return 'inherit'; // 默认颜色
};

const handleSearch = () => {
  console.log('处理查找');
  // 实现查找功能
};

const handleFollowed = () => {
  console.log('处理我关注的');
  // 实现查看关注列表功能
};

const handleRefresh = async () => {
  console.log('处理刷新');
  currentPage.value = 1;//这是刷新之后回到第一分页
  handleExpand();
  try {
    await loadUsers();
  } finally {
    if (loadingInstance.value) {
      loadingInstance.value.close();
    }
  }
};

// 添加 activated 钩子
onActivated(() => {
  console.log('friends_mobpage activated');
  // 如果需要在重新激活时刷新数据，可以取消下面的注释
  // if (showDetails.value) {
  //   loadUsers();
  // }
});

// ... (keep any other existing logic)
</script>

<style scoped>
.mobile-page {
  height: 100vh;
  overflow: hidden;  /* 防止页面整体滚动 */
  padding-bottom: 0px;
  /* 根据需要调整，为底部元素留出空间 */
  box-sizing: border-box;
  /* 确保padding不会增加元素的总高度 */
}

/* 如果你之后需要再次使用.content类，可以取消注释并调整样式 */

.content {
  flex-grow: 1;
  overflow-y: auto;
  padding-bottom: 10px;
  /* 给底部按钮留出一些空间 */
  min-height: 250px;
}

.opstyle {
  /* color: cornflowerblue;font-weight: bolder;font-size: 6vw; */
  color: gray;
  font-weight: bolder;
  font-size: 6vw;
}

.user-card {
  border-bottom: 1px dotted grey;
  margin-bottom: 3px;
  padding: 10px;
  transition: background-color 0.3s ease;
}

.user-card.active {
  background-color: #e0e0e0;
}

p {
  text-align: left;
  margin: 5px 0;
}


.news-item {
  background-color: #f0f0f0;
  margin-bottom: 10px;
}

.news-details {
  background-color: #ffffff;
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


:deep(.el-table) {
  background-color: transparent !important;
}


:deep(.el-table tr),
:deep(.el-table th) {
  background-color: transparent !important;
}

:deep(.el-table td) {
  background-color: transparent !important;
}

:deep(.el-table--enable-row-hover .el-table__body tr:hover > td) {
  background-color: rgba(0, 0, 0, 0.05) !important;
}

:deep(.el-table--border),
:deep(.el-table--group) {
  border-color: #EBEEF5;
}

:deep(.el-table td),
:deep(.el-table th.is-leaf) {
  border-bottom: 1px solid #EBEEF5;
}
</style>

