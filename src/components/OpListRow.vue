<!-- 
  这里的opspan组件，是用来展示用户的操作历史的,是个显示范围很大的组件，包括：
  
新闻动态--用户动态，用户+操作类型（分享，评论）+元素0+元素1(如有),附言:XXXXX。

元素被操作列表，被用户+操作类型+元素1(如有),附言:XXXXX

群内历史动态，用户+操作类型（分享评论发言）+元素0,附言:XXXXX。

我的历史动态：我-操作类型（分享+发言）+元素0，与元素1（如有）：附言：

用户历史动态：该用户-操作类型（分享+发言）+元素0，与元素1（如有）：附言：

新闻动态--互动信息: 用户+操作类型+你,关于。。。，附言：

元素关联列表：该元素关联了元素1，来自用户，附言：

标签包含列表：该标签内添加了元素0，附言：

群组列表：用户加入此群，附言：

新闻动态-内容动态：元素0+操作类型（关联+标签+评论）+元素1如有，来自用户，附言：

附言：（如果这是用户发言，则省略）   -->

<!-- 重要组件，与opspan组件配合使用 -->

<template>
    <div>
        <div v-for="op in paginatedData" :key="op.op_id" class="op-item" style="border:0px;border-bottom:0.5px solid #ccc;text-align: left;font-size:18px;padding-bottom:0px;">
            <el-row>
                <span v-if="showprops === '元素被操作列表'">
                    {{ op.item0type === '人物' ? '该用户信息被' : '该元素被' }}
                </span> 
                <span v-if="showprops !== '新闻动态-内容动态' && showprops!=='我的历史动态' && showprops!=='用户历史动态'">
                    <span v-if="op.userXid!==99999999"><router-link :to="{ name: 'DetailPage', params: { id: op.userXid } }" target="_blank" class="a_black">{{ op.userXname }}</router-link></span>
                    <span v-if="op.userXid===99999999" style="color:white;font-weight: bold;background-color: gray;">匿名者</span>
                </span>
                <span v-if="showprops==='我的历史动态'">我</span>
                <span v-if="showprops==='用户历史动态'">该用户</span>

                <span v-if="showprops !== '新闻动态-内容动态' && showprops !=='用户加群列表'">
                    <span>{{ op.op_type }}</span>
                    <span v-if="op.op_type!=='发言'">了</span>
                </span>

                <span v-if="showprops==='用户加群列表'">加入此群</span>

                <!-- 这里显示的是元素0的内容 -->
                <!-- 使用##���包裹标签，使用「」来包裹用户名或群组名，用【】来包裹重要事项如契约，投票，选举等-->
                <span v-if="showprops !=='元素关联列表' && showprops !=='用户加群列表' && op.op_type !=='发言'">
                    <router-link :to="{ name: 'DetailPage', params: { id: op.item0id } }" target="_blank" class="a_black">
                        <span v-if="op.item0type==='人物'||op.item0type==='群组'">「</span>
                        <span>{{ op.item0title }}</span>
                        <span v-if="op.item0type==='人物'||op.item0type==='群组'">」</span>
                    </router-link>
                </span>
                <span v-if="showprops ==='元素关联列表'">该元素</span>

                <span v-if="showprops === '新闻动态-内容动态'" style="color: grey;">
                    <span v-if="op.op_type==='关联'">关联了</span>
                    <span v-if="op.op_type==='加标签'">被添加入标签</span>
                    <!-- 这里要限定一些元素类型，比如要排除用户，而且要对关注的标签进行查找后与其他的合并去除重复，如果有特别关注，则可以加入更多的操作类型，如评论，纠错等。 -->
                </span>

                <span v-if="showprops !== '新闻动态-内容动态' && op.op_type ==='关联'">和</span>

                <!-- 这里显示的是元素1的内容 -->
                <span>
                    <router-link :to="{ name: 'DetailPage', params: { id: op.item1id } }" target="_blank" class="a_black">{{ op.item1title }}</router-link>
                </span>

                <span v-if="showprops === '新闻动态-内容动态'|| showprops === '元素关联列表'">
                    <span>来自</span>
                    <span v-if="op.userXid!==99999999"><router-link :to="{ name: 'DetailPage', params: { id: op.userXid } }" target="_blank" class="a_black">{{ op.userXname }}</router-link></span>
                    <span v-if="op.userXid===99999999" style="color:gray;font-weight: bold;">匿名者</span>
                </span>

                <span v-if="op.op_type !== '发言'&&op.ps_content">
                    <span><b>,</b>附言</span>
                    <span v-if="op.ps_content"><b>:</b></span>
                    <!-- <span v-if="!op.ps_content">无</span> -->
                </span>

                <span v-if="op.op_type === '发言'">
                    <span><b>：</b></span>
                </span>

                <span>
                    <router-link v-if="op.op_type==='发言' && op.ps_encrypted===0" :to="{ name: 'DetailPage', params: { id: op.item0id } }" target="_blank" class="a_brown"><span v-html="op.ps_content"></span></router-link>
                    <el-tooltip content="<h2>点击进入详情页以解密</h2>" raw-content placement="right">
                        <router-link v-if="op.op_type==='发言' && op.ps_encrypted!==0" :to="{ name: 'DetailPage', params: { id: op.item0id } }" target="_blank" class="a_brown"><span style="background-color: lightgray;color: brown;">{{ op.item0title }}</span></router-link>
                    </el-tooltip>
                    <router-link v-if="op.op_type!=='发言' && op.ps_encrypted===0" :to="{ name: 'PS_reply_page', params: { id: op.op_id } }" target="_blank" class="a_brown"><span v-html="op.ps_content"></span></router-link>
                    <el-tooltip content="<h2>点击进入详情页以解密</h2>" raw-content placement="right"> 
                        <router-link v-if="op.op_type!=='发言' && op.ps_encrypted!==0" :to="{ name: 'PS_reply_page', params: { id: op.op_id } }" target="_blank" class="a_brown"><span style="background-color: lightgray;color: brown;">{{ op.item0title }}</span></router-link>
                    </el-tooltip>
                    <!-- 这里是为了展示用户发言的内容，但没有使用ps_content，而是使用item0title，是因为ps_content可能很长，而item0title是ps_content的十个字的摘要。 -->
                    <!-- 这里点击之后到详情页，可以解密 ，显示一个提示-->
                </span>
                
            </el-row>

            <el-row style="display: flex; justify-content: space-between; padding-bottom: 0px;"> <!-- 使用 flexbox 进行左右对齐 -->
                <span style="display: flex; align-items: center;"> <!-- 垂直居中对齐 -->
                    <span style="text-align: left;">
                        <span v-if="op.op_range===99999999">所有人可见</span>
                        <span v-if="op.op_range===10000000">仅自己可见</span>
                        <span v-if="op.op_range!==10000000 && op.op_range!==99999999">群组<router-link :to="{ name: 'DetailPage', params: { id: op.op_range } }" target="_blank" class="a_black">{{op.op_range}}</router-link>内可见</span>
                    </span>
                    <span v-if="op.ps_type!==null">
                        <el-divider direction="vertical" />
                        <span>{{ op.ps_type }}</span>
                    </span>
                    <span v-if="showprops === '我的历史动态'">
                        <el-divider direction="vertical" />
                        <span>{{ op.op_status }}</span>
                    </span>
                </span>

                <span style="text-align: right;">
                    <span>回复<el-divider direction="vertical" /></span>
                    <span v-if="op.userXid === currentUserId">删<el-divider direction="vertical" /></span>
                    <span>{{ formatTime(op.op_time) }}</span>
                    </span>
            </el-row>
         
        </div>

        <el-pagination  
            v-if="oplist.length > 10"
            background
            @size-change="handleSizeChange"  
            @current-change="handleCurrentChange"  
            :current-page="currentPage"  
            :page-sizes="[10, 20, 30, 40]"  
            :page-size="pageSize"  
            layout="prev, pager, next"  
            :total="oplist.length">  
        </el-pagination>


    </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import axios from 'axios';
import { ElLoading } from 'element-plus';

const loadingInstance = ref(null); // 用于存储加载实例
const storedUserId = localStorage.getItem('userid') ?? '';
const currentUserId = storedUserId ? Number(storedUserId) : null;

const props = defineProps({
    showprops: {
        type: String,
        default: '111'
    },
    showList: {
        type: Boolean,
        default: false
    }
});

// 声明响应式变量  
const oplist = ref([]);

const currentPage = ref(1);
const pageSize = ref(10);

// 计算分页数据
const paginatedData = computed(() => {
    const start = (currentPage.value - 1) * pageSize.value;
    const end = start + pageSize.value;
    return oplist.value.slice(start, end);
});

// 处理每页大小变化
const handleSizeChange = (size) => {
    pageSize.value = size;
    currentPage.value = 1; // 重置到第一页
};

// 处理当前页变化
const handleCurrentChange = (page) => {
    currentPage.value = page;
};

const showLoading = () => {
    if (loadingInstance.value) {
        return;
    }
    loadingInstance.value = ElLoading.service({
        lock: true,
        text: '加载中...',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)',
    });
};

const hideLoading = () => {
    if (!loadingInstance.value) {
        return;
    }
    loadingInstance.value.close?.();
    loadingInstance.value = null;
};

const fetchData = async () => {
    showLoading();
    try {
        const payload = {
            user_id: storedUserId,
            op_type: props.showprops,
        };
        const response = await axios.post('https://www.aworld.wiki/api/opinfo/get_oplist/', payload);
        oplist.value = Array.isArray(response.data) ? response.data : [];
    } catch (error) {
        console.error('Failed to load operation list:', error);
        oplist.value = [];
    } finally {
        hideLoading();
    }
};

const formatTime = (op_time) => {
    const opDate = new Date(op_time);
    if (Number.isNaN(opDate.getTime())) {
        return '';
    }

    const diffMs = Date.now() - opDate.getTime();
    const hoursDiff = Math.floor(diffMs / (1000 * 60 * 60));

    if (hoursDiff < 8) {
        return `${opDate.getHours()}:${opDate.getMinutes().toString().padStart(2, '0')}`;
    }
    if (hoursDiff < 24) {
        return `${hoursDiff}小时前`;
    }

    const daysDiff = Math.floor(hoursDiff / 24);
    if (daysDiff < 30) {
        return `${daysDiff}天前`;
    }

    return opDate.toLocaleDateString();
};

// 将 fetchData 方法暴露给父组件
defineExpose({
    fetchList: fetchData,
});

// 监听 showList 的变化
watch(
    () => props.showList,
    (isVisible) => {
        if (isVisible) {
            fetchData();
        }
    },
    { immediate: true }
);

watch(
    () => props.showprops,
    () => {
        if (props.showList) {
            fetchData();
        }
    }
);

</script>

<style scoped>
.op-item {
    margin-bottom: 10px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}
</style>
