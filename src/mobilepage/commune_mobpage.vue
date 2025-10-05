<template>
  <div class="mobile-page">
    <Topbar topbartitle="公共事务"></Topbar>
    <!-- <el-empty image="https://z2024-1302616346.cos.ap-nanjing.myqcloud.com/underconstruction.jpg"
      description="working overtime" image-size="100%">
      <h2>该区正在建设，敬请期待!</h2>
      <h2>This section is under construction!</h2>
    </el-empty> -->
    <!-- 这里显示总公社和直属公社的公共决策 -->
<!-- 
    <el-empty image="http://aworld-1302616346.cos.ap-hongkong.myqcloud.com/static_pic/underconstruction_mob.jpg"
      description="working overtime" image-size="100%">
      <h2>该区正在建设，敬请期待!</h2>
      <h2>This section is under construction!</h2>
      </el-empty> -->



  <!-- 添加抽屉组件 -->
  <!-- <el-drawer
      v-model="drawerVisible"
      title="历史动态"
      direction="btt"
      size="80%"
    >
      <el-scrollbar height="100%">
        <div v-for="(item, index) in historyItems" :key="index" class="history-item">
          <p><strong>{{ item.date }}</strong></p>
          <p>{{ item.content }}</p>
        </div>
      </el-scrollbar>
    </el-drawer> -->
<p style="text-align: left;font-size: 20px;">公共事务展示｜尚未完成</p>
<!-- 这里应该有事务的提醒功能，每个月每个季度等频率。此外，用户可以在小组直接发布相关契约等正式文件 -->
<br>
    <el-scrollbar>
    <el-timeline style="max-width: 600px;text-align: left;font-size: 22px;">
    <el-timeline-item
      v-for="(activity, index) in activities"
      :key="index"
      :icon="activity.icon"
      :type="activity.type"
      :color="activity.color"
      :size="activity.size"
      :hollow="activity.hollow"
      :timestamp="activity.timestamp"
    >
      {{ activity.content }}
    </el-timeline-item>
  </el-timeline>

  <div style="height: 70px;"></div>
  </el-scrollbar>


  </div>
</template>

<script setup>
import { ref } from 'vue';
import Topbar from '../mobilecomponents/Topbar.vue';
import { MoreFilled } from '@element-plus/icons-vue';

const activities = [
  {
    content: '西撒公社年度大会',
    timestamp: '2018-04-12 20:46',
    size: 'large',
    type: 'primary',
    color: 'red',
    icon: MoreFilled,
  },
  {
    content: '001环保契约',
    timestamp: '2018-04-03 20:46',
    color: '#0bbd87',
  },
  {
    content: '001公社代表选举结果',
    timestamp: '2018-04-03 20:46',
    size: 'large',
    color: 'blue',
  },
  {
    content: '001公社代表选举',
    timestamp: '2018-04-03 20:46',
    type: 'primary',
    hollow: true,
    color: 'blue',
  },
  {
    content: '002公社总契约',
    timestamp: '2018-04-03 20:46',
    color: 'blue',
  },
]



</script>

