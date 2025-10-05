<template>
    <div>
      <el-row style="height:270px">
        <el-col :span="24">
          <img src="https://z2024-1302616346.cos.ap-nanjing.myqcloud.com/sp65.jpg" class="bg_image"
            style="height:270px;width:100%;position: relative;" alt="">
          <div
            style="color:white;position: absolute; top: 10%; left: 50%; transform: translate(-50%, -50%); z-index: 1; text-align: center;font-size: 30px;">
            <br>
            极限行为艺术
            <br>
            NO BORDER 来去自由运动
          </div>
        </el-col>
      </el-row>
      <br>
  
    </div>
  </template>
  
  <script>
  // import { ref } from 'vue';
  
  // import { Comment } from 'vue-feather-icons';
  
  
  // import decrypting from '../components/decrypting_word.vue';  
  // import { reactive, toRefs } from 'vue';  
  // import { ElMessage } from 'element-plus';  
  // import axios from 'axios';  
  import { formatTimestamp } from '@/utils/myfunctions'; // 导入 formatTimestamp 函数
  
  export default {
    name: 'SubPage65',
    components: {
  
    },
    setup() {
      // 在 setup 函数中调用 formatTimestamp 函数
      const formattedTimestamp = formatTimestamp();
  
      return {
        formattedTimestamp
      };
    }
  }
  </script>