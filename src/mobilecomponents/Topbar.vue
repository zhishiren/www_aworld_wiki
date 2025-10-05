<template>  
    <div class="top-bar">  
        <span @touchstart="navigate('/')"><a class="mainlinkstyle">首页</a>｜</span>
        <div>{{ topbartitle }}</div> 
        <span v-if="topbartitle!=='系统设置'">｜<a @click="showOptions" class="mainlinkstyle">筛选</a></span>
        <span v-if="topbartitle==='系统设置'">｜<a @click="showAlert" class="mainlinkstyle">高级</a></span>

      

        <el-dialog v-model="dialogVisible" title="提示" width="100%">
            <span>这是一段信息</span>
        </el-dialog>


    </div>  
</template>  
    
<script setup>  
    import { useRouter } from 'vue-router';  
    import { ref, onMounted } from 'vue';  
    import { ElMessage } from 'element-plus';
    const router = useRouter();  

// 定义一个prop来接收外部传入的新闻标题  
const props = defineProps({  
    topbartitle: {  
        type: String,  
        required: true,  
        default: '-'  
    }  
});  

const dialogVisible = ref(false);

// 这里需要根据不同的页面进行判断，显示不同的筛选选项。
const showOptions = () => {
    if (props.topbartitle === '朋友组织') {
        dialogVisible.value = true;
    } else {
        ElMessage.error('该功能尚未完成')
    } 
};



const showAlert = () => {



    ElMessage.error('该功能尚未完成')
};

// 定义导航函数
const navigate = (path) => {
    router.push(path);
};
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
  


.mainlinkstyle{
  color: grey;
  font-weight: bold;
  font-size: 6vw;
}
 
  /* .backbutton {
    font-size: 22px;
    cursor: pointer;
  } */
  
  
  </style>
  

