<!-- 这里要设计四种按钮，提出论点，提供论据，反驳，补充论点，补充论据 -->
<template>
    <div>      
      <el-row class="firstrow">
        <Opline variant="create" :showprops="$options.name" />
      </el-row>


      <el-table :show-header="false" :data="tableData" style="font-size: 18px;">
        <el-table-column label="" width=auto>
          <template #default="scope">
                <div v-if="scope.row.action==='正方'" style="max-width: 600px;">
                  <p>三分钟前，{{scope.row.name}}:</p>
                  <span class="roundedspan1">{{scope.row.address}}#《What about “human nature”?》</span>
                  
                </div>          
                <div v-if="scope.row.action==='反方'" style="max-width: 600px;float:right;text-align: right;">
                  <p>三分钟前，{{scope.row.name}}:</p>
                  <span class="roundedspan2">{{scope.row.address}}</span>
                </div>      
          </template>
        </el-table-column>
      </el-table>

      <br>
      <br>
      <br>
    </div>
    
  
  </template>
  <script>  
  import Opline from '@/components/Opline.vue';

import { ref} from 'vue';  

  
  export default {  
    name: 'subpage_debate', 
    components: {  
      Opline,
      },  
    setup() {
        const tableData = [
            {action:'正方', date: '2023-04-01', name: 'Alice1', address: '正方正方正方正方正方正方正方正方正方正方正方正方正方正方正方正方正方正方正方正方正方正方正方正方' },
            {action:'反方', date: '2023-04-01', name: 'Alice', address: '反方反方反方反方反方反方反方反方反方反方反方反方反方反方反方反方反方' },
            {action:'反方', date: '2023-04-02', name: 'Bob', address: '中立中立中立中立中立中立中立中立中立中立中立中立' },
            {action:'正方', date: '2023-04-02', name: 'Bob', address: '中立中立中立中立中立中立中立中立中立中立中立中立' },
            {action:'正方', date: '2023-04-02', name: 'Bob', address: '中立中立中立中立中立中立中立中立中立中立中立中立中立' },
        ];
  
        return {
            tableData: ref(tableData),
        };
    },
  
  
  
  
  
  
  
  
  }
  
  </script> 
  
  
  <style scoped>
  
 
.roundedspan1 {  
  /* 使用背景色来模拟圆角效果 */  
  background-color: pink; /* 选择一个与Element Plus风格相符的颜色 */  
  /* 添加边框半径来创建圆角 */  
  border-radius: 10px; /* 根据需要调整圆角的大小 */  
  /* 添加一些内边距，使文本不会紧贴着边角 */  
  padding: 5px 10px;  
  /* 可以添加其他样式来增强效果，比如字体、颜色等 */  
  font-size: 14px;  
  color: #333;  
  /* 如果需要，还可以添加一些阴影效果来增强立体感 */  
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);  
  /* 确保文本在背景色块中垂直居中 */  
  display: inline-flex;  
  align-items: center;  
  justify-content: center;  
  /* 根据需要，可以添加过渡效果 */  
  transition: background-color 0.3s ease;  
}  

.roundedspan2 {  
  /* 使用背景色来模拟圆角效果 */  
  background-color:deepskyblue; /* 选择一个与Element Plus风格相符的颜色 */  
  /* 添加边框半径来创建圆角 */  
  border-radius: 10px; /* 根据需要调整圆角的大小 */  
  /* 添加一些内边距，使文本不会紧贴着边角 */  
  padding: 5px 10px;  
  /* 可以添加其他样式来增强效果，比如字体、颜色等 */  
  font-size: 14px;  
  color: #333;  
  /* 如果需要，还可以添加一些阴影效果来增强立体感 */  
  box-shadow: 0 1px 2px rgba(12, 232, 225, 0.1);  
  /* 确保文本在背景色块中垂直居中 */  
  display: inline-flex;  
  align-items: center;  
  justify-content: center;  
  /* 根据需要，可以添加过渡效果 */  
  transition: background-color 0.3s ease;  
}  

.roundedspan3 {  
  /* 使用背景色来模拟圆角效果 */  
  background-color: pink; /* 选择一个与Element Plus风格相符的颜色 */  
  /* 添加边框半径来创建圆角 */  
  border-radius: 10px; /* 根据需要调整圆角的大小 */  
  /* 添加一些内边距，使文本不会紧贴着边角 */  
  padding: 5px 10px;  
  /* 可以添加其他样式来增强效果，比如字体、颜色等 */  
  font-size: 14px;  
  color: #333;  
  /* 如果需要，还可以添加一些阴影效果来增强立体感 */  
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);  
  /* 确保文本在背景色块中垂直居中 */  
  display: inline-flex;  
  align-items: center;  
  justify-content: center;  
  /* 根据需要，可以添加过渡效果 */  
  transition: background-color 0.3s ease;  
}  
  
  
  
  </style>
  
  
  
