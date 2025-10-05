<template>
    <div class="mobile-page" >
      <Topbar topbartitle="系统设置"></Topbar>
        <!-- Collapse 折叠面板 -->
        <el-collapse v-model="activeName" accordion>
          <el-collapse-item title="主题背景" name="1">
            <div>
              测试，尚未完成。可以设置网站的主题和背景色。
            </div>
          </el-collapse-item>
          <el-collapse-item title="网络代理" name="2">
            <div>
              这里可以设置网络代理。
            </div>
           
          </el-collapse-item>
          <el-collapse-item title="账户隐私" name="3">

          </el-collapse-item>

        </el-collapse>



    </div>
  </template>
  
  <script setup>
import Topbar from '../mobilecomponents/Topbar.vue';

  // 这里可以添加任何必要的逻辑
  </script>
  
  <style scoped>
 
  
  </style>
  