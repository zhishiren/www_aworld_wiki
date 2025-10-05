<template>
  <router-view v-slot="{ Component }">
    <transition>
      <keep-alive>
        <component 
          :is="Component" 
          v-if="$route.meta?.keepAlive"
          :key="$route.fullPath"
        />
      </keep-alive>
    </transition>
    <component 
      :is="Component" 
      v-if="!$route.meta?.keepAlive"
      :key="$route.fullPath"
    />
  </router-view>
</template>



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
body{
  /* position: relative; */
	width: 1280px;  
	margin: 0 auto;

}
* {margin: 0;padding: 0;}   

html, body {
  overflow-y: scroll; /* 使得水平滚动条始终存在防止页面跳动 */
  scrollbar-width: none; /* 对于Firefox */
}

html::-webkit-scrollbar, body::-webkit-scrollbar {
  display: none;
}


nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.el-loading-text {
  font-size: 50px;
  font-weight: 600;
}


</style>
