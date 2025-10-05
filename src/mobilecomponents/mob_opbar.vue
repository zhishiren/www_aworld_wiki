<template>
    <div style="position: fixed; bottom: 0; left: 0; height: auto; width: 100%; background: rgba(255, 255, 255, 0.8);font-size: 25px;font-weight: bolder;color:gray;font-family: 'Microsoft YaHei', '微软雅黑', sans-serif;">

      <el-row v-if="fromwhere==='m元素详情' && item_detail?.item_type === '段落'" justify="space-between" style="border-bottom: 1px groove lightblue;">
        <span @click="$emit('prevpara')">上一段</span>
        <span @click="$emit('paramenu')">全文目录</span>
        <span @click="$emit('nextpara')">下一段</span>
      </el-row>

      <el-row v-if="(fromwhere==='m元素详情' && total_number>10 && item_detail?.item_type === '文章') || (fromwhere==='m关注收藏' && total_number>10)|| (fromwhere==='m聊天列表' && total_number>10)|| (fromwhere==='m新闻动态' && total_number>10)||  (fromwhere==='m搜索页面' && total_number>10)|| (fromwhere==='m朋友组织' && total_number>10)" justify="space-between" style="border-bottom: 1px groove lightblue;">
        <span @click="$emit('prev10')">上十条</span>
        <span>第{{ current_number }}页</span>
        <span @click="$emit('next10')">下十条</span>
      </el-row>

      <el-row v-if="fromwhere==='m朋友组织'" justify="center">
        <!-- <span @click="$emit('search')">查找</span>
        <span>｜</span>-->
        <span @click="$emit('followed')">我关注的</span>
        <span>｜</span> 
        <span @click="$emit('refresh1')">重置刷新</span>
      </el-row>



      <el-row v-if="fromwhere==='m推荐阅读'" justify="center">
        <span @click="$emit('change')">换一批</span>
      </el-row>

      <el-row v-if="fromwhere==='m关注收藏'||fromwhere==='m聊天列表'" justify="center">
        <span @click="$emit('refresh2')">刷新</span>
      </el-row>

      <el-row justify="center" v-if="fromwhere==='m新闻动态'">
        <span>
          <span @click="$emit('post')">发言</span>
          <span>｜</span>
          <span @click="$emit('refresh3')">刷新</span>
        </span>
      </el-row>

      <el-row justify="space-between" v-if="fromwhere==='m聊天页面'">
        <span @click="$emit('scrollToBottom')">返底</span>
        <span @click="$emit('post')">发言</span>
        <span @click="$emit('refresh3')">刷新</span>
      </el-row>

      <el-row justify="center" v-if="fromwhere==='m搜索页面'">
        <template v-if="!showResults">
          <el-input
            v-model="localKeyword"
            @input="$emit('update:keyword', localKeyword)"
            @keyup.enter="handleSubmit"
            placeholder="请输入关键词"
            size="large"
            style="width: 98.5%"
            class="search-input"
          >
            <template #suffix>
              <el-icon class="search-icon" @click="handleSubmit">
                <Search />
              </el-icon>
            </template>
          </el-input>
        </template>
        <template v-else>
          <span>{{ total_number }} 条结果</span>
          <span @click="$emit('reset')">｜重置</span>
        </template>
      </el-row>

      <el-row v-if="fromwhere==='m元素详情'" justify="center">
        <span @click="$emit('share')">分享</span>
        <!-- <span><el-divider direction="vertical" /><span style="display: inline-block; width: 2em;"></span><el-divider direction="vertical" /></span> -->
        <span><el-divider direction="vertical" /><span style="display: inline-block; width: 2em;font-weight: lighter;color:white;background-color: grey">{{ isFollowed ? '已关' : '' }}</span><el-divider direction="vertical" /></span>
        <span @click="handleFollow">{{ isFollowed ? '取关' : '关注' }}</span>
      </el-row>

      <el-row v-if="fromwhere==='m元素详情'" justify="space-between" style="border-top: 1px groove lightblue;">
        <span @click="$emit('like')">顶</span>
        <span @click="$emit('comment')">评论</span>
        <span @click="$emit('dislike')">踩</span>
      </el-row>
    </div>
  </template>

<script>
import axios from 'axios'
import { Search } from '@element-plus/icons-vue'

export default {
  name: 'mob_opbar',
  components: {
    Search
  },
  props: {
    fromwhere: {type: String,required: true},
    current_number: {type: Number, required: false},
    total_number: {type: Number, required: false},
    item_detail: {type: Object, required: false},
    keyword: {type: String, required: false},
    isFollowed: {type: Boolean, required: false}
  },
  data() {
    return {
      localKeyword: this.keyword || '',
      showResults: false,
      userId: localStorage.getItem('userid'),
      username: localStorage.getItem('username'),
    }
  },
  watch: {
    keyword(newVal) {
      this.localKeyword = newVal;
    },
    total_number(newVal) {
      this.showResults = newVal > 0;
    }
  },
  methods: {
    handleSubmit() {
      if (this.showResults) {
        this.showResults = false;
      } else {
        this.$emit('submit', this.localKeyword);
      }
    },
    
    async handleFollow() {
      try {
        const response = await axios.post('https://www.aworld.wiki/api/opinfo/add_op/', {
          userid: this.userId,
          username: this.username,
          itemtype: '关注',  // op_type
          item0id: this.item_detail.item_id,
          item0title: this.item_detail.item_title,
          item0type: this.item_detail.item_type,
          subtype: '',
          publicRange: 99999999,
          content: '',
          isEncrypted: false,
          isAnonymous: false
        });

        if (response.data.success) {
          // this.isFollowed = !this.isFollowed;以下重新传递给父组件，重新加载
          this.$emit('refresh');
        } else {
          console.error('关注操作失败:', response.data.message);
        }
      } catch (error) {
        console.error('关注请求出错:', error);
      }
    }
  },
  emits: [
    'prevpara',     // 上一段
    'paramenu',     // 全文目录
    'nextpara',     // 下一段
    'prev10',    // 上十条
    'next10',    // 下十条
    'search',   // 查找
    'followed', // 我关注的
    'refresh1', // 刷新(朋友组织)
    'submit',   // 提交
    'reset',    // 重置
    'change',   // 换一批
    'refresh2', // 刷新(关注收藏/聊天列表)
    'post',     // 发言
    'refresh3', // 刷新(聊天页面)
    'share',    // 分享
    'follow',   // 关注
    'like',     // 顶
    'comment',  // 评论
    'dislike',  // 踩
    'update:keyword',
    'scrollTop',
    'scrollToBottom',
    'refresh'
  ]
}
</script>

<style scoped>
.el-row {
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  user-select: none;
}

.input_dengluye {
  transition: all 0.3s ease;
}

.search-input :deep(.el-input__suffix-inner .el-icon) {
  font-weight: bolder;
  color: #000000;
  font-size: 25px;
}
</style> 