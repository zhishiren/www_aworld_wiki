<!-- 这里显示公开范围｜状态｜删除｜顶｜踩｜回复，点击回复之后，跳转到附言详情页，状态和删除两个点只有在用户新增页面显示。 -->
<!-- 第一层是元素，第二层是附言，第三层是回复，第四层是回应 -->
<!-- 当回复时候，item0是附言id，item1为原附言用户id和title， -->
<!-- 如果是回应，item0是回复ID，item1为原回复用户的id和title -->
 <!-- 在互动信息中显示别人回应和回复我的内容，并且可以在其中筛选。 -->
<!-- 这里是各种的附言的信息，关注，分享，关联，加标签，等 -->
<template>
    <div>
        <HelloLogout></HelloLogout>
        <br>
        <el-row>
            <el-col :span="3"></el-col>
            <el-col :span="18">
                    <el-card shadow="always">
    
                        <el-row class="font20px" style="margin-bottom:5px;">
                            zhao关联了
                            <el-text class="truncated" >《Squeezed ddd 测试的长度 很长vvvvvvvvv》</el-text>
                            <span>和</span>
                            <el-text class="truncated" >《Squeezed by parent element vvvvvvvvvvvvv》</el-text>
                            <span style="color: grey;font-weight: bold;">附言:</span>
                        </el-row>

                  
                        <el-descriptions title="" column="1"  style="margin-bottom:5px;" >
                            <el-descriptions-item label="" >
                                <span class="font30px">“</span>
                                <span
                                    style="background-color:lightgrey;font-weight: bold;font-size: 24px;color: brown;">11字密文测试测试测11字密文测试测试测试11字密文11字密文测试测试测试测试测试测试试</span>
                                <span class="font30px">”</span>
                                <span>点击解密</span>
                            </el-descriptions-item>
                        </el-descriptions>
                  
                        
                        <el-descriptions title="" column="4">
                            <el-descriptions-item label="属性分类:">重要通知</el-descriptions-item>
                            <el-descriptions-item label="目前状态:">正常有效</el-descriptions-item>
                            <el-descriptions-item label="公开范围:">所有人</el-descriptions-item>
                            <el-descriptions-item label="发言时间:">20231201-12:01</el-descriptions-item>
                        </el-descriptions>
                    </el-card>

            </el-col>
            <el-col :span="3">

            </el-col>
        </el-row>

        <el-row style="width: 1200px;">
            <el-col :span="3">
                
            </el-col>

            <el-col :span="21" v-if="activeSubIndex0 === '01'">
                <el-row class="firstrow">关注|纠错｜举报｜顶｜踩</el-row>
                <el-row class="firstrow">该条附言有三条回复。刷新</el-row>
                <el-row class="firstrow">zhao回复了。</el-row>
                <el-row class="firstrow">zhao回应了kkk。</el-row>

            </el-col>


        </el-row>

    </div>
</template>

<script>

import { ref, onMounted } from 'vue';  
import axios from 'axios';
import { useRoute } from 'vue-router';  
import HelloLogout from '../components/HelloLogout.vue';
// import OperationRow from '../components/OperationRow.vue';
import Subpage_debate from '../detail_subpage/Subpage_debate.vue';




export default {
    name: 'DetailPage',
    components: {
        HelloLogout,
        // OperationRow,
        Subpage_debate
    },


    setup() {

        const detailData = ref(null)  
        const route = useRoute()  
        
        onMounted(async () => {  
            try {  
                const { id } = route.params;  
                const response = await axios.post('https://www.aworld.wiki/api/iteminfo/show_all_iteminfo/' ,{ id: id });  
                detailData.value = response.data;  
            } catch (error) {  
                console.error('Failed to fetch data:', error);  
            }  
        });


        const showCarousel = ref(false);  
        // Check if the name exists on the server  
        const imageUrls = ref([
            'https://z2024-1302616346.cos.ap-nanjing.myqcloud.com/10000001kk.jpg',
            'https://z2024-1302616346.cos.ap-nanjing.myqcloud.com/10000001er.jpg',
            'https://z2024-1302616346.cos.ap-nanjing.myqcloud.com/10000001%E6%AD%A3%E9%9D%A2.jpg'
        ]);




        const activeSubIndex0 = ref('01');
        const subhandleSelect0 = (index) => {
            activeSubIndex0.value = index;
        };

        return {

            activeSubIndex0,
            subhandleSelect0,
            imageUrls,
            showCarousel,
            detailData,


            // id,



        };
    },
};  
</script>

<style scoped>
.login {
    width: 1280px;
    margin: 0 auto;
}

.header {
    width: 1280px;
    background-color: #708090;
    ;
    height: 40px;
    color: white;
    font-size: 40px;
    line-height: 40px;
    text-align: left;
    padding: 0;
}



.menu-item {
    font-size: 20px;
    color: gray !important;
}

.menu-item18 {
    font-size: 18px;
    /* color: gray !important; */
    text-align: center;
}

.el-menu-vertical-demo {
    border-right: none !important;
}

.aside-left {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    justify-content: space-between;
    width: 120px;
    height: 450px;

}

.font30px {
    font-size: 45px;
    font-family: 'Microsoft YaHei';
    font-weight: bolder;
    vertical-align: -20px;
}

.flat-button {
    margin-bottom: 0px !important;
    padding: 15px;
    height: 56px;
    border: none;
    border-radius: 4px;
    background-color: #fff;
    color: #666;
    font-size: 25px;
    cursor: pointer;
}

.flat-button:hover {
    background-color: #f2f2f2;
}

::v-deep .el-descriptions__label {
    font-size: 18px;

}

::v-deep .el-descriptions__content {
    font-size: 18px;
    color: grey;
}

::v-deep .el-descriptions__cell {
    padding-bottom: 0 !important;
    /* 或需要调整padding来去除间距 */
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



.el-text.truncated {  
  display: inline-block; /* 或者 block，根据你的布局需要 */  
  white-space: nowrap;  
  overflow: hidden;  
  text-overflow: ellipsis;  
  max-width: 300px; /* 或者具体的宽度值，如 150px */  
  font-size: 20px;
}




</style>
