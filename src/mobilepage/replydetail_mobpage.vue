<template>
    <div class="mobile-page" >
        <div class="top-bar">  
          <!-- <span @touchstart="navigateTo"><a class="mainlinkstyle">返回</a>｜</span> -->
          <span><a class="mainlinkstyle">返回</a>｜</span>
          <!-- <div style="font-size: 20px;"><b>{{ subPageType }}</b></div>  -->
          <div style="font-size: 20px;">附言详情</div> 
        </div>  


    </div>
  </template>
  
  <script setup>
import Topbar from '../mobilecomponents/Topbar.vue';

  // 这里可以添加任何必要的逻辑
  </script>
  
  <style scoped>
 
  
 .top-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 5px 0;
    border-bottom: 2px solid #333;
    margin-bottom: 5px;
    font-size: 25px;
  }
  
  </style>
  