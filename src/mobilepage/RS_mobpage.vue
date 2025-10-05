<template>
  <div class="mobile-page">
    <Topbar topbartitle="推荐阅读"></Topbar>
    <TypewriterDiv v-if="!showDetails" :text="newsText" @click="handleClick"></TypewriterDiv>


    <!-- <el-empty image="https://z2024-1302616346.cos.ap-nanjing.myqcloud.com/underconstruction.jpg"
      description="working overtime" image-size="100%">
      <h2>该区正在建设，敬请期待!</h2>
      <h2>This section is under construction!</h2>
      </el-empty> -->
    <!-- 这里的推荐阅读直接推荐到元素详情页，可以选择上一条和下一条，
      并且注释（来自哪种推荐），有三种推荐方式，1，文本内容匹配，2，用户特点匹配，3，热门推荐。
      这里置顶一个网站介绍，项目介绍，我最近的计划，
      例如最近计划：我如何用区块链的方式改造，我如何进行公社管理和改造，如何进行通用化，模块化，可回收，可自我修复的生产体系。 
      这里分为三类，一类是置顶阅读，一种是推荐阅读3个，一个是最新阅读
      最下面的按键，换一批
      -->
    <el-scrollbar v-if="showDetails">
      <div v-for="(item, index) in RSlist" :key="index">
        <router-link class="a_black"
          :to="{ name: 'detail_mobpage', params: { id: item.item_id, subpagetype: '推荐阅读-详情' } }">
          <el-row style="text-align: left;font-size: 20px;" v-if="item.item_type !== '段落'"><strong>{{ item.item_title}}</strong></el-row>
          <el-row style="text-align: left;font-size: 20px;"
            v-if="item.item_type === '段落'"><strong>{{ item.sparefield1 }}</strong>{{ item.item_title }}</el-row>
          <!-- <el-row style="text-align: left;font-size: 18px;color:gray;border-bottom: 1px solid lightgray;"> -->
          <el-row style="text-align: left;font-size: 18px;color:gray;">
            {{ index === 0 ? '管理员置顶' : (index <= 3 ? '内容相似' : (index <= 6 ? '用户相似' : '随机抽取')) }}｜{{ item.item_subtype }}
          </el-row>
          <el-row class="ellipsis-row">
            <span class="ellipsis-text" style="font-size: 18px; color: gray; border-bottom: 1px solid lightgray;">
              {{ item.item_content }}
            </span>
          </el-row>
        </router-link>
      </div>
      <div style="height: 200px;"></div>

    </el-scrollbar>


    <mob_opbar v-if="showDetails" @change="loadRS" fromwhere="m推荐阅读" />

  </div>
</template>

<script setup>
import Topbar from '../mobilecomponents/Topbar.vue';
import mob_opbar from '../mobilecomponents/mob_opbar.vue';
import { ElLoading } from 'element-plus';
import { onMounted, ref, onActivated, computed } from 'vue';  // 添加 onActivated
import axios from 'axios';
import TypewriterDiv from '../mobilecomponents/TypewriterDiv.vue';

const showDetails = ref(false);
const newsText = ref('根据你的爱好和身份，向你推荐十个段落');
const RSlist = ref([]);
const loadingInstance = ref(null);


const handleClick = async () => {
  try {
    await loadRSData();
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

const loadRSData = async () => {
  try {
    const response = await axios.post('https://www.aworld.wiki/api/iteminfo/show_itemlist/', {
      item_type: 'm推荐阅读',
    });
    console.log('请求成功:', response.data);
    RSlist.value = response.data;
  } catch (e) {
    console.error('加载列表失败:', e);
  }
};

const loadRS = async () => {
  handleExpand();
  showDetails.value = true;
  
  await loadRSData();
  loadingInstance.value.close();
};

//添加 activated 钩子
onActivated(() => {
  //当组件被重新激活时，不需要重新加载数据
  console.log('RS_mobpage activated');
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

.ellipsis-row {
  width: 100%;
  text-align: left;
}

.ellipsis-text {
  display: block;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  width: 100%;
  padding: 0;
}
</style>
