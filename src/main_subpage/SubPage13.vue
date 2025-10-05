<template>  
    <div>  
    <p style="font-size: 18px;padding-top: 10px;text-align: left;">
      西撒总公社是由5个一级公社和50个二级公社组成。<a class="a_grey">Translate to English</a> 
    </p>
    <el-table :show-header="false" :data="tableData" style="width: 100%;font-size: 18px;">
      <el-table-column label="" width="auto">
        <template #default="scope">
          <el-row>
            <span v-if="scope.row.type==='二级公社'">········</span>
            <span>{{scope.row.name}}｜</span>
            <span>{{scope.row.type}}｜</span>
            <span>{{scope.row.address}}｜</span>
            <span>{{scope.row.nickname}}</span>
          </el-row>
        </template>
      </el-table-column>
    </el-table>
    </div>  
  </template>  
    
  <script>  
  import { ref} from 'vue';  
    
  export default {  
    name: 'SubPage12',  
    components: {  
    },  
    setup() {  
        const tableData = ref([

            {name: 'A10', address: '不放养宠物·内有监控·集中控枪',type:'一级公社'},
            {name: 'A11', address: '禁烟·不区分性别',type:'二级公社',nickname:'克鲁泡特金公社'  },
            {name: 'A13', address: '不禁烟·不区分性别',type:'二级公社'  },
            {name: 'A11', address: '禁烟·纯女性',type:'二级公社' },
            {name: 'A13', address: '不禁烟·纯女性',type:'二级公社'  },
            {name: 'A20', address: '不放养宠物·内有监控·自由持枪',type:'一级公社' },
            {name: 'A21', address: '禁烟·不区分性别',type:'二级公社'  },
            {name: 'A21', address: '禁烟·不区分性别',type:'二级公社'  },
            {name: 'A21', address: '禁烟·不区分性别',type:'二级公社'  },
            {name: 'A21', address: '禁烟·不区分性别',type:'二级公社'  },
  
            // 更多数据...  
        ]);
        return {
            tableData,
        };



    },  
  }  
  </script>  
    
  <style scoped>  
  /* 这里编写你的组件样式 */  
  </style>