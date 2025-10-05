<template>
  <div class="mobile-page">
    <!-- <Topbar :topbartitle="subPageType"></Topbar> -->
    <div class="top-bar">
      <span @touchstart="navigateTo"><a class="mainlinkstyle">返回</a>｜</span>
      <!-- <div style="font-size: 20px;"><b>{{ subPageType }}</b></div>  -->
      <div style="font-size: 20px;">{{ detailData?.item_type }}详情</div>
    </div>

    <el-scrollbar>

    <div v-if="detailData?.item_type === '人物'">
      <el-row>
        <el-col :span="24">
          <UserInfoMobCard 
            :userData="detailData"
            :localUserId="localUserId"
            defaultAvatarText="无头像"
          />
        </el-col>
      </el-row>

      <el-row style="font-size: 20px;font-weight: bold;color: gray;" justify="start"  v-show="!showDetails">
        <span @click="fetchUserDynamics">点看该用户最近10条动态</span>
      </el-row>
      <el-row style="font-size: 20px;" justify="start" v-show="showDetails">
        <span style="color: black;font-weight: lighter;">查询到{{ newsItems.length }}条记录</span>
        <span style="font-size: 20px;font-weight: bold;color: gray;" @click="fetchUserDynamics">｜刷新</span>
      </el-row>
      <div v-for="(item, index) in newsItems" :key="index" v-if="showDetails">
          <NewsItem :item="item" :userSelfId="localUserId" fromwhere="m用户动态" />
        </div>
    </div>

    <div v-if="detailData?.item_type === '群组'" style="text-align: left;">
    <el-card style="width: 100%; height: auto;" shadow="always">
    <el-row :gutter="0">
      <el-col :span="10" @click="loadImage" style="display: flex; align-items: center;background-color:#f0f0f0;">
        <img v-if="imageLoaded" class="custom-image" :src="imageSrc" />
        <div v-else class="default-avatar">
          <div class="avatar-group">
            <div class="avatar-circle"></div>
            <div class="avatar-circle center"></div>
            <div class="avatar-circle"></div>
          </div>
          <div class="avatar-text">{{ defaultAvatarText }}上传头像</div>
        </div>
      </el-col>
      <el-col :span="14" style="text-align: left; font-size: 18px;padding-left: 5px;">
        <div class="ellipsis"><strong> 群组名 </strong></div>
        <div>10000025</div>
        <div style="color: gray;">
          <span>现实团体</span>
        </div>
        <div><span style="color: gray;">来自未知</span></div>
        <div><span style="color: gray;">注册于1年前</span></div>
        <div style="color: gray;">
          <span style="color: gray;font-weight: bold;">
            <strong>群内聊天</strong>
          </span>
        </div>
      </el-col>
    </el-row>

    <el-row style="text-align: left;font-size: 18px;">
      <span style="color: black;">
        <span style="color: gray">群组介绍：这是群组的介绍文字，限100字。</span>
      </span>
    </el-row>
    <el-row style="text-align: left;">
      <span style="color:darkcyan;font-size: 18px;">
        群人数0
        评0
        顶0
        踩0
      </span>
    </el-row>
  </el-card>

  </div>
   

    <!-- <el-row style="text-align: left; font-size: 20px;">介绍说明：这是用户的自我介绍，也是各种数据展示，也有用户的联系方式</el-row> -->
    <!-- <el-row style="text-align: left; font-size: 20px;" @click="toggleDrawer">-----击这里显示他的历史动态-----</el-row> -->

    <div v-if="detailData?.item_type === '发言'" style="text-align: left;">
      <el-card style="width: 100%; height: auto;" shadow="always">
          <div style="text-align: left;font-size: 24px;color:brown;">
          <span style="color: black;font-size: 22px;">{{ detailData.user1name }}:</span>
          <span style="font-size: 20px;text-align: left;" v-html="detailData.item_content"></span>
          <span style="font-size: 18px;color: gray;">发表于{{ formatTime(detailData.time_create) }}</span>
        </div>

        <el-row style="text-align: left;font-size: 18px;color:gray;">
          <div>属性:{{ detailData.item_subtype }}｜{{ detailData.item_id }}｜正常有效</div>
        </el-row>
        <el-row style="text-align: left;"><span style="color:darkcyan;font-size: 18px;">关注1-分享1-评论1-顶1-踩1</span></el-row>
      </el-card>
      <div style="text-align: left;"><strong>点看该用户全部发言</strong></div>
    </div>

   



    <div v-if="detailData?.item_type === '段落'">
      <el-card style="width: 100%; height: auto;" shadow="always">

      <el-row style="font-size: 22px;font-weight: bold;text-align: left;">{{ detailData.sparefield1 }}</el-row>
      <el-row style="font-size: 22px;text-align: left;color: black;"><span style="text-align: left;font-size: 20px;color:gray;">段落名:</span>{{ detailData.item_title }}</el-row>

      <el-row style="text-align: left;font-size: 20px;color:gray;">
        <div>标识号:{{ detailData.item_id }}｜{{ detailData.item_subtype }}</div>
      </el-row>
      <el-row style="text-align: left;font-size: 20px;color:gray;">
        <div>创建日:20200101｜正常有效</div>
      </el-row>
      <el-row style="text-align: left;font-size: 20px;color:gray;">
        <div>管理员:10000002｜附件0</div>
      </el-row>
      <el-row style="text-align: left;"><span style="color:darkcyan;font-size: 18px;">关注1-分享1-评1-顶1-踩1</span></el-row>
    </el-card>


      <el-row style="text-align: left;font-size: 20px;color:gray;">
        <div v-if="detailData?.item_type === '段落'">段落正文：第{{ detailData?.itemXsn }}自然段</div>
        <div>
          <span style="font-size: 20px;color:black" v-html="detailData.item_content"></span>
        </div>
      </el-row>
      <div style="text-align: left;font-size: 20px;">

      </div>

    </div>




    <div v-if="detailData?.item_type === '文章'">
      <el-card style="width: 100%; height: auto;" shadow="always">
        <el-row style="font-size: 22px;font-weight: bold;text-align: left;">{{ detailData.item_title }}</el-row>
        <el-row style="text-align: left;font-size: 20px;color:gray;">
          <div>标识号:{{ detailData.item_id }}｜{{ detailData.item_subtype }}</div>
        </el-row>
        <el-row style="text-align: left;font-size: 20px;color:gray;">
          <div>创建日:20200101｜正常有效</div>
        </el-row>
        <el-row style="text-align: left;font-size: 20px;color:gray;">
          <div>管理员:10000002｜附件0</div>
        </el-row>
        <el-row style="text-align: left;font-size: 20px;color:gray;">
          <span>说明备注：<span style="color:black;" v-html="detailData.item_content"></span></span>
        </el-row>
        <el-row style="text-align: left;"><span style="color:darkcyan;font-size: 18px;">关注1-分享1-评论1-顶1-踩1</span></el-row>
      </el-card>

      <div v-if="!isFullDirectoryVisible" style="color: gray;font-size: 22px;font-weight: bold;text-align: left;">
        <strong @click="fetchFullDirectory">点击查看全文目录</strong>
      </div>
      <!-- 添加状态控制 -->
      <el-row v-if="isFullDirectoryVisible">
        <div v-for="(item, index) in paginatedList" :key="index"
          style="text-align: left;font-size: 18px;border-bottom: 1px solid lightgray;"
          @click="fetchListPara(item.item_id)">
          <div>{{ item.item_title }}</div> <!-- Display the title of each item -->
          <div class="ellipsis-multi-line" style="color: gray;">{{ item.item_content }}</div>
          <!-- Display the content of each item -->
        </div>
      </el-row>
    </div>
    
    <div style="height: 200px;"></div>
    </el-scrollbar>

    <mob_opbar 
      fromwhere="m元素详情"
      :current_number="currentPage"
      :total_number="fullDirectoryList.length"
      :item_detail="detailData"
      :isFollowed="detailData?.is_followed"
      @prevpara="fetchPrevious"
      @paramenu="fetchMenu"
      @nextpara="fetchNext"
      @prev10="fetchPreviousPage"
      @next10="fetchNextPage"
      @share="handleShare"
      @follow="handleFollow"
      @like="handleLike"
      @comment="handleComment"
      @dislike="handleDislike"
      @refresh="handleRefresh"
    />
  </div>
</template>

<script setup>
import { onMounted, ref, computed, watch } from 'vue';
import axios from 'axios';
import { useRoute } from 'vue-router';
import { useRouter } from 'vue-router';
import { ElLoading, ElMessage } from 'element-plus'; // 引 Element Plus 的 Loading 组件
import NewsItem from '@/mobilecomponents/NewsItem.vue';  // 修改导入路径
import mob_opbar from '../mobilecomponents/mob_opbar.vue';
import UserInfoMobCard from '@/mobilecomponents/UserInfoMobCard.vue';



const router = useRouter();

const route = useRoute();
const detailData = ref(null); // 确保 detailData 被定义
const localUserId = Number(localStorage.getItem('userid')); // 转化为值型
const itemId = ref(route.params.id); // 改为使用 ref




function navigateTo() {

  // 这里需要判断，根据跟中传递参数判断返回的页面。
  // let path;  
  // if (props.topbartitle === '推荐详细') {  
  //     path = '/page1';  
  // } else if (props.topbartitle === '人物群组-详情') {  
  //     path = '/friends_mobpage';  
  // } else if (props.topbartitle === '新闻详情') {  
  //     path = '/page3';  
  // } else {  
  //     path = '/';  
  // }  
  // router.push(path).catch(err => {  
  //     console.error('Navigation failed:', err);  
  // });  
  router.go(-1);
};
const loadingInstance = ref(null); // 添加加载实例

const handleExpand = () => {
  loadingInstance.value = ElLoading.service({ // 开始加载
    lock: true,
    text: '加载中...', // 增大字体
    spinner: 'el-icon-loading',
    background: 'rgba(0, 0, 0, 0.7)',
    customClass: 'custom-loading-text',
  });
};

// 加加载状态
const isLoading = ref(false);

// 修改 fetchItemInfo 函数
const fetchItemInfo = async (id, fetchtype) => {
  isLoading.value = true;
  handleExpand();
  try {
    const response = await axios.post('https://www.aworld.wiki/api/iteminfo/show_all_iteminfo/', { 
      id: id, 
      fetchtype: fetchtype,
      user_id: localUserId // 添加用户ID参数
    });
    console.log('Response:', response.data);
    return response.data;
  } catch (error) {
    console.error('Error fetching item info:', error);
    ElMessage.error(error.message);
    throw error;
  } finally {
    isLoading.value = false;
    if (loadingInstance.value) {
      loadingInstance.value.close();
    }
  }
};

// 修改 fetchPrevious 函数
const fetchMenu = async () => {
  detailData.value = await fetchItemInfo(detailData.value.itemXid);

};

const fetchListPara = async (id) => {
  detailData.value = await fetchItemInfo(id);

};


// 修改 fetchPrevious 函数
const fetchPrevious = async () => {
  try {
    detailData.value = await fetchItemInfo(detailData.value.item_id, 'fetchPrevious');
  } catch (error) {
    if (error.response && error.response.data && error.response.data.error) {
      ElMessage.error(error.response.data.error); // 显示后端返回的友好提示
    } else {
      ElMessage.error('获取上一段失败');
    }
  }
};

// 修改 fetchNext 函数
const fetchNext = async () => {
  try {
    detailData.value = await fetchItemInfo(detailData.value.item_id, 'fetchNext');
  } catch (error) {
    // 检查是否有错误响应
    if (error.response && error.response.data && error.response.data.error) {
      ElMessage.error(error.response.data.error); // 使用 info 而不是 error，因为这是预期的提示
    } else {
      ElMessage.error('获取下一段失败');
    }
  }
};


// Ensure params is accessed correctly
const params = route.params || {};  // Safely access params
// const itemId = params.id;           // 获取 id
const subPageType = params.subpagetype; // 获取 subpagetype

onMounted(async () => {
  try {
    if (!route.params.id) {  // 直接使用 route.params.id 而不是 itemId
      ElMessage.error('未找到项目ID');
      return;
    }
    detailData.value = await fetchItemInfo(route.params.id);
  } catch (error) {
    console.error('Failed to load item details:', error);
    ElMessage.error('加载详情失败');
  }
});

// 这里可以添加任何必要的逻辑

const imageLoaded = ref(false); // 控制图片是否加载
const imageSrc = 'http://aworld-1302616346.cos.ap-hongkong.myqcloud.com/static_pic/underconstruction_mob.jpg'; // 图片源

const loadImage = () => {
  imageLoaded.value = true; // 点击后加载图片
};



const formatTime = (op_time) => {
  const now = new Date();
  const opDate = new Date(op_time);
  const timeDiff = now - opDate; // 时间差单位为毫秒

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






const fullDirectoryList = ref([]); // 存储所有目录列表
const currentPage = ref(1); // 当前页码
const itemsPerPage = 10; // 每页显示的条目数

const isFullDirectoryVisible = ref(false); // 新增状态变量

const fetchFullDirectory = async () => {
  isLoading.value = true;
  handleExpand();
  try {
    const response = await axios.post('https://www.aworld.wiki/api/iteminfo/show_itemlist/', {
      item_type: '全文目录',
      id: detailData.value.item_id, // 传递必要的参数
      user_id: localUserId
    });
    fullDirectoryList.value = response.data; // 更新录列表
    isFullDirectoryVisible.value = true; // 点后设置为可见
  } catch (error) {
    console.error('Error fetching full directory:', error);
    ElMessage.error('获取全文目录失败，请稍后重试');
  } finally {
    isLoading.value = false;
    if (loadingInstance.value) {
      loadingInstance.value.close();
    }
  }
};

// 计算当前页的数据
const paginatedList = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  return fullDirectoryList.value.slice(start, start + itemsPerPage);
});

// 新增函数以获取上一页
const fetchPreviousPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
};

// 新增函数以取下一页
const fetchNextPage = () => {
  if (currentPage.value < Math.ceil(fullDirectoryList.value.length / itemsPerPage)) {
    currentPage.value++;
  }
};

// 添加新的状态变量
const showDetails = ref(false);
const newsItems = ref([]);

// 修改 fetchUserDynamics 方法
const fetchUserDynamics = async () => {
  isLoading.value = true;
  handleExpand();
  try {
    const response = await axios.post('https://www.aworld.wiki/api/opinfo/get_oplist/', {
      user_id: detailData.value.item_id || '',
      op_type: 'm用户动态',
    });
    console.log('请求成功:', response.data);
    newsItems.value = response.data;
    showDetails.value = true; // 显示动态列表
  } catch (e) {
    console.error('加载用户动态失败:', e);
  } finally {
    isLoading.value = false;
    if (loadingInstance.value) {
      loadingInstance.value.close();
    }
  }
};

// 修改 watch
watch(() => route.params.id, async (newId) => {
  if (newId) {
    try {
      detailData.value = await fetchItemInfo(newId);
    } catch (error) {
      console.error('Failed to load item details:', error);
      ElMessage.error('加载详情失败');
    }
  }
});

// 添加新的处理函数
const handleShare = () => {
  console.log('理分享');
};

const handleFollow = () => {
  console.log('处理关注');
};

const handleLike = () => {
  console.log('处理顶');
};

const handleComment = () => {
  console.log('处理评论');
};

const handleDislike = () => {
  console.log('处理踩');
};

const handleRefresh = async () => {
  try {
    if (!route.params.id) {  // 直接使用 route.params.id 而不是 itemId
      ElMessage.error('未找到项目ID');
      return;
    }
    detailData.value = await fetchItemInfo(detailData.value.item_id);
  } catch (error) {
    console.error('Failed to load item details:', error);
    ElMessage.error('加载详情失败');
  }
};

</script>

<style scoped>
.custom-image {
  height: auto;
  /* 设置高度为160px */
  width: 100%;
  /* 宽度最大不超过容器宽度 */
  object-fit: cover;
  /* 保持纵横比并填充容器 */
  display: flex;
  /* 添加 flex 布局 */
  align-items: center;
  /* 垂直居中 */
}

.history-item {
  border-bottom: 1px solid #eaeaea;
  padding: 10px 0;
}

.history-item:last-child {
  border-bottom: none;
}

.ellipsis {
  white-space: nowrap;
  /* 不换行 */
  overflow: hidden;
  /* 超出部分隐藏 */
  text-overflow: ellipsis;
  /* 超出部分用省略号表示 */
}

.ellipsis-multi-line {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  /* 显示两行 */
  overflow: hidden;
  text-overflow: ellipsis;
}

.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 5px 0;
  border-bottom: 2px solid #333;
  margin-bottom: 5px;
  font-size: 25px;
}



.mainlinkstyle {
  color: grey;
  font-weight: bold;
  font-size: 6vw;
}

.mobile-page {
  min-height: 100vh;
  padding-bottom: 0px;
  box-sizing: border-box;
}

:deep(.el-scrollbar__wrap) {
  overflow-x: hidden;
}

.default-avatar {
  width: 100px;
  height: 100px;
  background: #f5f5f5;
  position: relative;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  align-items: center;
}

.avatar-group {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: -10px;
}

.avatar-circle {
  width: 32px;
  height: 32px;
  background: #e0e0e0;
  border-radius: 50%;
  border: 2px solid #f5f5f5;
  margin: 0 -6px;
  position: relative;
}

.avatar-circle.center {
  width: 36px;
  height: 36px;
  background: #d0d0d0;
  z-index: 2;
  margin: 0 -8px;
}

.avatar-text {
  position: absolute;
  width: 100%;
  text-align: center;
  color: gray;
  bottom: 0px; /* 将文字放在头下方 */
  left: 0;
}

/* 覆盖 el-card 的默认内距 */
:deep(.el-card__body) {
  padding: 10px;
}
</style>
