<template>
    <div>
      <el-row class="firstrow">
        <Opline variant="create" :showprops="$options.name" />
      </el-row>
    </div>
</template>
<script>
import { ref } from 'vue';
import Opline from '../components/Opline.vue';

export default {
    name: 'SubPage05',
    components: {
        Opline

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
.firstrow {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 0;
  flex-wrap: wrap;
}

.my-date-picker .el-date-picker__input {  
  width: 200px;  
}  
</style>
