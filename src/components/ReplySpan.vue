  
  <!-- 这是用以前数据表结果设计的，作废。 -->
  <template>  
    <el-row style="display: flex; justify-content: space-between;padding-top: 3px;">
      <span>
        <span v-if="item_object1.fytype">{{ item_object1.fytype }}<el-divider direction="vertical" /></span>
        <span v-if="item_object1.fyatt">{{ item_object1.fyatt }}<el-divider direction="vertical" /></span>
        <span>{{ fanweiText }}</span>
        <!-- 发言范围如果为90000000，则为所有人可见，如果为80000000则为本人可见。 -->
      </span>
      <span>
        <span><a class="a_grey">回复</a><el-divider direction="vertical" /></span>
        <span><a class="a_grey">顶</a><el-divider direction="vertical" /></span>
        <span><a class="a_grey">踩</a><el-divider direction="vertical" /></span>
        <span>{{ getRelativeTime(item_object1.time1) }}</span>
      </span>
    </el-row>
  </template>  

  <script>  
import { ref, computed } from 'vue'; 
  // // Add the following line to import the 'props' object
  // import { props } from 'vue';

  export default {
    name: 'ReplySpan', 

    props: {

      itemObject1: {  
        type: Object,  
        required: false,
        default: () => ({}) // 提供一个默认空对象以避免未定义错误  
      },

    },

    setup(props) {
 
      function getRelativeTime(dateString) {  
  const now = new Date();  
  const pastDate = new Date(dateString);  
  const secondsAgo = Math.floor((now - pastDate) / 1000);  
  
  const intervals = [  
    { threshold: 60 * 60, label: '秒', maxCount: 59 },  
    { threshold: 60 * 60 * 24, label: '分钟', maxCount: 59 },  
    { threshold: 60 * 60 * 24 * 7, label: '小时', maxCount: 23 },  
    { threshold: 60 * 60 * 24 * 30, label: '天', maxCount: 30 }, // Approximately one month  
    { threshold: 60 * 60 * 24 * 365, label: '月', maxCount: 11 }, // Approximately one year  
    { threshold: Infinity, label: '年', maxCount: null }  
  ];  
  
  let count = 0;  
  for (let i = 0; i < intervals.length; i++) {  
    if (secondsAgo < intervals[i].threshold) {  
      count = Math.floor(secondsAgo / intervals[i - 1].threshold);  
      return count + ' ' + intervals[i - 1].label + '前';  
    }  
  }  
  
  // If the date is too far in the past, just return the number of years  
  if (intervals[intervals.length - 1].threshold !== Infinity) {  
    count = Math.floor(secondsAgo / intervals[intervals.length - 1].threshold);  
  }  
  return count + ' ' + intervals[intervals.length - 1].label + '前';  
}  



      const item_object1 = ref(props.itemObject1);
      const fanweiText = computed(() => {  
        if (props.itemObject1.fyfanwei === 90000000) {  
          return "所有人可见";  
        } else if (props.itemObject1.fyfanwei === 80000000) {  
          return "本人可见";  
        } else {  
          return "部分群组可见";  
        }  
      });  
      const relativeTime = computed(() => {  
      return getRelativeTime(props.itemObject1.time0);  
    });  


      return {
        item_object1,
        fanweiText,
        getRelativeTime,
        relativeTime,


    

      };
    
   

    },
  };  




  </script>