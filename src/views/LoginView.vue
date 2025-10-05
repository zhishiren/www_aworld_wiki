<template>
  <div class="full-bg-container">  
    <div class="background-image"></div>  
    <div class="content">  
    <el-row style=" margin-top: 120px;">  
      <el-col :span="6">  
        <br>
        <el-menu
          :default-active="activeMenu"
          @select="handleSelect"
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose"
          style="border:0px;" 
          background-color="rgba(0,0,0,0)" 
          text-color="black" 
          active-text-color="#FF8000">
          <el-menu-item index="2" style="font-size: 22px;">
            <el-tooltip content="<h2>Log in</h2>" raw-content>账号登录</el-tooltip> 
          </el-menu-item>
          <el-menu-item index="1" style="font-size: 22px;">
            <span>通知公告</span>
          </el-menu-item>
          <el-menu-item index="3" style="font-size: 22px;">
            <el-tooltip content="<h2>Sign up</h2>" raw-content>新人注册</el-tooltip> 
          </el-menu-item>
        </el-menu>
      </el-col>   
      <el-col :span="18" style="font-size: 22px;font-style: 微软雅黑;">  

        <div class="input_area">
          <div v-show="activeMenu === '1'" >
              <br>
              <p>-----Public Notice-----</p>
              <div>QQgroup:771722807</div>
              <div>(管理面板的导入信息)</div>
              <div>(管理面板的导入信息)</div>
              <div>(管理面板的导入信息)</div>
              <div>(管理面板的导入信息)</div>
          </div>
          <div v-show="activeMenu === '2'">
            <br>
            <input id="name0" v-model="name0" autocomplete="off" type="text" placeholder="你的用户名,your username" class="input_dengluye">
            <br><br><br>
            <input id="password0" type="password"  v-model="password0" placeholder="你的密码,your password" class="input_dengluye">
            <br>
            <span v-if="error0" class="font18px" style="color:orange">{{error0}}</span>
            <span v-if="message0" class="font18px" style="color:orange">{{message0}}</span>
            <br><br>
            <el-row>
                <el-button class="commmit-button" @click="submit0" size="medium" round>确定</el-button>
            </el-row>

          </div>
          <div v-show="activeMenu === '3'">
            <br>
            <input id="name1" v-model="name1" autocomplete="off" type="text" placeholder="新建用户名,create username" class="input_dengluye" @blur="check_name_existed">
            <br><br>
            <input id="password1"  type="password"  v-model="password1" placeholder="设置密码,create password" class="input_dengluye">
            <br><br>
            <input id="password2" type="password"  v-model="password2" placeholder="再输密码,password again" class="input_dengluye">
            <br>
            <h4 v-if="error1" style="color:orange">{{error1}}</h4>
            <h4 v-if="message1" style="color:orange">{{message1}}</h4>

            <br>
            <el-row>
                <el-button  @click="submit1" class="commmit-button" size="medium" round>确定</el-button>
            </el-row>
          </div> 

        </div>
      </el-col>   
 
    </el-row> 
    </div>  
  </div>  
</template>

<script setup>  
      import { ref } from 'vue';  
      import axios from 'axios';  

      const name0 = ref('');  
      const password0 = ref('');  
      const error0 = ref('');  
      const message0 = ref('');  
      // 以上是登录的配置

      const name1 = ref('');  
      const password1 = ref('');  
      const password2 = ref('');  
      const error1 = ref('');  
      const message1 = ref('');  
      // 以上是注册的配置

      const activeMenu = ref('2');

      const submit1 = async () => {
        if (!name1.value || !password1.value || !password2.value || password1.value !== password2.value) {  
          // 如果任一密码为空或不相等，设置错误消息并返回  
          error1.value = '输入不为空且密码须一致'; 
          message1.value = '';  
          return; // 停止执行后续代码  
        }  

        try {
          const response = await axios.post('https://www.aworld.wiki/api/iteminfo/register/', {
            username: name1.value,
            password1: password1.value,
            password2: password2.value,
          });
          message1.value = response.data.message;
          error1.value = '';
          // localStorage.setItem('username', name1.value); 
          // ceshi.value = localStorage.getItem('username');
          localStorage.setItem('username', name1.value);
          localStorage.setItem('userid', response.data.userid);
          name0.value = name1.value;
        } catch (e) {
          error1.value = e.response.data.error;
          message1.value = '';
        }
      };


      const submit0 = async () => {
        if (!name0.value || !password0.value ) {  
          // 如果任一密码为空或不相等，设置错误消息并返回  
          error0.value = '输入不为空';  
          message0.value = '';  
          return; // 停止执行后续代码  
        }  

        try {
          const response = await axios.post('https://www.aworld.wiki/api/iteminfo/login/', {
            username: name0.value,
            password0: password0.value,
          });
          message0.value = response.data.message;
          error0.value = '';
          localStorage.setItem('username', name0.value); 
          localStorage.setItem('userid', response.data.userid);
          // ceshi.value = localStorage.getItem('username');
          window.location.href = '/';

        } catch (e) {
          error0.value = e.response.data.error;
          message0.value = '';
        }
      };
        

    
      const handleOpen = (key, keyPath) => {
        console.log('Menu Opened:', key, keyPath);
      };
      const handleClose = (key, keyPath) => {
        console.log('Menu Closed:', key, keyPath);
      };
      const handleSelect = (key) => {
        activeMenu.value = key;
      };
  

</script>


<style scoped>  

          

.full-bg-container {  
  position: relative;  
  width: 100%; 
  overflow: hidden;  
/* 确保内容不会溢出 */  
   /* 设置容器高度为视口高度 */  
}  
  
.background-image {  
  position: absolute;
  background-image: url('https://aworld-1302616346.cos.ap-hongkong.myqcloud.com/static_pic/aworldwiki_login.jpg');  
  /* background-image: url('https://z2020-1302616346.cos.ap-hongkong.myqcloud.com/zhishiren_info_white6.jpg');   */
  background-position: center center;
  background-repeat: no-repeat;  
  background-size: cover; 
  width: 1280px;
  height: 100%;
  z-index: -1; /* 确保背景图片在最底层 */  
}  
  
.content {  
  position: relative;  
  z-index: 999; /* 确保内容悬浮在背景图片之上 */  
  padding: 10px; /* 可以根据需要添加内边距 */  
  color: black; /* 设置文字颜色，确保在背景图片上可见 */  
  text-align: left;
  height: 800px;
  width: 450px;
}  

.commmit-button{
  margin-left:70px;font-size:20px;background-color:rgba(0,0,0,0);color:black;border-color:grey;
}

.input_area{height:100%;width:auto;color: black;text-align:left;margin-left: 50px;}
.input_dengluye{
  background-color:rgba(0,0,0,0);
  border-top:0px;
  border-left:0px;
  border-right:0px;
  border-color:grey;
  height: 30px;
  width:100%;
  color:black;
  font-size: 20px;
  outline:none;}

</style>