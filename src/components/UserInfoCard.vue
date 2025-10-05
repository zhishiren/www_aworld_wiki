<template>
    <el-card shadow="always" v-if="itemData?.item_type === '人物'">
        <el-row>
            <el-col :span="5"
                style="border: 1px dashed lightgrey; display: flex; justify-content: center; align-items: center;">
                <img src="https://z2024-1302616346.cos.ap-nanjing.myqcloud.com/NoData.jpg"
                    style="width: 100%; height: auto;">
            </el-col>
            <el-col :span="16">
                <el-descriptions title="" column="1" style="margin-left: 10px;">
                    <el-descriptions-item label="用户名称:">{{ itemData?.item_title }}</el-descriptions-item>
                    <el-descriptions-item label="类型与ID:">{{ itemData?.item_subtype }}｜{{ itemData?.item_id }}</el-descriptions-item>
                    <el-descriptions-item label="所在地区:">{{ itemData?.sparefield1 }}</el-descriptions-item>
                    <el-descriptions-item label="注册时间:">{{ itemData?.createtime }}</el-descriptions-item>
                    <el-descriptions-item label="上次登录:">ceshi</el-descriptions-item>
                    <el-descriptions-item label="联系方式:">{{ itemData?.sparefield2 }}</el-descriptions-item>
                    <el-descriptions-item label="数据统计:">欣赏10-鄙视1｜装逼说谎5</el-descriptions-item>
                    <el-descriptions-item label="自我介绍:">{{itemData?.item_content}}</el-descriptions-item>
                </el-descriptions>
            </el-col>
            <el-col :span="3">
                <span v-if="itemData?.item_id !== localUserId">
                    <el-button key="info" type="info" text class="custom-button">
                        <el-icon class="my-icon"><ChatLineSquare /></el-icon><span>与TA聊</span>
                    </el-button>
                </span>
                <span v-if="itemData?.item_id === localUserId">
                    <el-button key="info" type="info" text class="custom-button">
                        <el-icon class="my-icon"><Edit /></el-icon><span>改信息</span>
                    </el-button>
                </span>
                <span v-if="itemData?.item_id === localUserId">
                    <el-button key="info" type="info" text class="custom-button">
                    <el-icon class="my-icon"><Edit /></el-icon><span>写介绍</span></el-button>
                </span>

            </el-col>
        </el-row>
    </el-card>
</template>

<script setup>
import { ref } from 'vue';
import { Edit, ChatLineSquare } from '@element-plus/icons-vue'

defineProps({
    itemData: {
        type: Object,
        required: true
    }
});

const localUserId = ref(Number(localStorage.getItem('userid'))); 
</script>

<style scoped>
.my-icon {
    margin-right: 4px;
    vertical-align: middle;
}

.custom-button {
    padding: 4px 8px;
}

:deep(.el-descriptions__label) {
    font-size: 18px;
}

:deep(.el-descriptions__content) {
    font-size: 18px;
    color: grey;
}

:deep(.el-descriptions__cell) {
    padding-bottom: 0 !important;
}
</style> 