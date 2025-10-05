<template>
  <div class="mobile-page">
    <!-- 头部区域 -->
    <div class="top-bar">
      <span @touchstart="navigateTo"><a class="mainlinkstyle">返回</a>｜</span>
      <div style="font-size: 20px;"><b>公共聊天室</b></div>
    </div>
    <!-- 聊天消息列表 -->
    <el-scrollbar ref="scrollbarRef" class="chat-container">
      <div class="messages-container">
        <div v-for="(message, index) in messages" :key="index" 
             :class="['message-item', message.isSelf ? 'message-self' : 'message-other']">
          <div>
            <div class="message-header" :class="{ 'self-header': message.isSelf }">
              <div v-if="!message.isSelf" class="left-header">
                <el-avatar 
                  :size="30" 
                  class="message-avatar" 
                  :class="{ 'anonymous-avatar': message.username === '匿名者' }"
                  shape="square"
                >{{ message.username === '匿名者' ? '匿' : message.username.charAt(0) }}</el-avatar>
                <span class="username">{{ message.username }}</span>
              </div>
              <span class="time">{{ message.time }}</span>
              <div v-if="message.isSelf" class="right-header">
                <span class="username">{{ message.username }}</span>
              </div>
            </div>

            <div v-if="message.reply" class="message-reference" :class="{ 'self-reference': message.isSelf }">
              <span class="reference-text">回应@{{ message.ReplyWho}}:{{ message.ReplyWhat }}</span>
<!-- <span class="reference-text">{{ message.ReplyWhat }}</span> -->
            </div>

            <div class="message-content">
              <div v-if="message.attitude === 'against'" class="attitude">反对｜</div>
              <div v-if="message.encrypted > 0" class="encrypted-content">
                <span style="color: brown;">{{ message.encrypted }}字密文</span>
                <span>｜</span>
                <span style="color: darkgray;">点击解密</span>
              </div>
              <div v-else class="normal-content">{{ message.content }}</div>
            </div>

            <div v-if="message.reference" class="message-reference" :class="{ 'self-reference': message.isSelf }">
              <span class="reference-text">引用:{{ message.reference_itemtype }}-{{ message.reference_itemid }}</span>
              <span class="reference-text">{{ message.reference_itemcontent }}</span>
            </div>
          </div>
        </div>
      </div>
      <div style="height: 100px;">

      </div>
    </el-scrollbar>

    <el-drawer 
      v-model="dialogVisible" 
      size="50%" 
      direction="btt" 
      :with-header="false"
    >
      <el-row justify="space-between" style="font-size: 24px;">
        <span>发言<span class="dot">.</span><span class="dot">.</span><span class="dot">.</span></span>
        <span @click="dialogVisible = false">关闭</span>
      </el-row>
      <br>

      <el-row style="text-align: left;font-size: 20px;">
        <input
          v-model="messageForm.content"
          type="text"
          placeholder="请输入发言内容"
          class="input_dengluye"
          style="width: 100%; text-align: left;padding: 0px;"
          autocomplete="off"
        />
      </el-row>

      <el-row justify="space-between">
          <span>
            <el-checkbox 
              v-model="messageForm.encrypted" 
              label="加密" 
              size="large" 
            />
          </span>
          <span>
            <el-checkbox 
              v-model="messageForm.anonymous" 
              label="匿名" 
              size="large" 
            />
          </span>
          <span>
            <el-checkbox 
              v-model="messageForm.reference" 
              label="引用" 
              size="large" 
            />
          </span>
          <el-radio-group v-model="messageForm.attitude" class="attitude-group">
            <el-radio label="support" size="large">支持</el-radio>
            <el-radio label="against" size="large">反对</el-radio>
          </el-radio-group>
      </el-row>

      <el-row v-if="messageForm.reference" style="padding-bottom: 10px;">
        <input
          v-model="messageForm.referenceId"
          type="text"
          placeholder="请输入要引用的知识元素ID"
          class="input_dengluye"
          style="width: 100%;padding: 0px;color: darkgray;"
          autocomplete="off"
        />
      </el-row>

      <el-row v-if="messageForm.encrypted" style="padding-bottom: 10px;">
        <input
          v-model="messageForm.password"
          type="password"
          placeholder="请输入6位加密密码"
          class="input_dengluye"
          style="width: 100%;padding: 0px;color: darkgray;"
          autocomplete="new-password"
        />
        <input
          v-model="messageForm.passwordHint"
          type="text"
          placeholder="请输入密码提示"
          class="input_dengluye"
          style="width: 100%;padding: 0px;color: darkgray;"
          autocomplete="off"
        />
      </el-row>


      <el-row justify="center" style="font-size: 20px;">
        <span style="font-weight: bolder;" @click="submitMessage">发送</span>
      </el-row>





    </el-drawer>

    <!-- 移动到这里：底部操作栏，这是不需要分页-->
    <mob_opbar 
      fromwhere="m聊天页面"
      @post="openMessageDialog"
      @refresh3="refreshMessages"
      @scrollTop="scrollToTop"
      @scrollToBottom="scrollToBottom"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted, nextTick } from 'vue';
import Topbar from '../mobilecomponents/Topbar.vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import mob_opbar from '../mobilecomponents/mob_opbar.vue';

// 添加 scrollbarRef 的定义
const scrollbarRef = ref(null);

const onlineCount = ref(5);
const messages = ref([
  // 最早的消息
  {
    username: '张三',
    time: '10:01',
    content: '大家好，今天天气真不错！',
    isSelf: false,
    encrypted: 0,
    pswdhint: null,
    reference: null,
    attitude: 'neutral',
    ReplyWho: null,
    ReplyWhat: null,
    reference_itemtype: null,
    reference_itemid: null,
    reference_itemcontent: null,
    reply: false
  },
  {
    username: '我',
    time: '10:02',
    content: '是啊，适合出去走走',
    isSelf: true,
    encrypted: 0,
    reference: true,
    attitude: 'support',
    ReplyWho: '张三',
    ReplyWhat: '大家好',
    reference_itemtype: '段落',
    reference_itemid: '10000001',
    reference_itemcontent: '这是一段很长的引用内容，超出部分会被省略...',
    reply: true
  },
  {
    username: '我',
    time: '10:02',
    content: '是啊，适合出去走走',
    isSelf: true,
    encrypted: 0,
    reference: true,
    attitude: 'support',
    ReplyWho: '张三',
    ReplyWhat: '大家好',
    reference_itemtype: '段落',
    reference_itemid: '10000001',
    reference_itemcontent: '这是一段很长的引用内容，超出部分会被省略...',
    reply: true
  },
  // 中间的消息...
  {
    username: '张三',
    time: '10:05',
    content: '我们去公园吧',
    isSelf: false,
    encrypted: 0,
    pswdhint: null,
    reference: null,
    attitude: 'neutral',
    ReplyWho: null,
    ReplyWhat: null,
    reference_itemtype: null,
    reference_itemid: null,
    reference_itemcontent: null,
    reply: false
  },

  {
    username: '张三',
    time: '10:06',
    content: '我们去公园吧',
    isSelf: false,
    encrypted: 0,
    pswdhint: null,
    reference: null,
    attitude: 'neutral',
    ReplyWho: null,
    ReplyWhat: null,
    reference_itemtype: null,
    reference_itemid: null,
    reference_itemcontent: null,
    reply: false
  },

  {
    username: '张三',
    time: '10:07',
    content: '我们去公园吧',
    isSelf: false,
    encrypted: 0,
    pswdhint: null,
    reference: null,
    attitude: 'neutral',
    ReplyWho: null,
    ReplyWhat: null,
    reference_itemtype: null,
    reference_itemid: null,
    reference_itemcontent: null,
    reply: false
  },


  {
    username: '张三',
    time: '10:08',
    content: '我们去公园吧',
    isSelf: false,
    encrypted: 0,
    pswdhint: null,
    reference: null,
    attitude: 'neutral',
    ReplyWho: null,
    ReplyWhat: null,
    reference_itemtype: null,
    reference_itemid: null,
    reference_itemcontent: null,
    reply: false
  },
  {
    username: '张三',
    time: '10:09',
    content: '我们去公园吧',
    isSelf: false,
    encrypted: 0,
    pswdhint: null,
    reference: null,
    attitude: 'neutral',
    ReplyWho: null,
    ReplyWhat: null,
    reference_itemtype: null,
    reference_itemid: null,
    reference_itemcontent: null,
    reply: false
  },
  // 最新的消息
  {
    username: '匿名者',
    time: '10:10',
    content: 'ceshi',
    isSelf: false,
    encrypted: 9,
    pswdhint: 'ceshi5word',
    reference: true,
    attitude: 'neutral',
    ReplyWho: '张三',
    ReplyWhat: '大家好',
    reference_itemtype: '段落',
    reference_itemid: '10000001',
    reference_itemcontent: '这是一段很长的引用内容，超出部分会被省略...',
    reply: false
  }
]);
const dialogVisible = ref(false);
const messageForm = ref({
  content: '',
  encrypted: false,
  anonymous: false,
  attitude: '',
  reference: false,
  referenceId: '',
  password: '',
  passwordHint: ''
});

const router = useRouter();

const navigateTo = () => {
  router.go(-1);
};

// 打开发言对话框
const openMessageDialog = () => {
  dialogVisible.value = true;
};

// 修改滚动到底部的方法
const scrollToBottom = () => {
  if (scrollbarRef.value) {
    const scrollbar = scrollbarRef.value.$el.querySelector('.el-scrollbar__wrap');
    if (scrollbar) {
      scrollbar.scrollTop = scrollbar.scrollHeight;
    }
  }
};

// 修改刷新消息列表方法
const refreshMessages = async () => {
  try {
 
    const response = await axios.get('https://www.aworld.wiki/api/chat/messages/');
    if (Array.isArray(response.data)) {
      // 确保消息按时间顺序排序，最新的在最后
      messages.value = response.data.sort((a, b) => {
        return new Date(a.time) - new Date(b.time);
      });
      await nextTick(() => {
        scrollToBottom();
      });
    } else {
      console.error('Invalid response format:', response.data);
    }
  } catch (error) {
    console.error('获取消息失败:', error);
  }
};

// 修改提交消息方法
const submitMessage = async () => {
  try {
    // 构建提交数据
    const submitData = {
      ...messageForm.value,
      // 如果选择了引用，只发送 reference_itemid
      ...(messageForm.value.reference ? {
        reference_itemid: messageForm.value.referenceId
      } : {})
    };

    const response = await axios.post('https://www.aworld.wiki/api/chat/send_message/', submitData);
    
    if (response.data.success) {
      dialogVisible.value = false;
      await refreshMessages();
      // 重置表单
      messageForm.value = {
        content: '',
        encrypted: false,
        anonymous: false,
        attitude: '',
        reference: false,
        referenceId: '',
        password: '',
        passwordHint: ''
      };
    }
  } catch (error) {
    console.error('发送消息失败:', error);
  }
};

// 修改返回顶部方法
const scrollToTop = () => {
  if (scrollbarRef.value) {
    const scrollbar = scrollbarRef.value.$el.querySelector('.el-scrollbar__wrap');
    if (scrollbar) {
      scrollbar.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    }
  }
};

// 修改组件挂载时的初始化
onMounted(async () => {
  await refreshMessages();
  // 确保初始位置在底部
  nextTick(() => {
    scrollToBottom();
  });
});




const currentPage = ref(1);
const totalMessages = messages.value.length // 初始化为0
</script>

<style scoped>
.mobile-page {
  height: 100vh;
  /* display: flex;
  flex-direction: column; */
  overflow: hidden;
}

.messages-container {
  width: 100%;
  min-height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-end; /* 让内容从底部开始排列 */
}

.message-item {
  max-width: 80%;
  margin-bottom: 5px;
  /* 保留 float 布局 */
}

.message-self {
  float: right;
  margin-left: 20%;
}

.message-other {
  float: left;
  margin-right: 20%;
}

.message-header {
  display: flex;
  align-items: center;
  margin-bottom: 4px;
  padding: 0;
}

.self-header {
  justify-content: flex-end;
}

.message-avatar {
  margin: 0;
  font-size: 25px;
}

.username {
  font-weight: bold;
  font-size: 14px;
  color: #666;
}

.time {
  color: #999;
  font-size: 16px;
  margin: 0 8px;
}

.message-content {
  padding: 10px;
  border-radius: 12px;
  word-break: break-all;
  text-align: left;
  background-color: white;
  margin: 0 30px;
  border: 1px solid #eee;
}

.message-reference {
  font-size: 16px;
  color: #666;
  padding: 4px 8px;
  margin-top: 4px;
  background-color: rgba(0, 0, 0, 0.03);
  border-radius: 4px;
  text-align: left;
}

.self-reference {
  margin-left: 20%;
}

.message-other .message-reference {
  margin-right: 20%;
}

.reference-text {
  display: block;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.custom-avatar {
  display: flex;
  justify-content: center;
  align-items: center;
}

.custom-icon {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.attitude-tag {
  display: inline-block;
  padding: 2px 6px;
  border-radius: 4px;
  margin-right: 6px;
  font-size: 12px;
}

.attitude-support {
  color: #ff8c00;
}

.attitude-against {
  color: #ff8c00;
}

.anonymous-avatar {
  background-color: white !important;
  color: black !important;
  border: 1px solid #ddd;
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

.input_dengluye {
  border: none;
  border-bottom: 1px solid #dcdfe6;
  padding: 10px 0;
  font-size: 20px;
  width: 100%;
  margin-bottom: 10px;
}

.input_dengluye:focus {
  outline: none;
  border-bottom-color: #409eff;
}

:deep(.el-drawer__body) {
  padding: 20px;
}

.left-header {
  display: flex;
  align-items: center;
}

.right-header {
  display: flex;
  align-items: center;
  justify-content: flex-end;
}

.encrypted-content, .normal-content, .attitude {
  display: inline-block;
}

.message-content {
  display: flex;
  align-items: center;
  gap: 5px;
}

.chat-container {
  flex: 1;
  overflow: hidden;
  position: relative;
  height: calc(100vh - 150px); /* 减去头部和底部的高度 */
}

.dot {
  display: inline-block;
  animation: dotFlash 1.4s infinite;
  opacity: 0;
  color:black
}

.dot:nth-child(1) {
  animation-delay: 0s;
}

.dot:nth-child(2) {
  animation-delay: 0.2s;
}

.dot:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes dotFlash {
  0% { opacity: 0; }
  50% { opacity: 1; }
  100% { opacity: 0; }
}

.attitude-group {
  display: flex;
  gap: 5px;  /* 减小按钮之间的间距 */
}

:deep(.el-radio) {
  margin-right: 0;  /* 移除 Element Plus 的默认右边距 */
  padding: 0;  /* 移除内边距 */
}
</style>


