import { createRouter, createWebHashHistory } from 'vue-router';
// import HomeView from '../views/HomeView.vue'
import '../assets/zcss.css';
import PCHomePage from '../views/MainView.vue';
import MobileHomePage from '../views/MobileHomePage.vue';


// 设备检测函数
const isMobile = window.innerWidth <= 768;

// 根据设备类型选择不同的主页组件
const HomeView = isMobile ? MobileHomePage : PCHomePage;



const routes = [
  {
    path: '/login',
    name: 'login',
    component: () => import( '../views/LoginView.vue')
  },
  {
    path: '/DetailPage/:id',
    name: 'DetailPage',
    component: () => import( '../views/DetailPage.vue')
  },


 



  {
    path: '/PS_reply_page/:id',
    name: 'PS_reply_page',
    component: () => import( '../detail_subpage/PS_reply_page.vue')
  },

  {
    path: '/',
    name: 'main',
    // component: () => import( '../views/MainView.vue')
    component: HomeView // 使用根据设备类型选择的主页组件

  },


  {
    path: '/search_apage',
    name: 'search_apage',
    component: () => import( '../actionpage/search_apage.vue')
  },

 


  {
    path: '/ai_apage',
    name: 'ai_apage',
    component: () => import( '../actionpage/ai_apage.vue')
  },



  {
    path: '/chat_apage',
    name: 'chat_apage',
    component: () => import( '../actionpage/chat_apage.vue')
  },



  {
    path: '/create_apage',
    name: 'create_apage',
    component: () => import( '../actionpage/create_apage.vue')
  },
  

  {
    path: '/chatlist_mobpage',
    name: 'chatlist_mobpage',
    component: () => import( '../mobilepage/chatlist_mobpage.vue')
  },

  {
    path: '/commune_mobpage',
    name: 'commune_mobpage',
    component: () => import( '../mobilepage/commune_mobpage.vue')
  },

  {
    path: '/debate_mobpage',
    name: 'debate_mobpage',
    component: () => import('../mobilepage/create_mobpage.vue')
  },

  {
    path: '/followed_mobpage',
    name: 'followed_mobpage',
    component: () => import('../mobilepage/followed_mobpage.vue'),
    meta: { 
      keepAlive: true  // 添加 keepAlive 标记
    }
  },

  {
    path: '/friends_mobpage',
    name: 'friends_mobpage',
    component: () => import('../mobilepage/friends_mobpage.vue'),
    meta: { 
      keepAlive: true  // 添加 keepAlive 标记
    }
  },

  {
    path: '/mine_mobpage',
    name: 'mine_mobpage',
    component: () => import('../mobilepage/mine_mobpage.vue')
  },


  {
    path: '/RS_mobpage',
    name: 'RS_mobpage',
    component: () => import('../mobilepage/RS_mobpage.vue'),
    meta: { 
      keepAlive: true  // 添加 keepAlive 标记
    }
  },

  {
    path: '/search_mobpage',
    name: 'search_mobpage',
    component: () => import('../mobilepage/search_mobpage.vue')
  },


  {
    path: '/setting_mobpage',
    name: 'setting_mobpage',
    component: () => import('../mobilepage/setting_mobpage.vue')
  },


  {
    path: '/shared_mobpage',
    name: 'shared_mobpage',
    component: () => import('../mobilepage/shared_mobpage.vue')
  },


  {
    path: '/TodayNews_mobpage',
    name: 'TodayNews_mobpage',
    component: () => import('../mobilepage/TodayNews_mobpage.vue'),
    meta: { 
      keepAlive: true  // 需要被缓存
    }
  },

  {
    path: '/detail_mobpage/:id/:subpagetype',
    name: 'detail_mobpage',
    component: () => import('../mobilepage/detail_mobpage.vue'),
    meta: { 
      keepAlive: false  // 不需要被缓存
    }
  },
  
  {
    path: '/replydetail_mobpage/:id',
    name: 'replydetail_mobpage',
    component: () => import('../mobilepage/replydetail_mobpage.vue')
  },

  {
    path: '/mobile/chatroom',
    name: 'chatroom_mobpage',
    component: () => import('../mobilepage/chatroom_mobpage.vue')
  },







];

const router = createRouter({
  history: createWebHashHistory(),
  routes
});


// 路由守卫 - 检查用户是否登录  
router.beforeEach((to, from, next) => {  
  // 排除登录页和主页的路由检查  
  if (to.path === '/login' || to.path === '/') {  
    next(); // 直接进入目标路由  
  } else {  
    // 检查localStorage中是否有用户名  
    const username = localStorage.getItem('username');  
    if (!username) {  
      // 如果没有用户名，则重定向到主页  
      next('/');  
    } else {  
      // 如果有用户名，则正常进入目标路由  
      next();  
    }  
  }  
});

export default router
