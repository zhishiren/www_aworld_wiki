<template>  
  <div class="logo">  
    <span>Aworld</span>  
    <!-- <span style="font-size: 16px;" v-typewriter="`【你好${username},今天是2024年1月1日`"></span> -->
    <!-- <span style="font-size: 16px;">【这是打字机效果{{ username }}</span> -->
    <span class="typewriter" ref="typewriterElement"></span>

    <span style="font-size: 16px;font-weight: bolder;" v-cursor>Ⓐ</span>
    <span style="font-size: 16px;" >】</span>
    <!-- <CommandLine :text="commandText" style="color: white;font-size: 18px;" /> -->
    <span class="logout19px">  
      <a class="a_white" @click="logout"><b>退出</b></a>  
    </span>  
  </div>  
</template>  
  
<script>  
// import { ref} from 'vue';  
import { ref, onMounted } from 'vue';  
// import CommandLine from '../../mobilecomponents/CommandLine.vue';  // 导入新组件


export default {  
  components: {  
    // CommandLine,

  }  ,

  setup() {  
    // const commandText = ref("测试hi,testusername");  // 将文本作为响应式数据，不超过13个汉字长度

    const username = ref('');  
    const userid = ref('');  
  
    const typewriterElement = ref(null);

    onMounted(() => {
      username.value = localStorage.getItem('username') || '';
      userid.value = localStorage.getItem('userid') || '';
      
      const now = new Date();
      const year = now.getFullYear();
      const formatNumber = (value) => String(value).padStart(2, '0');

      const month = formatNumber(now.getMonth() + 1); // getMonth() 返回 0-11
      const day = formatNumber(now.getDate());
      const hours = formatNumber(now.getHours());
      const minutes = formatNumber(now.getMinutes());

      const currentDate = `${year}年${month}月${day}日${hours}:${minutes}`;
      
      typeWriter(`【你好,${username.value},今天是${currentDate}`, typewriterElement.value);
    });

    function typeWriter(text, element, i = 0) {
      if (i < text.length) {
        element.innerHTML += text.charAt(i);
        i++;
        setTimeout(() => typeWriter(text, element, i), 100);
      }
    }

    function logout() {
      console.log("Logout function called"); // 添加调试信息
      localStorage.removeItem('username');
      localStorage.removeItem('userid');
      window.location.reload();
    }

    return {
      username,
      typewriterElement,
      logout,
    };



  },
  directives: {
    // typewriter: {
    //   mounted(el, binding) {
    //     const text = binding.value
    //     let index = 0
    //     const interval = setInterval(() => {
    //       if (index < text.length) {
    //         el.textContent += text[index]
    //         index++
    //       } else {
    //         clearInterval(interval)
    //       }
    //     }, 100)
    //   }
    // },
    cursor: {
      mounted(el) {
        setInterval(() => {
          el.style.opacity = el.style.opacity === '0' ? '1' : '0'
        }, 500)
      }
    }
  }
};  
</script>  

<style scoped>
.logo {
  height: 40px;
  font-size: 40px;
  line-height: 40px;
  color: #FFF;
  background-color: #708090;
  text-align: left;
  padding: 0;
}

.logout19px {
  font-size: 19px;
  width: 60px;
  float: right;
  text-align: center;
  display: inline-block;
  margin-top: 5px;
}

.a_white {
  text-decoration: none;
  cursor: pointer;
  color: white;
}

.a_white:hover {
  color: orange;
}


.typewriter {
  font-size: 16px;
  overflow: hidden;
  white-space: nowrap;
  margin: 0 auto;
  letter-spacing: .15em;
}

@keyframes blink-caret {
  from, to { border-color: transparent }
  50% { border-color: orange; }
}


</style>
