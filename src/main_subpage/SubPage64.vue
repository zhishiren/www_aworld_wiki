<template>
  <div class="subpage64">
    <el-row style="height:270px">
      <el-col :span="24">
        <img
          src="https://z2020-1302616346.cos.ap-hongkong.myqcloud.com/aboutwebsite/aboutus51.jpg"
          class="bg_image"
          style="height:270px;width:100%;position: relative;"
          alt="背景图"
        >
        <div
          class="page-header"
          style="color:white;position: absolute; top: 10%; left: 50%; transform: translate(-50%, -50%); z-index: 1; text-align: center;font-size: 30px;"
        >
          管理界面
        </div>
      </el-col>
    </el-row>

    <el-row class="query-row">
      <el-col :span="24">
        <div class="query-controls">
          <span class="query-label">查询元素信息：</span>
          <el-input
            v-model="queryId"
            placeholder="请输入元素 ID"
            class="query-input"
            clearable
            @keyup.enter="handleQuery"
          />
          <el-button
            type="primary"
            :loading="loading"
            :disabled="!queryId.trim()"
            @click="handleQuery"
          >
            查询
          </el-button>
        </div>

        <el-alert
          v-if="errorMessage"
          :title="errorMessage"
          type="error"
          show-icon
          class="query-alert"
        />

        <div v-if="result" class="query-result">
          <div class="result-header">元素详情（ID: {{ lastQueriedId }}）</div>
          <pre class="result-pre">{{ formattedResult }}</pre>
        </div>
      </el-col>
    </el-row>

        <el-row class="query-row">
      <el-col :span="24">
        <div class="query-controls">
          <span class="query-label">查询操作记录：</span>
          <el-input
            v-model="opQueryId"
            placeholder="请输入操作记录 ID"
            class="query-input"
            clearable
            @keyup.enter="handleOpQuery"
          />
          <el-button
            type="primary"
            :loading="opLoading"
            :disabled="!opQueryId.trim()"
            @click="handleOpQuery"
          >
            查询
          </el-button>
        </div>

        <el-alert
          v-if="opErrorMessage"
          :title="opErrorMessage"
          type="error"
          show-icon
          class="query-alert"
        />

        <div v-if="opResult" class="query-result">
          <div class="result-header">操作记录（ID: {{ lastOpQueryId }}）</div>
          <pre class="result-pre">{{ formattedOpResult }}</pre>
        </div>
      </el-col>
    </el-row>

-------------------------------------
            <br>
            <router-link :to="{ name: 'DetailPage', params: { id: 10002491 } }" target="_blank">  
              查看10002491段落
            </router-link>
--
<router-link :to="{ name: 'DetailPage', params: { id: 10000003 } }" target="_blank">  
              查看10000003文章
            </router-link>
--
<router-link :to="{ name: 'DetailPage', params: { id: 10000004 } }" target="_blank">  
              查看10000004物品
            </router-link>
--
<router-link :to="{ name: 'DetailPage', params: { id: 10000005 } }" target="_blank">  
              查看10000005标签
            </router-link>
--
<router-link :to="{ name: 'DetailPage', params: { id: 10000006 } }" target="_blank">  
              查看10000006人物
            </router-link>
--
<router-link :to="{ name: 'DetailPage', params: { id: 10000007 } }" target="_blank">  
              查看10000007群组
            </router-link>
--
<router-link :to="{ name: 'DetailPage', params: { id: 10000008 } }" target="_blank">  
              查看10000008契约
            </router-link>
--
<router-link :to="{ name: 'DetailPage', params: { id: 10000009 } }" target="_blank">  
              查看10000009辩论
            </router-link>
--
<router-link :to="{ name: 'DetailPage', params: { id: 10000010 } }" target="_blank">  
              查看10000010选举
            </router-link>
--
            <router-link :to="{ name: 'PS_reply_page', params: { id: 100000001 } }" target="_blank">  
              查看100000001附言
            </router-link>
--
<br>

  </div>
</template>

<script>
import { ref, computed } from 'vue';
import axios from 'axios';
import { ElMessage } from 'element-plus';

const QUERY_ENDPOINT = 'https://www.aworld.wiki/api/iteminfo/show_all_iteminfo/';
const QUERY_OP_ENDPOINT = 'https://www.aworld.wiki/api/opinfo/query_op_by_id/';

export default {
  name: 'SubPage64',
  setup() {
    const queryId = ref('');
    const loading = ref(false);
    const result = ref(null);
    const errorMessage = ref('');
    const lastQueriedId = ref('');

    const formattedResult = computed(() => {
      if (!result.value) {
        return '';
      }
      try {
        return JSON.stringify(result.value, null, 2);
      } catch (error) {
        return String(result.value);
      }
    });

    const opQueryId = ref('');
    const opLoading = ref(false);
    const opResult = ref(null);
    const opErrorMessage = ref('');
    const lastOpQueryId = ref('');

    const formattedOpResult = computed(() => {
      if (!opResult.value) {
        return '';
      }
      try {
        return JSON.stringify(opResult.value, null, 2);
      } catch (error) {
        return String(opResult.value);
      }
    });

    const handleQuery = async () => {
      const trimmedId = queryId.value.trim();
      if (!trimmedId) {
        errorMessage.value = '请输入有效的元素 ID';
        return;
      }

      loading.value = true;
      errorMessage.value = '';
      result.value = null;

      try {
        const response = await axios.post(QUERY_ENDPOINT, { id: trimmedId });
        result.value = response.data;
        lastQueriedId.value = trimmedId;

        if (!response.data || (typeof response.data === 'object' && Object.keys(response.data).length === 0)) {
          ElMessage.warning('查询成功，但未返回元素信息');
        } else {
          ElMessage.success('查询成功');
        }
      } catch (error) {
        const message = error?.response?.data?.message || '查询失败，请稍后重试';
        errorMessage.value = message;
        ElMessage.error(message);
      } finally {
        loading.value = false;
      }
    };

    const handleOpQuery = async () => {
      const trimmedId = opQueryId.value.trim();
      if (!trimmedId) {
        opErrorMessage.value = '请输入有效的操作记录 ID';
        return;
      }

      opLoading.value = true;
      opErrorMessage.value = '';
      opResult.value = null;

      try {
        const response = await axios.post(QUERY_OP_ENDPOINT, { op_id: trimmedId });
        opResult.value = response.data;
        lastOpQueryId.value = trimmedId;

        const success = response.data?.success;
        const payload = response.data?.data;
        if (success === false) {
          const message = response.data?.message || response.data?.error || '查询失败';
          opErrorMessage.value = message;
          ElMessage.warning(message);
        } else if (success === true || payload) {
          opErrorMessage.value = '';
          ElMessage.success(response.data?.message || '查询成功');
        } else {
          const message = '查询成功，但未返回记录';
          opErrorMessage.value = message;
          ElMessage.warning(message);
        }
      } catch (error) {
        const message = error?.response?.data?.error || error?.response?.data?.message || '查询失败，请稍后重试';
        opErrorMessage.value = message;
        ElMessage.error(message);
      } finally {
        opLoading.value = false;
      }
    };

    return {
      queryId,
      loading,
      result,
      errorMessage,
      lastQueriedId,
      formattedResult,
      handleQuery,
      opQueryId,
      opLoading,
      opResult,
      opErrorMessage,
      lastOpQueryId,
      formattedOpResult,
      handleOpQuery
    };
  }
};
</script>

<style scoped>
.subpage64 {
  width: 100%;
}

.query-row {
  margin-top: 32px;
  padding: 0 12px;
}

.query-controls {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: nowrap;
}

.query-label {
  font-size: 18px;
  font-weight: 600;
  white-space: nowrap;
}

.query-input {
  flex: 1;
  min-width: 220px;
}

.query-alert {
  margin-top: 16px;
  max-width: 540px;
}

.query-alert :deep(.el-alert__content) {
  white-space: nowrap;
}

.query-result {
  margin-top: 20px;
  max-width: 900px;
  border: 1px solid #dcdfe6;
  border-radius: 8px;
  background: #f6f9ff;
  padding: 16px;
}

.result-header {
  font-weight: 600;
  margin-bottom: 12px;
  color: #303133;
}

.result-pre {
  margin: 0;
  font-size: 13px;
  line-height: 1.6;
  white-space: pre-wrap;
  word-break: break-word;
  color: #2f3b52;
}

@media (max-width: 540px) {
  .query-controls {
    flex-wrap: wrap;
  }
}
</style>
