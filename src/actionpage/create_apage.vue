
<template>
    <div>
        <HelloLogout></HelloLogout>
        <br>
        <el-row style="width: 1060px;">
            <el-col :span="3"></el-col>
            <el-col :span="21" class="bgcolor_menu_FC" style="text-align: left;font-size: 20px;">
                <p>这是用户本人增添各类知识元素的页面。</p>
                <p>This is a page for users to add various knowledge elements by themselves.</p>
              
            </el-col>
        </el-row>

        <el-row style="width: 1060px;">
            <el-col :span="3">
                <el-menu :default-active=activeSubIndex0 class="el-menu-vertical-demo bgcolor_menu_FC"
                    @select="subhandleSelect0">

                    <el-menu-item index="01" class="menu-item18">
                        <span>我要发言</span>
                    </el-menu-item>
                    <el-menu-item index="02" class="menu-item18">
                        <span>主题标签</span>
                    </el-menu-item>
                    <el-menu-item index="03" class="menu-item18">
                        <span>文章标题</span>
                    </el-menu-item>
                    <el-menu-item index="04" class="menu-item18">
                        <span>独立段落</span>
                    </el-menu-item>
                    <el-menu-item index="05" class="menu-item18">
                        <span>站内群组</span>
                    </el-menu-item>
                    <el-menu-item index="06" class="menu-item18">
                        <span>辩论议题</span>
                    </el-menu-item>
                    <el-menu-item index="07" class="menu-item18">
                        <span>问答求教</span>
                    </el-menu-item>
                    <el-menu-item index="08" class="menu-item18">
                        <span>公共物品</span>
                    </el-menu-item>
                    <el-menu-item index="09" class="menu-item18">
                        <span>影音图集</span>
                    </el-menu-item>

                </el-menu>
            </el-col>

            <el-col :span="21" v-if="activeSubIndex0 === '01'">
                <el-row class="firstrow">
                    <Opline variant="create" :showprops="$options.name" propitemtype="发言" />
                </el-row>
            </el-col>
            <el-col :span="21" v-if="activeSubIndex0 === '02'">
                这是成员列表
            </el-col>
            <el-col :span="21" v-if="activeSubIndex0 === '03'">
                
                <el-row class="firstrow">
                    <Opline variant="create" :showprops="$options.name" propitemtype="文章" />
                </el-row>
            </el-col>
            <el-col :span="21" v-if="activeSubIndex0 === '04'">
                这里是其他用户可以对他采取的操作
            </el-col>
            <el-col :span="21" v-if="activeSubIndex0 === '05'">
                这里是其他用户可以对他采取的操作
            </el-col>
            <el-col :span="21" v-if="activeSubIndex0 === '06'">
                这里是其他用户可以对他采取的操作
            </el-col>
            <el-col :span="21" v-if="activeSubIndex0 === '07'">
                这里是其他用户可以对他采取的操作
            </el-col>

        </el-row>




    </div>
</template>

<script>import { ref, reactive } from 'vue';
import HelloLogout from '../components/HelloLogout.vue';
import Opline from '../components/Opline.vue';

export default {
    name: 'create_apage',
    components: {
        HelloLogout,
        Opline,

    },

    setup() {
        // do not use same name with ref
        const activeSubIndex0 = ref('01');
        const subhandleSelect0 = (index) => {
            activeSubIndex0.value = index;
        };
        const form = reactive({
            name: '',
            region: '',
            desc: '',
        })
        return {
            form,
            activeSubIndex0,
            subhandleSelect0,
        };

    },
}
</script>
