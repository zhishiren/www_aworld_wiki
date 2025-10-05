<template>
  <div class="news-item">



    <div style="display: flex; justify-content: space-between; align-items: center;">
      <span style="font-size: 20px;">
        <span v-if="fromwhere==='m新闻动态' || fromwhere==='m群内动态'">
          <router-link v-if="item.userXid !== 99999999" class="a_black" 
            :to="{ name: 'detail_mobpage', params: { id: item.userXid, subpagetype: '人物群组-详情' } }">
            <span style="font-size: 20px;"><strong>{{ item.userXname }}</strong></span>
          </router-link>
        <span v-else style="font-size: 20px;"><strong>{{ item.userXname }}</strong></span>
        </span>
        <span v-if="fromwhere==='m用户动态'">
          <span v-if="item.userXid === userSelfId">你</span>
          <span v-if="item.userXid !== userSelfId">TA</span>
        </span>
      </span>
      <span v-if="item.userXid === userSelfId" style="font-size: 18px;color: gray;">Ｘ删</span>
    </div>

    <div style="text-align: left;font-size: 20px;">
      <span v-if="item.op_type === '发言'">
        <span>发言说:</span>
        <span v-if="item.ps_encrypted === 0" class="a_brown">
          <span v-html="item.ps_content" style="color: brown;"></span>
        </span>
        <span v-else class="a_brown" @click="showDialog(item.sparefield1)">
          <span style="background-color: lightgray;color: brown;">{{ item.item0title }}</span>
        </span>
      </span>

      <span v-if="item.op_type === '分享'">
        <span>分享了</span>
        <span class="a_black" @click="navigateToDetail(item.item0id)">
          {{ item.item0title }}
        </span>
        <span v-if="item.ps_content">
          <span style="color: DimGray;">,附言<b>:</b></span>
            <span v-if="item.ps_encrypted === 0" class="a_brown"><span v-html="item.ps_content"></span></span>
            <span v-if="item.ps_encrypted !== 0" class="a_brown" @click="showDialog(item.sparefield1)">
              <span style="background-color: lightgray;color: brown">{{ item.item0title }}</span>
            </span>
        </span>
      </span>
    </div>

    <el-row justify="space-between" style="font-size: 18px;color: gray;border-bottom: 1px solid lightgray;">
      <span>
        <span>{{ formatTime(item.op_time) }}</span>
        <span v-if="item.op_range === 10000000" style="font-size: 18px;color: gray;">｜本人可见</span>
        <span v-if="item.op_range === 99999999" style="font-size: 18px;color: gray;">｜所有人可见</span>
        <span v-if="item.op_range > 10000000 && item.op_range < 99999999" style="font-size: 18px;color: gray;">｜群组可见</span>
      </span>
      <span>
        <span @click="item.drawerVisible = true" style="cursor: pointer;">回复</span>
      </span>
    </el-row>

    <el-drawer v-model="item.drawerVisible" size="50%" direction="btt" :with-header="false">
      <el-row justify="space-between" style="font-size: 24px;">
        <span style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis; display: block; max-width: 80%;">
          <span style="color: black;"><strong>{{ item.userXname }}:</strong></span>
          <span v-if="item.ps_content&&item.op_type==='分享'" v-html="item.ps_content" style="color: brown;"></span>
          <span v-if="item.ps_content&&item.op_type==='发言'" style="color: brown;">{{ item.item0title }}</span>
          <span v-if="!item.ps_content" style="color: brown;">无</span>
        </span>
        <span @click="item.drawerVisible = false">关闭</span>
      </el-row>
      
      <el-row style="text-align: left;font-size: 24px;padding-top: 5px;">
        <input type="text" placeholder="请输入回复上文的内容" class="input_dengluye" style="width: 100%; text-align: left;">
      </el-row>
      <el-row justify="space-between" style="font-size: 20px;">
        <span>
          <el-checkbox label="匿名发言" size="large" />
        </span>
        <span style="font-weight: bolder;">提交</span>
      </el-row>
      <div style="font-size: 22px;text-align: left;color: gray;">以下是所有回复，长按进行回应</div>
    </el-drawer>

    <el-dialog v-model="dialogVisible" width="100%" :close-on-click-modal="true" class="custom-dialog">
      <el-form ref="decodeform" v-model="loginForm">
        <br>
        <input type="password" placeholder="请输入解密密码" class="input_dengluye" style="width: 100%; text-align: center;">
        <br>
        <p style="font-size: 24px;">提示:{{ dialogContent }}</p>
      </el-form>

      <template #footer>
        <el-divider>
          <a class="my-icon" style="font-size: 25px;" @touchstart="handleLogin">点击解密</a>
        </el-divider>
        <br>
        <h2 style="text-align: center; color: brown; font-weight: 300;">测试的解密正文。</h2>
        <br>
        <h2>
          <a class="my-icon" style="color: cornflowerblue;">点看此言论详情</a>
        </h2>
      </template>
    </el-dialog>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'NewsItem',
  props: {
    item: {
      type: Object,
      required: true
    },
    userSelfId: {
      type: Number,
      required: true
    },
    fromwhere: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      dialogVisible: false,
      dialogContent: '',
      loginForm: {
        password: ''
      },
      drawerVisible: false,
      replyContent: '',
      isAnonymous: false
    }
  },
  methods: {
    formatTime(op_time) {
      if (!op_time) return '';
      const now = new Date();
      const opDate = new Date(op_time);
      const timeDiff = now - opDate;
      const hoursDiff = Math.floor(timeDiff / (1000 * 60 * 60));
      const daysDiff = Math.floor(hoursDiff / 24);

      if (hoursDiff < 8) {
        return `${opDate.getHours()}:${opDate.getMinutes().toString().padStart(2, '0')}`;
      } else if (hoursDiff < 24) {
        return `${hoursDiff}小时前`;
      } else {
        return `${daysDiff}天前`;
      }
    },
    showDialog(content) {
      if (content) {
        this.dialogContent = content;
        this.dialogVisible = true;
      }
    },
    handleLogin() {
      if (!this.loginForm.password) {
        console.warn('密码未输入');
        return;
      }
      console.log('处理登录');
    },
    submitReply() {
      if (!this.replyContent) {
        console.warn('回复内容为空');
        return;
      }
      console.log('提交的回复内容:', this.replyContent);
      this.drawerVisible = false;
      this.replyContent = '';
    },
    navigateToDetail(itemId) {
      if (!itemId) {
        console.warn('无效的项目ID');
        return;
      }
      window.location.href = this.$router.resolve({ 
        name: 'detail_mobpage', 
        params: { 
          id: itemId, 
          subpagetype: '知识元素-详情' 
        } 
      }).href;
    }
  },
  created() {
    if (this.item && !this.item.drawerVisible) {
      this.item.drawerVisible = false;
    }
  }
}
</script>

<style scoped>
.news-item {
  margin-bottom: 10px;
}

:deep(.el-scrollbar__wrap) {
  overflow-x: hidden;
}


</style> 