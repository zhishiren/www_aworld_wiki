<template>
    <div>
      <el-table :show-header="false" :data="tableData" style="width: 100%;font-size: 18px;" >
        <el-table-column label="" width=auto>
          <template #default="scope">
            <div v-show="scope.row.action==='回复'">
              <el-row>
                <span>{{scope.row.name}}回复说:<span style="color: darkblue;">ceshiceshiceshi。</span></span>
                <span style="color: grey;"><b>@你</b>分享《测试》的附言<b>:</b><a class="a_grey">测试测试测试测试。</a></span>
              </el-row>
              <el-row style="display: flex; justify-content: space-between;">
                  <span>异议反对<el-divider direction="vertical" />仅本人可见</span>
                <span>
                  <span><a class="a_grey">回复</a><el-divider direction="vertical" /></span>
                  <span><a class="a_grey">顶</a><el-divider direction="vertical" /></span>
                  <span><a class="a_grey">踩</a><el-divider direction="vertical" /></span>
                  <span>3分钟前</span>
                </span>
              </el-row>
            </div>

            <div v-show="scope.row.action==='关注'">
                <span>{{scope.row.name}}关注了你</span>
                <el-row style="display: flex; justify-content: space-between;">
                  <span>所有人可见</span>
                    <span>3分钟前</span>
                 
                </el-row>
            </div>

            <div v-show="scope.row.action==='屏蔽'">
              <el-row>
                <span>{{scope.row.name}}公开屏蔽了你，并说:<span style="color: darkblue;">ceshiceshiceshi。</span></span>
              </el-row>
              <el-row  style="display: flex; justify-content: space-between;">
                <span>所有人可见</span>
                  <span>3分钟前</span>
              </el-row>
            </div>

            <div v-show="scope.row.action==='评价'">
              <el-row>
                <span>{{scope.row.name}}评价你说:<span style="color: darkblue;">ceshiceshiceshi。</span></span>
              </el-row>
              <el-row  style="display: flex; justify-content: space-between;">
                  <span>大聪明<el-divider direction="vertical" />所有人可见</span>
                <span>
                  <span><a class="a_grey">回复</a><el-divider direction="vertical" /></span>
                  <span><a class="a_grey">顶</a><el-divider direction="vertical" /></span>
                  <span><a class="a_grey">踩</a><el-divider direction="vertical" /></span>
                  <span>3分钟前</span>
                </span>
              </el-row>
            </div>

          </template>
        </el-table-column>
      </el-table>
  
    </div>
    
  
  </template>
  <script>  
import { ref} from 'vue';  

  
  export default {  
    name: 'SubPage04', 
    setup() {
          const tableData = ref([
            {action:'回复', date: '2023-04-02', name: 'Bob', address: 'Address 2' },
            {action:'屏蔽', date: '2023-04-02', name: 'Bob', address: 'Address 2' },
            {action:'关注', date: '2023-04-02', name: 'Bob1', address: 'Address 2' },
            {action:'评价', date: '2023-04-02', name: 'Bob1', address: 'Address 2' },

          ]);
  
  
  
  
          return {
              tableData,
  
          };
  
  
  
      },
  
  
  
  
  
  
  
  
  }
  
  </script> 
  
  
  <style scoped>
  
  
   
  
  
  </style>
  
  
  
