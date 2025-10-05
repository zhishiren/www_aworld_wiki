<template>
  <el-card style="width: 100%; height: auto;" shadow="always" v-if="userData">
    <el-row :gutter="0">
      <el-col :span="10" @click="loadImage" style="display: flex; align-items: center;background-color:#f0f0f0;">
        <img v-if="imageLoaded" class="custom-image" :src="imageSrc" />
        <div v-else class="default-avatar">
          <div class="avatar-head"></div>
          <div class="avatar-body"></div>
          <div class="avatar-text">{{ defaultAvatarText }}</div>
        </div>
      </el-col>
      <el-col :span="14" style="text-align: left; font-size: 18px;padding-left: 5px;">
        <div class="ellipsis"><strong>{{ userData?.item_title || '加载中...' }}</strong></div>
        <div>{{ userData?.item_id || '' }}</div>
        <div style="color: gray;">
          <span>{{ userData?.item_subtype || '注册用户' }}</span>
        </div>
        <div><span style="color: gray;">来自</span>{{ userData?.sparefield1 || '未知地点' }}</div>
        <div><span style="color: gray;">注册于</span>{{ formatTime(userData?.time_create) }}</div>
        <div style="color: gray;">
          <span style="color: gray;font-weight: bold;">
            <strong>{{ isCurrentUser ? '修改信息' : '和TA聊天' }}</strong>
          </span>
        </div>
      </el-col>
    </el-row>

    <el-row style="text-align: left;font-size: 18px;">
      <span style="color: black;">
        <span style="color: gray">用户介绍：</span>{{ userData?.introduction || 'qq12345678' }}
      </span>
    </el-row>
    <el-row style="text-align: left;">
      <span style="color:darkcyan;font-size: 18px;">
        被关注{{ userData?.followCount || 0 }}
        分享{{ userData?.followCount || 0 }}
        评{{ userData?.commentCount || 0 }}
        顶{{ userData?.likeCount || 0 }}
        踩{{ userData?.dislikeCount || 0 }}
      </span>
    </el-row>
  </el-card>
  <el-card v-else style="width: 100%; height: auto;" shadow="always">
    <div style="text-align: center; padding: 20px;">加载中...</div>
  </el-card>
</template>

<script setup>
import { ref, computed } from 'vue';

const props = defineProps({
  userData: {
    type: Object,
    required: true,
    default: () => ({
      followCount: 1,
      shareCount: 1,
      commentCount: 1,
      likeCount: 1,
      dislikeCount: 1
    })
  },
  localUserId: {
    type: [String, Number],
    default: ''
  },
  defaultAvatarText: {
    type: String,
    default: '头像'
  }
});

const imageLoaded = ref(false);
const imageSrc = ref('http://aworld-1302616346.cos.ap-hongkong.myqcloud.com/static_pic/underconstruction_mob.jpg');

const isCurrentUser = computed(() => {
  return String(props.userData.item_id) === String(props.localUserId);
});

const loadImage = () => {
  imageLoaded.value = true;
};

const formatTime = (time) => {
  if (!time) return '未知时间';
  const now = new Date();
  const opDate = new Date(time);
  const timeDiff = now - opDate;
  const hoursDiff = Math.floor(timeDiff / (1000 * 60 * 60));
  const daysDiff = Math.floor(hoursDiff / 24);

  if (hoursDiff < 8) {
    return `${opDate.getHours()}:${opDate.getMinutes().toString().padStart(2, '0')}`;
  } else if (hoursDiff < 24) {
    return `${hoursDiff}小时前`;
  } else if (daysDiff < 30) {
    return `${daysDiff}天前`;
  } else {
    return opDate.toLocaleDateString();
  }
};
</script>

<style scoped>
.custom-image {
  height: auto;
  width: 100%;
  object-fit: cover;
  display: flex;
  align-items: center;
}

.ellipsis {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.default-avatar {
  width: 100px;
  height: 100px;
  background: #f0f0f0;
  border-radius: 50%;
  position: relative;
  margin: 0 auto;
}

.avatar-head {
  position: absolute;
  width: 40px;
  height: 40px;
  background: #d0d0d0;
  border-radius: 50%;
  top: 20%;
  left: 50%;
  transform: translateX(-50%);
}

.avatar-body {
  position: absolute;
  width: 60px;
  height: 40px;
  background: #d0d0d0;
  border-radius: 50% 50% 0 0;
  bottom: 10%;
  left: 50%;
  transform: translateX(-50%);
}

.avatar-text {
  position: absolute;
  width: 100%;
  text-align: center;
  color: gray;
  bottom: -10px;
  left: 0;
}

/* 覆盖 el-card 的默认内边距 */
:deep(.el-card__body) {
  padding: 10px;
}
</style> 