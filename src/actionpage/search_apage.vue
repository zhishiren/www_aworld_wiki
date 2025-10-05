
<template>
    <div>
        <HelloLogout></HelloLogout>
        <br>
        <el-row style="width: 1060px;">
                <el-col :span="3"></el-col>
                <el-col :span="21" class="bgcolor_menu_FC" style="text-align: left;">
                    <input type="text" class="sousuolan" size="mini" v-model="sou_keyword" placeholder="请输入搜索关键词" style="font-size: 18px;">
                    <el-button key="info" type="info" text class="custom-button" style="font-size: 23px;color: black;">
                        <el-icon class="my-icon">
                            <Search />
                        </el-icon>搜
                    </el-button>
                    <p>
                        <span style="vertical-align: middle;"><el-icon><CaretRight /></el-icon></span>
                        历史搜索词:
                    </p>
                </el-col>
        </el-row>
        
        <el-row style="width: 1060px;">
            <el-col :span="3">
                <el-menu :default-active=activeSubIndex0 class="el-menu-vertical-demo bgcolor_menu_FC"
                    @select="subhandleSelect0">

                    <el-menu-item index="01" class="menu-item18">
                        <span>用户言论</span>
                    </el-menu-item>
                    <el-menu-item index="02" class="menu-item18">
                        <span>主题标签</span>
                    </el-menu-item>
                    <el-menu-item index="03" class="menu-item18">
                        <span>文章标题</span>
                    </el-menu-item>
                    <el-menu-item index="04" class="menu-item18">
                        <span>段落内容</span>
                    </el-menu-item>
                    <el-menu-item index="05" class="menu-item18">
                        <span>辩论问答</span>
                    </el-menu-item>
                    <el-menu-item index="06" class="menu-item18">
                        <span>公共物品</span>
                    </el-menu-item>


                </el-menu>
            </el-col>

            <el-col :span="21" v-if="activeSubIndex0 === '01'">
                <el-table :data="tableData" style="width: 100%;font-size: 18px;padding-top: 8px;">
                    <!-- <el-table-column :label="'优先展示前10条最新的用户言论'+ceshi" width=auto> -->
                    <el-table-column label="优先展示最新的10条用户言论" width=auto>
                        <template #default="scope">
                            <el-row>
                                <span v-if="scope.row.type==='二级公社'">········</span>
                                <span>{{scope.row.name}}｜</span>
                                <span>{{scope.row.type}}｜</span>
                                <span>{{scope.row.address}}｜</span>
                                <span>{{scope.row.nickname}}</span>
                            </el-row>
                        </template>
                    </el-table-column>
                </el-table>
            </el-col>
            <el-col :span="21" v-if="activeSubIndex0 === '02'">
                这是成员列表
            </el-col>
            <el-col :span="21" v-if="activeSubIndex0 === '03'">
                这里是其他用户可以对他采取的操作
            </el-col>
            <el-col :span="21" v-if="activeSubIndex0 === '04'">
                这里是其他用户可以对他采取的操作
            </el-col>
            <el-col :span="21" v-if="activeSubIndex0 === '05'">
                这里是其他用户可以对他采取的操作
            </el-col>

        </el-row>




    </div>
</template>

<script>import { ref, reactive } from 'vue';
import HelloLogout from '../components/HelloLogout.vue';

export default {
    name: 'search_apage',
    components: {
        HelloLogout,

    },

    setup() {
        // do not use same name with ref
        const activeSubIndex0 = ref('01');
        const subhandleSelect0 = (index) => {
            activeSubIndex0.value = index;
        };
        const ceshi=111;
        const form = reactive({
            name: '',
            region: '',
            desc: '',
        })
        return {
            form,
            activeSubIndex0,
            subhandleSelect0,
            ceshi
        };

    },
}
</script>
