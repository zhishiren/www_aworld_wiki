<template>
    <div>
      <el-carousel :interval="4000" type="card" height="200px">
          <el-carousel-item v-for="item in 6" :key="item">
            <h3 text="2xl" justify="center">{{ item }}</h3>
          </el-carousel-item>
        </el-carousel>
      <el-row class="firstrow">
        <Opline variant="create" :showprops="$options.name" />
      </el-row>
      这是上传文件的页面
    </div>
</template>
<script>
import { ref } from 'vue';
import Opline from '../components/Opline.vue';

export default {
    name: 'SubPage72',
    components: {
        Opline

    },
    setup() {
   

        const value2 = ref('')

        const items = ref([]);

        for (let i = 1; i <= 6; i++) {
          items.value.push(i);
        }


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




.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>
