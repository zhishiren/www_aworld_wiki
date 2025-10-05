
<template>  
    <div>  
      <el-row class="firstrow">
        <!-- <Opline variant="create" :showprops='$options.name'></Opline> -->
      </el-row>
      <el-timeline style="max-width: 600px;text-align: left;font-size: 18px;padding-top: 10px;">  
            <el-timeline-item  
            v-for="(activity, index) in timelineData"  
            :key="index"  
            :timestamp="activity.timestamp"  
            :color="activity.color"
            >  

            {{ activity.action }}  :{{ activity.title }}
            </el-timeline-item>  
        </el-timeline>  
      <!-- 分页组件在这里可能不是必需的，除非您要在时间线上进行分页，这在常规情况下是不常见的 -->  
    </div>  
  </template>  
    
  <script>  
  import { ref, computed } from 'vue';  
    
  export default {  
    name: 'SubPage12',  
    components: {  
    },  
    setup() {  
      // 假设这是从后端API获取的原始时间线数据  
      const rawTimelineData = ref([  
              {action:'发起投票', date: '2023-04-02', name: '「西撒二级公社A001契约202401」', address: 'Address 2' },
              {action:'投票结果', date: '2023-04-02', name: 'Bob', address: 'Address 2' },
              {action:'发起选举', date: '2023-04-02', name: 'Bob1', address: 'Address 2' },
              {action:'选举结果', date: '2023-04-02', name: 'Bob1', address: 'Address 2' },
              {action:'发布契约', date: '2023-04-02', name: 'Bob1', address: 'Address 2' },
              {action:'发布通知', date: '2023-04-02', name: 'Bob1', address: 'Address 2' },
              {action:'紧急通知', date: '2023-04-02', name: 'Bob1', address: 'Address 2' },
              // 更多数据...  
      ]);  
    
      // 转换原始数据为时间线所需的数据结构  
      const timelineData = computed(() => {  
        return rawTimelineData.value.map((item) => { // 移除了未使用的 index 参数  
            if(item.action==='发起投票'){item.color='#FF7F00'}
            if(item.action==='发起选举'){item.color='#FF7F00'}
            if(item.action==='投票结果'){item.color='#0000FF'}
            if(item.action==='选举结果'){item.color='#0000FF'}
            if(item.action==='发布契约'){item.color='#D9D919'}
            if(item.action==='发布通知'){item.color='#8C7853'}
            if(item.action==='紧急通知'){item.color='#FF0000'}
            // 假设 date 字段是时间戳  
            return {  
            timestamp: new Date(item.date), // 将日期字符串转换为时间戳  
            action:item.action,
            title:item.name,
            color:item.color,
            };  
        });  
        });
    

    
      return {  
        timelineData,  
      };  
    },  
  };  
  </script>





  <style scoped>
  
  
  </style>
  
  
  
