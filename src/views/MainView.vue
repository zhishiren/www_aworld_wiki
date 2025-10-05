<template>
  <div class="login">
   
    <HelloLogout></HelloLogout>
    <el-menu
      :default-active="activeIndex"
      class="el-menu-demo top-menu"
      mode="horizontal"
      :ellipsis="false"
      @select="handleSelect"
    >
      <el-menu-item
        v-for="item in topMenuItems"
        :key="item.index"
        :index="item.index"
        class="menu-item"
      >
        {{ item.label }}
      </el-menu-item>
    </el-menu>

    <el-container>
      <el-main class="main-area">
        <el-row class="section-row" v-if="activeIndex === '0'">
          <el-col :span="3">
            <el-menu
              :default-active="activeSubIndices['0']"
              class="el-menu-vertical-demo bgcolor_menu_FC"
              @select="(index) => handleSubSelect('0', index)"
            >
              <el-menu-item
                v-for="item in subMenuItems['0']"
                :key="item.index"
                :index="item.index"
                class="menu-item18"
              >
                <span>{{ item.label }}</span>
              </el-menu-item>
            </el-menu>
          </el-col>

          <el-col :span="21" v-show="activeSubIndices['0'] === '01'">
            <SubPage01></SubPage01>
          </el-col>
          <el-col :span="21" v-show="activeSubIndices['0'] === '02'">
            <!-- 这里修改为SubPage02，形式见SubPage01 -->
             <SubPage02></SubPage02>
          </el-col>
          <el-col :span="21" v-show="activeSubIndices['0'] === '03'">
            <SubPage03></SubPage03>
             <!-- <SubPage04></SubPage04> -->

          </el-col>
          <el-col :span="21" v-if="activeSubIndices['0'] === '04'">
            <!-- <SubPage03></SubPage03> -->
            这里有其他用户回复和回应的信息，也有其他用户纠错和加入群组（本人为管理员）的信息
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['0'] === '06'">
            <EmptyImage></EmptyImage>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['0'] === '05'">
            <SubPage05></SubPage05>
          </el-col>
        </el-row>

        <el-row class="section-row" v-if="activeIndex === '1'">
          <el-col :span="3">
            <el-menu
              :default-active="activeSubIndices['1']"
              class="el-menu-vertical-demo bgcolor_menu_FC"
              @select="(index) => handleSubSelect('1', index)"
            >
              <el-menu-item
                v-for="item in subMenuItems['1']"
                :key="item.index"
                :index="item.index"
                class="menu-item18"
              >
                <span>{{ item.label }}</span>
              </el-menu-item>
            </el-menu>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['1'] === '11'">
            <SubPage11></SubPage11>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['1'] === '12'">
            <SubPage12></SubPage12>
          </el-col>

          <el-col :span="21" v-if="activeSubIndices['1'] === '13'">
            <SubPage13></SubPage13>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['1'] === '14'">
            这里使用SubPage_teamorusers的组件。
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['1'] === '15'">
            <EmptyImage></EmptyImage>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['1'] === '16'">
            这里使用SubPage_teamorusers的组件。
          </el-col>

        </el-row>


        <el-row class="section-row" v-if="activeIndex === '2'">
          <el-col :span="3">
            <el-menu
              :default-active="activeSubIndices['2']"
              class="el-menu-vertical-demo bgcolor_menu_FC"
              @select="(index) => handleSubSelect('2', index)"
            >
              <el-menu-item
                v-for="item in subMenuItems['2']"
                :key="item.index"
                :index="item.index"
                class="menu-item18"
              >
                <span>{{ item.label }}</span>
              </el-menu-item>
            </el-menu>
          </el-col>
          <!-- 
          <el-col :span="21" v-if="activeSubIndices['2'] === '21'">
          </el-col> -->
          <el-col :span="21" v-if="activeSubIndices['2'] === '22'">
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['2'] === '23'">
            这是协会列表
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['2'] === '24'">
            这是所有的公社成员信息
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['2'] === '25'">
            这是你的任务列表
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['2'] === '26'">
            这是你的任务列表
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['2'] === '27'">
            这是你的任务列表
          </el-col>
        </el-row>

        <el-row class="section-row" v-if="activeIndex === '3'">
          <el-col :span="3">
            <el-menu
              :default-active="activeSubIndices['3']"
              class="el-menu-vertical-demo bgcolor_menu_FC"
              @select="(index) => handleSubSelect('3', index)"
            >
              <el-menu-item
                v-for="item in subMenuItems['3']"
                :key="item.index"
                :index="item.index"
                class="menu-item18"
              >
                <span>{{ item.label }}</span>
              </el-menu-item>
            </el-menu>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['3'] === '32'">
            <SubPage3X itemType="文章"></SubPage3X>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['3'] === '33'">
            <SubPage3X itemType="段落"></SubPage3X>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['3'] === '31'">
            <SubPage3X itemType="标签"></SubPage3X>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['3'] === '34'">
            <SubPage3X itemType="发言"></SubPage3X>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['3'] === '35'">
            <SubPage3X itemType="人物"></SubPage3X>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['3'] === '36'">
            <SubPage3X itemType="群组"></SubPage3X>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['3'] === '37'">
            <SubPage3X itemType="问辩"></SubPage3X>
          </el-col>
        </el-row>

        <el-row class="section-row" v-if="activeIndex === '4'">
          <el-col :span="3">
            <el-menu
              :default-active="activeSubIndices['4']"
              class="el-menu-vertical-demo bgcolor_menu_FC"
              @select="(index) => handleSubSelect('4', index)"
            >
              <el-menu-item
                v-for="item in subMenuItems['4']"
                :key="item.index"
                :index="item.index"
                class="menu-item18"
              >
                <span>{{ item.label }}</span>
              </el-menu-item>
            </el-menu>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['4'] === '41'">
            <!-- 这是含有我头像的页面，与detailpage中的用户信息设计类似，最后设计。这里可以设置我的头像，更改我的登录密码，匿名加密密码(一个月换一次)，
            这里发言密码，创建也可以修改，给一个十个字的提示词。每一次发布密闻，都需要输入一次密码，同时填写密码提示语言。
            在这里显示我的密码提示语和操作类型和时间。 -->
            <SubPage41></SubPage41>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['4'] === '42'">
            <SubPage42></SubPage42>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['4'] === '43'">
            <SubPage43></SubPage43>
            这里是我的历史动态，
          </el-col>

          <el-col :span="21" v-if="activeSubIndices['4'] === '44'">
           <SubPage44></SubPage44>
          </el-col>
      
        </el-row>

        <el-row class="section-row" v-if="activeIndex === '5'">
          <el-col :span="3">
            <el-menu
              :default-active="activeSubIndices['5']"
              class="el-menu-vertical-demo bgcolor_menu_FC"
              @select="(index) => handleSubSelect('5', index)"
            >
              <el-menu-item
                v-for="item in subMenuItems['5']"
                :key="item.index"
                :index="item.index"
                class="menu-item18"
              >
                <span>{{ item.label }}</span>
              </el-menu-item>
            </el-menu>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['5'] === '51'">
            <SubPage51></SubPage51>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['5'] === '52'">
            <EmptyImage></EmptyImage>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['5'] === '53'">
            <EmptyImage></EmptyImage>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['5'] === '54'">
            <EmptyImage></EmptyImage>
          </el-col>

          <el-col :span="21" v-if="activeSubIndices['5'] === '55'">
            这是是生产各类生活必需品的生产计划，包含维生素蛋白质食品、内衣、工装、卫生巾等。
          </el-col>
        </el-row>


        <el-row class="section-row" v-if="activeIndex === '6'">
          <el-col :span="3">
            <el-menu
              :default-active="activeSubIndices['6']"
              class="el-menu-vertical-demo bgcolor_menu_FC"
              @select="(index) => handleSubSelect('6', index)"
            >
              <el-menu-item
                v-for="item in subMenuItems['6']"
                :key="item.index"
                :index="item.index"
                class="menu-item18"
              >
                <span>{{ item.label }}</span>
              </el-menu-item>
            </el-menu>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['6'] === '61'">
            <SubPage61></SubPage61>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['6'] === '62'">
            <SubPage62></SubPage62>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['6'] === '63'">
            <SubPage63></SubPage63>
          </el-col>
          <!-- <el-col :span="21" v-if="activeSubIndices['6'] === '65'">
            <SubPage65></SubPage65>
          </el-col> -->
          <el-col :span="21" v-if="activeSubIndices['6'] === '64'">
            <SubPage64></SubPage64>


          </el-col>
        </el-row>

        <el-row class="section-row" v-if="activeIndex === '7'">
          <el-col :span="3">
            <el-menu
              :default-active="activeSubIndices['7']"
              class="el-menu-vertical-demo bgcolor_menu_FC"
              @select="(index) => handleSubSelect('7', index)"
            >
              <el-menu-item
                v-for="item in subMenuItems['7']"
                :key="item.index"
                :index="item.index"
                class="menu-item18"
              >
                <span>{{ item.label }}</span>
              </el-menu-item>
            </el-menu>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['7'] === '71'">
            <SubPage71></SubPage71>
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['7'] === '72'">
            本项目旨在建立一个在某匪帮倒台之后，对其麾下的权贵资本与恶棍走狗进行全球追讨的信息共享网站。特别说明：我说的某匪帮可以理解为民进党，请不要恶意联想。
          </el-col>
          <el-col :span="21" v-if="activeSubIndices['7'] === '73'">
            这是协会列表
          </el-col>

          <el-col :span="21" v-if="activeSubIndices['7'] === '74'">
            这是74
          </el-col>

          <el-col :span="21" v-if="activeSubIndices['7'] === '75'">
            这是75
          </el-col>

          <el-col :span="21" v-if="activeSubIndices['7'] === '76'">
            这是
          </el-col>
        </el-row>




      </el-main>


      <el-aside class="aside-left">
          <el-button class="flat-button">
            <router-link :to="{ name: 'create_apage' }" target="_blank" class="grey-link" style="text-decoration: none;">增</router-link>
          </el-button>
        <el-button class="flat-button">
          <router-link :to="{ name: 'search_apage' }" target="_blank" class="grey-link" style="text-decoration: none;">搜</router-link>
        </el-button>
        <el-button class="flat-button">
          <router-link :to="{ name: 'chat_apage' }" target="_blank" class="grey-link" style="text-decoration: none;">聊</router-link>
        </el-button>
        <el-button class="flat-button">
          <router-link :to="{ name: 'ai_apage' }" target="_blank" class="grey-link" style="text-decoration: none;">AI</router-link>
        </el-button>
        <el-button class="flat-button">
          <router-link :to="{ name: 'ai_apage' }" target="_blank" class="grey-link" style="text-decoration: none;">
          <span style="font-size: 20px;">En</span>
          </router-link>
        </el-button>
      </el-aside>
    </el-container>
    <el-dialog
      v-model="dialogVisible"
      title=""
      :modal="true"
      :close-on-click-modal="false"
      :lock-scroll="true"
      class="login-dialog"
      width="500px"
    >
        <el-row class="custom-background">
          <el-col :span="8">

          </el-col>
          <el-col :span="16">
            <br>
            <h2>登录Login</h2>
            <el-form ref="loginform" v-model="loginForm">
              <br>
              <input 
                autocomplete="off" 
                type="text" 
                placeholder="你的用户名,your username" 
                v-model="loginForm.username"
                class="input_dengluye">
              <br><br><br>
              <input 
                type="password" 
                placeholder="你的密码,your password" 
                v-model="loginForm.password"
                class="input_dengluye">
              <br>
            </el-form>
            <br>
            <h2><a class="a_grey" @click="handleLogin">确定Confirm</a></h2>
            <br>
            <br>
            <br>
          
            <h3>注册,to register</h3>
            <br>
            <h3>找回密码,Reset Password</h3>
            <br>


          </el-col>
        </el-row>
    </el-dialog>


  </div>
</template>

<script>

import { ref, onMounted, reactive  } from 'vue';
// import { ElMenu, ElMenuItem } from 'element-plus';  
// import 'element-plus/lib/theme-chalk/index.css';  
import HelloLogout from '../components/HelloLogout.vue';
import EmptyImage from '../components/EmptyImage.vue';

import SubPage65 from '../main_subpage/SubPage65.vue';
import SubPage64 from '../main_subpage/SubPage64.vue';
import SubPage63 from '../main_subpage/SubPage63.vue';
import SubPage62 from '../main_subpage/SubPage62.vue';
import SubPage61 from '../main_subpage/SubPage61.vue';
import SubPage01 from '../main_subpage/SubPage01.vue';
import SubPage02 from '../main_subpage/SubPage02.vue';
import SubPage03 from '../main_subpage/SubPage03.vue';
import SubPage05 from '../main_subpage/SubPage05.vue';
import SubPage11 from '../main_subpage/SubPage11.vue';
import SubPage12 from '../main_subpage/SubPage12.vue';
import SubPage13 from '../main_subpage/SubPage13.vue';
import SubPage3X from '../main_subpage/SubPage3X.vue';
import SubPage44 from '../main_subpage/SubPage44.vue';
import SubPage42 from '../main_subpage/SubPage42.vue';
import SubPage43 from '../main_subpage/SubPage43.vue';
import SubPage41 from '../main_subpage/SubPage41.vue';
import SubPage51 from '../main_subpage/SubPage51.vue';
import SubPage71 from '../main_subpage/SubPage71.vue';
import axios from 'axios'

const topMenuItems = [
  { index: '0', label: '新闻动态', defaultSub: '01' },
  { index: '1', label: '公共事务', defaultSub: '16' },
  { index: '2', label: '朋友组织', defaultSub: '22' },
  { index: '3', label: '关注收藏', defaultSub: '31' },
  { index: '4', label: '我的主页', defaultSub: '41' },
  { index: '5', label: '共享资源', defaultSub: '51' },
  { index: '6', label: '本站介绍', defaultSub: '64' },
  { index: '7', label: '安批百科', defaultSub: '71' },
];

const subMenuItems = {
  '0': [
    { index: '01', label: '用户动态' },
    { index: '02', label: '内容动态' },
    { index: '03', label: '推荐阅读' },
    { index: '04', label: '互动信息' },
    { index: '06', label: '系统通知' },
    { index: '05', label: '历史动态' },
  ],
  '1': [
    { index: '16', label: '创建组织' },
    { index: '12', label: '公议事项' },
    { index: '13', label: '组织架构' },
    { index: '14', label: '组织成员' },
    { index: '15', label: '任务列表' },
    { index: '11', label: '西撒公社' },
  ],
  '2': [
    { index: '21', label: '我的群组' },
    { index: '22', label: '我关注的' },
    { index: '23', label: '注册用户' },
    { index: '24', label: '站内群组' },
    { index: '25', label: '现实人物' },
    { index: '26', label: '历史名人' },
    { index: '27', label: '现实团体' },
  ],
  '3': [
    { index: '31', label: '标签主题' },
    { index: '32', label: '文章标题' },
    { index: '33', label: '段落内容' },
    { index: '34', label: '用户言论' },
    { index: '35', label: '人物朋友' },
    { index: '36', label: '团体群组' },
    { index: '37', label: '问答辩论' },
  ],
  '4': [
    { index: '41', label: '我的信息' },
    { index: '42', label: '公众评价' },
    { index: '43', label: '历史动态' },
    { index: '44', label: '事务清单' },
  ],
  '5': [
    { index: '51', label: '文档下载' },
    { index: '52', label: '数据查询' },
    { index: '53', label: '公共服务' },
    { index: '54', label: '数据分析' },
    { index: '55', label: '生产计划' },
    { index: '56', label: '公共物品' },
  ],
  '6': [
    { index: '61', label: '功能介绍' },
    { index: '62', label: '卡牌游戏' },
    { index: '63', label: '安润行动' },
    // { index: '65', label: '极限艺术' },
    { index: '64', label: '管理界面' },
  ],
  '7': [
    { index: '71', label: '词条排行' },
    { index: '72', label: '恶人榜单' },
    { index: '73', label: '旧闻跟踪' },
    { index: '74', label: '知识地图' },
    { index: '75', label: '解密爆料' },
    { index: '76', label: '辟谣专区' },
  ],
};

export default {

  components: {
    HelloLogout,
    EmptyImage,
    SubPage01,
    SubPage02,
    SubPage03,
    SubPage05,
    SubPage11,
    SubPage12,
    SubPage13,
    SubPage65,
    SubPage64,
    SubPage62,
    SubPage63,
    SubPage61,
    SubPage3X,
    SubPage44,
    SubPage42,
    SubPage41,
    SubPage43,
    SubPage51,
    SubPage71,


  

  },



  setup() {

    const error0 = ref('');  
    const message0 = ref('');  


    const activeIndex = ref('6'); // 默认选中新闻动态  
    const defaultSubIndices = topMenuItems.reduce((acc, item) => {
      acc[item.index] = item.defaultSub;
      return acc;
    }, {});
    const activeSubIndices = reactive({ ...defaultSubIndices });

    const handleSelect = (index) => {
      activeIndex.value = index;
      if (!activeSubIndices[index] && subMenuItems[index]?.length) {
        activeSubIndices[index] = subMenuItems[index][0].index;
      }
    };

    const handleSubSelect = (mainIndex, subIndex) => {
      activeSubIndices[mainIndex] = subIndex;
    };

    const dialogVisible = ref(false);

    const loginForm = reactive({
      username: '',
      password: ''
    });

    const handleLogin = async () => {
      if (!loginForm.username || !loginForm.password ) {  
          // 如果任一密码为空或不相等，设置错误消息并返回  
          error0.value = '输入不为空';  
          message0.value = '';  
          return; // 停止执行后续代码  
        }  

        try {
          const response = await axios.post('https://www.aworld.wiki/api/iteminfo/login/', {
            username: loginForm.username,
            password0: loginForm.password,
          });
          message0.value = response.message;
          error0.value = '';
          localStorage.setItem('username', loginForm.username); 
          localStorage.setItem('userid', response.data.userid);
          // ceshi.value = localStorage.getItem('username');
          dialogVisible.value = false;
          window.location.href = '/';

        } catch (e) {
          error0.value = e.error;
          message0.value = '';
        }
};


    onMounted(() => {  
      const username = localStorage.getItem('username');
      if (!username) {
        dialogVisible.value = true;
      }
    });


    return {
      topMenuItems,
      subMenuItems,
      activeIndex,
      activeSubIndices,
      handleSelect,
      handleSubSelect,
      dialogVisible,
      handleLogin,
      loginForm,
      error0,
      message0
    

    };
  },
};  
</script>


<style>
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



.top-menu {
  margin-left: 120px;
}

.main-area {
  padding: 0;
}

.section-row {
  width: 100%;
  margin: 0;
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
  height: 300px;

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




.login-dialog :deep(.el-dialog__body) {
  min-height: 400px;
}

.custom-background {  
  /* background-image: url('https://aworld-1302616346.cos.ap-hongkong.myqcloud.com/static_pic/login2.jpg');  替换为你的图片URL */  
  background-size: cover;  
  height: 100%; /* 确保高度覆盖整个dialog */  
  width: 100%; /* 确保宽度也覆盖 */  
  position: absolute; /* 可能需要绝对定位来覆盖默认背景 */  
  top: 0;  
  left: 0;  
  /* 可能还需要其他样式来确保内容不被遮挡 */  
}  

.input_dengluye{
  background-color:rgba(0,0,0,0);
  border-top:0px;
  border-left:0px;
  border-right:0px;
  border-color:grey;
  height: 30px;
  width:80%;
  color:black;
  font-size: 20px;
  outline:none;}
</style>
