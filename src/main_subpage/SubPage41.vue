<template>
    <div style="margin: 10px;font-size: 20px;">
        <UserInfoCard :itemData="detailData" />

        <el-row class="firstrow">
            以下是可以设置用户登陆密码，用户头像，用户上传的图片等。 详情介绍，其中有用户的公告，图册，公职历史。
                这是用户的详细介绍，图片，担任职务， 这是用户的历史动态，还有群组中分享的新闻。
                详情介绍，其中有用户的公告，图册，公职历史。
                这是用户的详细介绍，图片，担任职务，
        </el-row>
    </div>
</template>

<script>
import { ref } from 'vue';
import UserInfoCard from '../components/UserInfoCard.vue'

export default {
    name: 'SubPage41',
    components: {
        UserInfoCard
    },
    setup() {
        const detailData = ref({
            item_type: '人物',
            item_title: 'ceshi',
            item_subtype: '注册用户',
            item_id: 10000047,
            sparefield1: '',
            sparefield2: '',
            createtime: '',
            item_content: '',
        });

        return {
            detailData
        };
    },
}
</script>