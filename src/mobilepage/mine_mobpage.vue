<template>
  <div class="mobile-page">
    <Topbar topbartitle="个人事务"></Topbar>
    <el-scrollbar>
      <el-row>
        <el-col :span="24">
          <UserInfoMobCard 
            :userData="userData"
            :localUserId="localUserId"
            defaultAvatarText="上传头像"
          />
        </el-col>
      </el-row>

      <el-row>
        <el-col :span="12">
          <el-card style="width: 100%; height: 150px;" shadow="always">身份码</el-card>
          <el-card style="width: 100%; height: 150px;" shadow="always">投票选举</el-card>
        </el-col>
        <el-col :span="12">
          <el-card style="width: 100%; height: 300px;" shadow="always">今日任务</el-card>
        </el-col>
      </el-row>

      <el-row>
        <el-col :span="24">
          <el-card style="width: 100%; height: 150px;" shadow="always">任务清单</el-card>
        </el-col>
      </el-row>

      <el-row>
        <el-col :span="12">
          <el-card style="width: 100%; height: 300px;" shadow="always">福利与休假</el-card>
        </el-col>
        <el-col :span="12">
          <el-card style="width: 100%; height: 150px;" shadow="always">公共物品</el-card>
          <el-card style="width: 100%; height: 150px;" shadow="always">担任公职</el-card>
        </el-col>
      </el-row>
      <div style="height: 200px;"></div>
    </el-scrollbar>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { ElLoading, ElMessage } from 'element-plus';
import Topbar from '../mobilecomponents/Topbar.vue';
import UserInfoMobCard from '../mobilecomponents/UserInfoMobCard.vue';

const userData = ref({
  item_title: '',
  item_id: '',
  item_subtype: '',
  sparefield1: '',
  time_create: '',
  introduction: '',
  followCount: 0,
  shareCount: 0,
  commentCount: 0,
  likeCount: 0,
  dislikeCount: 0
});
const localUserId = ref(localStorage.getItem('userid'));
const loadingInstance = ref(null);

const handleExpand = () => {
  loadingInstance.value = ElLoading.service({
    lock: true,
    text: '加载中...',
    spinner: 'el-icon-loading',
    background: 'rgba(0, 0, 0, 0.7)',
    customClass: 'custom-loading-text',
  });
};

const fetchUserInfo = async () => {
  const userId = localStorage.getItem('userid');
  if (!userId) {
    ElMessage.error('未找到用户ID');
    return;
  }

  handleExpand();
  
  try {
    const response = await axios.post('https://www.aworld.wiki/api/iteminfo/show_all_iteminfo/', {
      id: userId
    });
    console.log('User Info Response:', response.data);
    userData.value = response.data;
  } catch (error) {
    console.error('Error fetching user info:', error);
    ElMessage.error(error.message || '获取用户信息失败');
  } finally {
    if (loadingInstance.value) {
      loadingInstance.value.close();
    }
  }
};

// 在组件挂载时自动加载用户信息
onMounted(() => {
  fetchUserInfo();
});
</script>

<style scoped>
.mobile-page {
  min-height: 100vh;
  padding-bottom: 0px;
  box-sizing: border-box;
}

:deep(.el-scrollbar__wrap) {
  overflow-x: hidden;
}
</style>
  