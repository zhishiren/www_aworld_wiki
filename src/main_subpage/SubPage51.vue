<template>
    <div>
      <el-row class="firstrow">
      </el-row>
      这是上传文件的页面
    </div>
</template>
<script>
import { ref } from 'vue';
// import CreatenewRow from '../components/CreatenewRow.vue';

export default {
    name: 'SubPage51',
    components: {
        // CreatenewRow,

    },
    setup() {
   

        const value2 = ref('')



        return {
            value2,

        };



    },








}

</script>


<style scoped>
.my-date-picker .el-date-picker__input {  
  width: 200px;  
}  
</style>
