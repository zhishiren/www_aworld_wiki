<!-- 这里用作显示各种知识元素的列表-通用组件，例如在pc端的推荐阅读（推荐的段落内容），用户新增，用户搜索等。
 如果是推荐阅读，这里是系统自动推送的相关信息，在右下角可以有个选项，用户觉得是否精准相关：这样会记录
-->
<template>
    <div>
        <div v-for="item in itemlistData" :key="item.item_id" class="op-item"  style="border:0px;border-bottom:0.5px solid #ccc;text-align: left;font-size:18px;padding-bottom:0px;">
            <div v-if="item.item_type === '段落'">
                <el-row>
                    <router-link :to="{ name: 'DetailPage', params: { id: item.item_id } }" target="_blank" class="a_black">
                        <span style="font-size: 22px;font-weight: bold;text-align: left;">{{ item.sparefield1 }}</span>
                        <span style="font-size: 20px;color:gray;">{{ item.item_title }}</span>
                    </router-link>
                </el-row>
                <el-row class="ellipsis-row">
                    <span class="ellipsis-text">{{ item.item_subtype }}｜段落正文:{{ item.item_content }}</span>
                </el-row>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        itemlistData: {
            type: Array,
            required: true
        }
    }
}
</script>

<style scoped>
.ellipsis-row {
    width: 100%;
}

.ellipsis-text {
    display: block;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    width: 100%;
}

.op-item {
    margin-bottom: 10px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.a_black {
    text-decoration: none;
    color: inherit;
}

.a_black:hover {
    color: #409EFF;
}
</style>