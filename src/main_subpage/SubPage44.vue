<template>
    <div class="subpage44">
        <el-row>
            <el-col :span="12">
                <el-card style="width: 100%; height: 300px;" shadow="always">
                    年度工作计划｜Annual work plan
                   <EmptyImage></EmptyImage> 
                </el-card>
            </el-col>
            <el-col :span="6">
                <el-card style="width: 100%; height: 150px;" shadow="always">
                担任公职
                </el-card>
                <el-card style="width: 100%; height: 150px;" shadow="always">
                投票选举
                </el-card>
            </el-col>
            <el-col :span="6">
                <el-card style="width: 100%; height: 300px;" shadow="always">
                今日任务
                </el-card>
            </el-col>
        </el-row>

        <el-row>
            <el-col :span="12">
                <el-card style="width: 100%; height: 150px;" shadow="always">福利清单</el-card>
                <el-card style="width: 100%; height: 150px;" shadow="always">休假</el-card>
            </el-col>

       
            <el-col :span="12">
                <!-- Content for the second column -->
                <el-card style="width: 100%; height: 300px;" shadow="always">所有生活和劳动的历史</el-card>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import EmptyImage from '@/components/EmptyImage.vue';

export default {
    name: 'SubPage44',
    // Your component options here
    components: {
        EmptyImage
    }
}
</script>

<style scoped>
.subpage44 {
    width: 100%;
    overflow-x: hidden;
    box-sizing: border-box;
}

.subpage44 :deep(.el-row) {
    margin-left: 0 !important;
    margin-right: 0 !important;
}

.subpage44 :deep(.el-col) {
    padding-left: 0 !important;
    padding-right: 0 !important;
}

</style>