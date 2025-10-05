<template>
  <div class="mobile-page" :class="{ navigating: isNavigating }">
    <div class="top-bar">

      <div style="font-size: 7vw;"><b>Aworld.wiki</b><span>｜</span><a @click.prevent="handleTileTap('/setting_mobpage')" class="mainlinkstyle">设置</a></div>
      <div class="exitbutton">
        <a @click.prevent="handleLogout" class="mainlinkstyle">退出</a>
      </div>
    </div>
    <div class="grid-container">
      <div @click="handleTileTap('/search_mobpage')" :class="['grid-item2', tileDisabledClass, { 'grid-item--active': activeTile === '/search_mobpage' }]">搜</div>
      <div @click="handleTileTap('/followed_mobpage')" :class="['grid-item1', tileDisabledClass, { 'grid-item--active': activeTile === '/followed_mobpage' }]">
        <div class="two-line">关注<br>收藏</div>
      </div>
      <div @click="handleTileTap('/chatlist_mobpage')" :class="['grid-item2', tileDisabledClass, { 'grid-item--active': activeTile === '/chatlist_mobpage' }]">聊</div>
      <div @click="handleTileTap('/friends_mobpage')" :class="['grid-item1', tileDisabledClass, { 'grid-item--active': activeTile === '/friends_mobpage' }]">
        <div class="two-line">朋友<br>组织</div>
      </div>
      <div @click="handleTileTap('/TodayNews_mobpage')" :class="['grid-item1', tileDisabledClass, { 'grid-item--active': activeTile === '/TodayNews_mobpage' }]">
        <div class="two-line">新闻<br>动态</div>
      </div>
      <!-- 这里的推荐阅读，经点击之后直接跳转到下下的页面 -->
      <div @click="handleTileTap('/RS_mobpage')" :class="['grid-item1', tileDisabledClass, { 'grid-item--active': activeTile === '/RS_mobpage' }]">
        <div class="two-line">推荐<br>阅读</div>
      </div>
      <div @click="handleTileTap('/debate_mobpage')" :class="['grid-item2', tileDisabledClass, { 'grid-item--active': activeTile === '/debate_mobpage' }]">增</div>
      <div @click="handleTileTap('/shared_mobpage')" :class="['grid-item1', tileDisabledClass, { 'grid-item--active': activeTile === '/shared_mobpage' }]">
        <div class="two-line">共享<br>资料</div>
      </div>
      <!-- <div @touchstart.prevent="navigateTo('/En_mobpage')" class="grid-item2" style="font-weight: bolder;">En</div> -->
      <div class="grid-item2" style="font-weight: bolder;">En</div>
      <div @click="handleTileTap('/commune_mobpage')" :class="['grid-item2', 'wide', tileDisabledClass, { 'grid-item--active': activeTile === '/commune_mobpage' }]">
        <div class="two-line" style="white-space: nowrap;">公共事务</div>
      </div>
      <div @click="handleTileTap('/mine_mobpage')" :class="['grid-item1', tileDisabledClass, { 'grid-item--active': activeTile === '/mine_mobpage' }]">
        <div class="two-line">个人<br>事务</div>
      </div>
    </div>
    <br>
    <CommandLine :text="commandText" style="color: #333;" />
    <el-dialog v-model="drawerVisible" title="登录或注册" width="100%" :show-close="false" :close-on-click-modal="false"
      class="custom-dialog">
      <el-form ref="loginform" v-model="loginForm">
        <br>
        <div v-if="loginInputVisible">
          <input autocomplete="off" type="text" placeholder="你的用户名,your username" v-model="loginForm.username"
            class="input_dengluye">
          <br><br><br>
          <input type="password" placeholder="你的密码,your password" v-model="loginForm.password" class="input_dengluye">
        </div>

        <div v-if="!loginInputVisible">
          <input autocomplete="off" type="text" placeholder="设置用户名,Set username" v-model="loginForm.usernamek"
            class="input_dengluye">
          <br><br><br>
          <input type="password" placeholder="设置密码,Set password" v-model="loginForm.passwordk" class="input_dengluye">
          <br><br><br>
          <input type="password" placeholder="确认密码,Confirm password" v-model="loginForm.confirmPasswordk"
            class="input_dengluye">
        </div>


      </el-form>

      <template #footer>
        <el-divider>
          <a class="my-icon" style="font-size: 25px;" @click="handleLogin" v-if="loginInputVisible">确定登陆</a>
          <a class="my-icon" style="font-size: 25px;" @click="handleRegister" v-if="!loginInputVisible">确认注册</a>
        </el-divider>
        <br>
        <h2 v-if="showError" style="text-align: center; color: red; font-weight: 300;">{{ error0 }}</h2>
        <br>
        <h2>
          <a class="my-icon" style="color: cornflowerblue;" v-if="loginInputVisible"
            @click="loginInputVisible = false">第一次来？点击注册</a>
          <a class="my-icon" style="color: cornflowerblue;" v-if="!loginInputVisible"
            @click="loginInputVisible = true">返回登录</a>
        </h2>
      </template>
    </el-dialog>

  </div>
</template>

<script setup>
import { ref, reactive, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import CommandLine from '../mobilecomponents/CommandLine.vue';  // 导入新组件

const router = useRouter();
const drawerVisible = ref(false);
const username = ref(localStorage.getItem('username') || '');
const userid = ref(localStorage.getItem('userid') || '');
const commandText = ref(`hello,${username.value}`);
const loginForm = reactive({
  username: '',
  password: '',
  usernamek: '',
  passwordk: '',
  confirmPasswordk: ''
});
const error0 = ref('');
const showError = ref(false);

const loginInputVisible = ref(true);

const isNavigating = ref(false);
const activeTile = ref('');
const tileDisabledClass = computed(() => ({ 'grid-item--disabled': isNavigating.value }));

const navigateTo = async (path) => {
  if (isNavigating.value) return;
  isNavigating.value = true;
  try {
    await router.push(path);
  } catch (error) {
    if (error?.name !== 'NavigationDuplicated') {
      console.error('Navigation failed:', error);
    }
  } finally {
    requestAnimationFrame(() => {
      isNavigating.value = false;
    });
  }
};

const handleTileTap = async (path) => {
  if (isNavigating.value) return;
  activeTile.value = path;
  try {
    await navigateTo(path);
  } finally {
    setTimeout(() => {
      if (activeTile.value === path) {
        activeTile.value = '';
      }
    }, 120);
  }
};

const handleLogout = () => {
  localStorage.removeItem('username');
  localStorage.removeItem('userid');
  window.location.reload();
};

const handleLogin = async () => {
  if (!loginForm.username || !loginForm.password) {
    setError('用户名和密码不能为空');
    return;
  }
  try {
    const response = await axios.post('https://www.aworld.wiki/api/iteminfo/login/', {
      username: loginForm.username,
      password0: loginForm.password,
    });

    error0.value = '';
    localStorage.setItem('username', loginForm.username);
    localStorage.setItem('userid', response.data.userid);

    drawerVisible.value = false;
    window.location.href = '/';
    loginForm.username = '';
    loginForm.password = '';
    loginInputVisible.value = true;

  } catch (e) {
    if (e.response) {
      // 服务器返回了响应，但状态码不在2xx范围内
      setError(`错误 ${e.response.status}: ${e.response.data.error || e.response.statusText}`);
    } else if (e.request) {
      // 请求已发出，但未收到响应
      setError('无响应，请检查网络连接');
    } else {
      // 其他错误
      setError(`请求失败: ${e.message}`);
    }
  }
};

const setError = (errorMessage) => {
  error0.value = errorMessage;
  showError.value = true;
  setTimeout(() => {
    showError.value = false;
  }, 3000);
};

const handleRegister = async () => {
  if (loginForm.usernamek.length > 8) {
    setError('用户名不能超过8个字符');
    return;
  }
  if (!loginForm.usernamek || !loginForm.passwordk || !loginForm.confirmPasswordk) {
    setError('注册信息不能为空');
    return;
  }
  if (loginForm.passwordk !== loginForm.confirmPasswordk) {
    setError('注册密码输入不一致');
    return;
  }
  try {
    const response = await axios.post('https://www.aworld.wiki/api/iteminfo/register/', {
      username: loginForm.usernamek,
      password1: loginForm.passwordk,
      password2: loginForm.confirmPasswordk,
    });

    error0.value = '';
    localStorage.setItem('username', loginForm.usernamek);
    localStorage.setItem('userid', response.data.userid);

    drawerVisible.value = false;
    window.location.href = '/';
    loginForm.usernamek = '';
    loginForm.passwordk = '';
    loginForm.confirmPasswordk = '';
    loginInputVisible.value = true;

  } catch (e) {
    if (e.response) {
      setError(`错误 ${e.response.status}: ${e.response.data.error || e.response.statusText}`);
    } else if (e.request) {
      setError('无响应，请检查网络连接');
    } else {
      setError(`请求失败: ${e.message}`);
    }
  }
};

onMounted(() => {
  if (!userid.value) {
    drawerVisible.value = true;
  }
});
</script>

<style scoped>
.mobile-page {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  min-height: 100vh;
  overflow-y: auto;
  background-color: #f0f0f0;
  color: #333;
  display: flex;
  flex-direction: column;
  padding: 20px;
  box-sizing: border-box;
  font-family: 'Courier New', Courier, monospace;
  isolation: isolate;
  z-index: 1;
}

.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 5px 0;
  border-bottom: 2px solid #333;
  margin-bottom: 20px;
}

.exitbutton {
  font-size: 6vw;
  cursor: pointer;
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 10px;
  width: 100%;
  max-width: 400px;
  margin: 0 auto;
  position: relative;
  z-index: 2;
}

.grid-item1,
.grid-item2 {
  background-color: #fff;
  border: 2px solid #333;
  padding: 20px;
  text-align: center;
  aspect-ratio: 1 / 1;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 3px 3px 0 #333;
  transition: all 0.1s ease;
  position: relative;
  overflow: hidden;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  user-select: none;
  touch-action: manipulation;
  z-index: 3;
  pointer-events: auto;
}

.wide {
  grid-column: span 2;
  aspect-ratio: 2.5 / 1;
  font-size: 30px;
}

.grid-item1::before,
.grid-item2::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background:
    linear-gradient(45deg, transparent 49%, #ddd 49%, #ddd 51%, transparent 51%);
  background-size: 6px 6px;
  opacity: 0.1;
  transition: opacity 0.3s ease;
}

.grid-item1:hover,
.grid-item2:hover {
  transform: translate(1px, 1px);
  box-shadow: 2px 2px 0 #333;
}

.grid-item1:active,
.grid-item2:active {
  opacity: 0.8;
  transform: translate(2px, 2px);
  box-shadow: 1px 1px 0 #333;
  transition: all 0.05s ease;
}

.grid-item--active {
  transform: translate(2px, 2px);
  box-shadow: 1px 1px 0 #333;
  opacity: 0.85;
}

.grid-item--disabled {
  pointer-events: none;
  opacity: 0.6;
}

.grid-item1:hover::before,
.grid-item2:hover::before {
  opacity: 0.2;
}

.grid-item1:active::before,
.grid-item2:active::before {
  opacity: 0.3;
}

.grid-item1 {
  font-size: 20px;
}

.grid-item2 {
  font-size: 30px;
}

.two-line {
  display: inline-block;
  text-align: center;
  line-height: 1.2;
}

@keyframes scroll {
  0% {
    transform: translate(0, 0);
  }

  100% {
    transform: translate(-100%, 0);
  }
}

@media (max-width: 768px) {
  .grid-container {
    grid-gap: 5px;
  }

  .grid-item1,
  .grid-item2 {
    padding: 15px;
  }

  .grid-item1 {
    font-size: 25px;
  }

  .grid-item2 {
    font-size: 40px;
  }
}


/* 使用深度选择器来覆盖 Element UI 的内部样式 */
/* .custom-dialog /deep/ .el-dialog__title {  
  font-size: 28px;  
}   */
/* 注意：在一些构建工具或 Vue 版本中，你可能需要使用 ::v-deep 而不是 /deep/ */
::v-deep .el-dialog__title {
  font-size: 28px;
}


.mainlinkstyle {
  color: grey;
  font-weight: bold;
  font-size: 6vw;
  -webkit-tap-highlight-color: transparent;
  user-select: none;
  touch-action: manipulation;
  position: relative;
  z-index: 3;
  pointer-events: auto;
}

.mobile-page.navigating .mainlinkstyle {
  pointer-events: none;
  opacity: 0.6;
}

.mobile-page::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
  pointer-events: none;
  z-index: 10;
}

.mobile-page.navigating::before {
  pointer-events: auto;
}
</style>
