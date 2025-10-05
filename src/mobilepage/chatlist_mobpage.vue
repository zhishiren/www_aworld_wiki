<template>
    <div class="mobile-page" >
      <Topbar topbartitle="聊"></Topbar>
<!-- 默认页面是公开聊天室，在右上筛选中，可以选择用户，或者群组，
      可以加密发言，也可以匿名发言 -->
      <el-scrollbar>
      <router-link :to="{ name: 'chatroom_mobpage' }" class="chat-link">
        <div class="news-details"
            style="display: flex; align-items: flex-start; padding: 10px; border-bottom: 0.5px dotted grey;">
            <div style="flex: 0 0 auto; margin-right: 10px; display: flex; align-items: center; height: 100%;">
              <el-avatar :size="50" class="custom-avatar" shape="square" style="background-color: #000;">
                <div class="custom-icon" style="font-weight: bolder;font-size: 35px;">Ⓐ</div>
              </el-avatar>
            </div>
            <div style="flex: 1; text-align: left;">
              <div>
                <span style="font-size: 20px;font-weight: bold;">公共聊天室</span>
              </div>
              <div>
                <span>群聊</span><span style="color: gray;">｜1条未读</span>
              </div>
            </div>
          </div>
      </router-link>

      <router-link :to="{ name: 'chatroom_mobpage' }" class="chat-link">
        <div class="news-details"
            style="display: flex; align-items: flex-start; padding: 10px; border-bottom: 0.5px dotted grey;">
            <div style="flex: 0 0 auto; margin-right: 10px; display: flex; align-items: center; height: 100%;">
              <el-avatar :size="50" class="custom-avatar" shape="square" style="background-color: #000;">
                <div class="custom-icon" style="font-weight: bolder;font-size: 35px;">AI</div>
              </el-avatar>
            </div>
            <div style="flex: 1; text-align: left;">
              <div>
                <span style="font-size: 20px;font-weight: bold;">智能机器人</span>
              </div>
              <div>
                <span>单聊</span><span style="color: gray;">｜1条未读</span>
              </div>
            </div>
          </div>
      </router-link>
      <div style="height: 70px;"></div>
    </el-scrollbar>

    </div>
  </template>
  
  <script setup>
import Topbar from '../mobilecomponents/Topbar.vue';

  // 这里可以添加任何必要的逻辑
  </script>
  
  <style scoped>
  .chat-link {
    text-decoration: none;
    color: inherit;
  }

  .news-details:active {
    background-color: #f0f0f0;
  }
  </style>
  