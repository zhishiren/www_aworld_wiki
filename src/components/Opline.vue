<template>
  <div class="opline">
    <div class="opline-group" v-if="visibleActions.length">
      <template v-for="(action, index) in visibleActions" :key="action.key">
        <el-button
          type="info"
          text
          class="custom-button"
          :disabled="action.disabled"
          @click="action.onClick()"
        >
          <el-icon v-if="action.icon" class="my-icon"><component :is="action.icon" /></el-icon>
          {{ action.label }}
        </el-button>
        <el-divider
          direction="vertical"
          class="opline-divider"
        />
      </template>
      <FeedbackMessage
        v-if="createShowFeedback"
        :message="createFeedbackMessage"
        :show="createShowFeedback"
        class="feedback-inline"
      />
      <FeedbackMessage
        v-if="opShowFeedback"
        :message="opFeedbackMessage"
        :show="opShowFeedback"
        class="feedback-inline"
      />
    </div>

    <el-dialog v-model="createDialogs.add" title="新增各种元素" :append-to-body="true" width="25%">
      <el-form ref="createAddFormRef" :model="createForms.add">
        <el-form-item :label="`${props.propitemtype}标题:`">
          <el-input v-model="createForms.add.itemtitle" placeholder="请输入该元素的标题或名称" style="width: 300px;" />
        </el-form-item>
        <el-form-item label="属性分类:" v-if="props.propitemtype === '文章' || props.propitemtype === '段落'">
          <el-select v-model="createForms.add.itemsubtype" placeholder="请选择该元素的属性分类" style="width: 300px;">
            <template v-if="props.propitemtype === '文章'">
              <el-option v-for="item in createItemtypeOptions1" :key="item.value" :label="item.label" :value="item.value" />
            </template>
            <template v-else>
              <el-option v-for="item in createItemtypeOptions2" :key="item.value" :label="item.label" :value="item.value" />
            </template>
          </el-select>
        </el-form-item>
        <el-form-item prop="itemcontent">
          <CustomInput v-model="createForms.add.itemcontent" style="width: 400px;" />
        </el-form-item>
      </el-form>

      <el-divider>
        <span class="dialog-footer-text">
          <a class="my-icon" @click="submitCreateForm('additem')">提交</a>
          <el-divider direction="vertical" class="opline-divider" />
          <a class="my-icon" @click="createDialogs.add = false">取消</a>
        </span>
      </el-divider>
    </el-dialog>

    <el-dialog
      v-model="speakDialogs.speak"
      title="用户发言功能"
      width="25%"
      :append-to-body="true"
      :lock-scroll="false"
    >
      <el-form ref="speakFormRef" :model="speakForms.speak">
        <el-form-item label="是否匿名:">
          <el-switch v-model="speakForms.speak.isAnonymous" />
        </el-form-item>
        <el-form-item label="是否加密:">
          <el-switch v-model="speakForms.speak.isEncrypted" />
        </el-form-item>
        <template v-if="speakForms.speak.isEncrypted">
          <el-form-item label="发言密码:">
            <el-input v-model="speakForms.speak.password" type="password" placeholder="请输入本次发言的密码" style="width: 300px;" />
          </el-form-item>
          <el-form-item label="密码提示:">
            <el-input v-model="speakForms.speak.passwordHint" placeholder="请输入密码提示,所有人可见" style="width: 300px;" />
          </el-form-item>
        </template>
        <el-form-item label="发言类型:">
          <el-select v-model="speakForms.speak.subtype" placeholder="请选择发言的态度" style="width: 300px;">
            <el-option v-for="item in speakSubtypeOptions" :key="item.value" :label="item.label" :value="item.value" />
          </el-select>
        </el-form-item>
        <el-form-item label="公开范围:">
          <el-select
            v-model="speakForms.speak.publicRange"
            placeholder="请选择公开范围"
            style="width: 300px;"
            @focus="loadSpeakPublicRangeOptions"
          >
            <el-option v-for="option in speakPublicRangeOptions" :key="option.value" :label="option.label" :value="option.value" />
          </el-select>
        </el-form-item>
        <el-form-item prop="content">
          <CustomInput v-model="speakForms.speak.content" style="width: 400px;" />
        </el-form-item>
      </el-form>

      <el-divider>
        <span class="dialog-footer-text">
          <a class="my-icon" @click="submitSpeakForm">提交</a>
          <el-divider direction="vertical" class="opline-divider" />
          <a class="my-icon" @click="speakDialogs.speak = false">取消</a>
        </span>
      </el-divider>
      <FeedbackMessage :message="speakFeedbackMessage" :show="speakShowFeedback" />
    </el-dialog>

    <el-dialog v-model="opDialogVisible" :title="`${opDialogTitle}的相关选项`" width="25%" :append-to-body="true">
      <el-form :model="opForm" ref="opFormRef">
        <el-form-item label="是否匿名:" v-if="opShowAnonymous">
          <el-switch v-model="opForm.isAnonymous" />
        </el-form-item>
        <el-form-item label="是否加密:" v-if="opShowEncrypted">
          <el-switch v-model="opForm.isEncrypted" />
        </el-form-item>
        <template v-if="opForm.isEncrypted">
          <el-form-item label="发言密码：">
            <el-input v-model="opForm.password" type="password" placeholder="发言码，限6位数字" style="width: 300px;" />
          </el-form-item>
          <el-form-item label="密码提示：">
            <el-input v-model="opForm.passwordHint" placeholder="密码提示，限10个字" style="width: 300px;" />
          </el-form-item>
        </template>

        <el-form-item label="属性分类：" prop="subtype" v-if="opShowSubtype">
          <el-select v-model="opForm.subtype" placeholder="请选择你的态度" style="width: 300px;">
            <el-option v-for="option in opSubtypeOptions" :key="option.value" :label="option.label" :value="option.value" />
          </el-select>
        </el-form-item>

        <el-form-item label="公开范围：" prop="publicRange" v-if="opShowPublicRange">
          <el-select
            v-model="opForm.publicRange"
            placeholder="请选择公开范围"
            style="width: 300px;"
            @focus="loadOpPublicRangeOptions"
          >
            <el-option v-for="option in opPublicRangeOptions" :key="option.value" :label="option.label" :value="option.value" />
          </el-select>
        </el-form-item>
        <el-form-item label="选择标签：" prop="mylabel" v-if="opShowMyLabel">
          <el-select
            v-model="opForm.mylabel"
            placeholder="请选择你的标签"
            style="width: 300px;"
            @focus="loadOpMyLabelOptions"
            @change="(value) => (opForm.item1id = value)"
          >
            <el-option v-for="option in opMyLabelOptions" :key="option.value" :label="option.label" :value="option.value" />
          </el-select>
        </el-form-item>

        <el-form-item label="关联元素ID:" v-if="opShowConnectId">
          <el-input v-model="opForm.item1id" placeholder="请输入关联元素ID号" style="width: 300px;" />
        </el-form-item>

        <el-form-item label="附言内容:" v-if="opShowContent">
          <CustomInput
            v-model="opForm.content"
            style="width: 400px;"
            :placeholder="opContentPlaceholder"
          />
        </el-form-item>
      </el-form>

      <el-divider>
        <span class="dialog-footer-text">
          <a class="my-icon" @click="submitOpForm">提交</a>
          <el-divider direction="vertical" class="opline-divider" />
          <a class="my-icon" @click="opDialogVisible = false">取消</a>
        </span>
      </el-divider>
    </el-dialog>

    <template v-if="showExpandline">
      <div class="expandline">
        <el-button type="info" text class="label-button" @click.prevent>
          <span class="button-text">{{ expandText }}</span>
        </el-button>
        <el-divider direction="vertical" class="opline-divider" />
        <el-button
          type="info"
          text
          class="custom-button"
          :loading="expandLoading"
          @click="handleExpandClick"
        >
          <el-icon v-if="resolvedExpandIcon" class="my-icon compact-icon"><component :is="resolvedExpandIcon" /></el-icon>
          <span class="button-text">{{ expandButtonText }}</span>
        </el-button>
      </div>
    </template>
  </div>
</template>

<script setup>
import { computed, reactive, ref } from 'vue'
import axios from 'axios'
import { ElMessage } from 'element-plus'
import CustomInput from './CustomInput.vue'
import FeedbackMessage from './FeedbackMessage.vue'

import { Plus, Star, Comment, Share, Microphone, Refresh, Expand } from '@element-plus/icons-vue'

const normalizeActionInput = (value) => {
  if (Array.isArray(value)) {
    return value
      .filter((item) => typeof item === 'string' && item.trim())
      .map((item) => item.trim())
  }
  if (typeof value === 'string') {
    return value
      .split(',')
      .map((item) => item.trim())
      .filter((item) => item)
  }
  return []
}

const props = defineProps({
  actions: { type: [Array, String], default: () => [] },
  expandText: { type: String, default: '' },
  expandLoading: { type: Boolean, default: false },
  showprops: { type: String, default: '' },
  propitemtype: { type: String, default: '111' },
  itemObject: { type: Object, default: () => ({}) }
})

const emit = defineEmits(['expand', 'click', 'refreshList', 'refresh-list', 'action'])

const normalizedActionKeys = computed(() => {
  const provided = normalizeActionInput(props.actions)
  if (provided.length) return provided
  return []
})

const showExpandline = computed(() => Boolean(props.expandText))

const isExpanded = ref(false)

const expandButtonText = computed(() => (isExpanded.value ? '刷新' : '展开'))

const resolvedExpandIcon = computed(() => (isExpanded.value ? Refresh : Expand))

const handleExpandClick = () => {
  if (!isExpanded.value) {
    isExpanded.value = true
    emit('expand')
  } else {
    emit('refreshList')
    emit('refresh-list')
  }
  emit('click')
}

function buildUserContext() {
  return {
    userid: localStorage.getItem('userid'),
    username: localStorage.getItem('username')
  }
}

function createAddDefaults() {
  return {
    itemsubtype: '',
    itemtitle: '',
    itemcontent: ''
  }
}

const createDialogs = reactive({ add: false })
const createForms = reactive({
  add: createAddDefaults()
})
const createFeedbackMessage = ref('')
const createShowFeedback = ref(false)
const createAddFormRef = ref(null)

const createItemtypeOptions1 = [
  { value: 'Opt1', label: 'Option1' },
  { value: 'Opt2', label: 'Option2' },
  { value: 'Opt3', label: 'Option3' },
  { value: 'Opt4', label: 'Option4' },
  { value: 'Opt5', label: 'Option5' }
]
const createItemtypeOptions2 = [
  { value: 'Opt1', label: 'Option1' },
  { value: 'Opt2', label: 'Option2' },
  { value: 'Opt3', label: 'Option3' },
  { value: 'Opt4', label: 'Option4' },
  { value: 'Opt5', label: 'Option5' }
]

const createFeedbackTimeout = () => {
  setTimeout(() => {
    createShowFeedback.value = false
  }, 3000)
}

const submitCreateForm = (formName) => {
  if (formName === 'additem') {
    createFeedbackMessage.value = '新增逻辑暂未实现'
    createShowFeedback.value = true
    createDialogs.add = false
    createFeedbackTimeout()
  }
}

function speakFormDefaults() {
  return {
    isEncrypted: false,
    isAnonymous: false,
    password: '',
    passwordHint: '',
    content: '',
    subtype: '',
    publicRange: 99999999
  }
}

const speakDialogs = reactive({ speak: false })
const speakForms = reactive({
  speak: speakFormDefaults()
})
const speakFeedbackMessage = ref('')
const speakShowFeedback = ref(false)
const speakFormRef = ref(null)
const speakPublicRangeOptions = ref([{ label: '所有用户', value: 99999999 }])
const speakSubtypeOptions = [
  { value: '求助启示', label: '求助启示' },
  { value: '时事新闻', label: '时事新闻' },
  { value: '紧急通知', label: '紧急通知' },
  { value: '感悟思考', label: '感悟思考' },
  { value: '名人名言', label: '名人名言' },
  { value: '经验分享', label: '经验分享' },
  { value: '行动实践', label: '行动实践' },
  { value: '重要公告', label: '重要公告' }
]

const loadSpeakPublicRangeOptions = async () => {
  const payload = {
    user_id: localStorage.getItem('userid'),
    op_type: '获取范围值'
  }
  try {
    const response = await axios.post('https://www.aworld.wiki/api/opinfo/get_oplist/', payload)
    const dynamic = response.data.map((item) => ({ label: item.item0title, value: item.item0id }))
    speakPublicRangeOptions.value = [
      { label: '所有用户', value: 99999999 },
      { label: '仅我本人', value: 10000000 },
      ...dynamic
    ]
  } catch (error) {
    speakFeedbackMessage.value = '加载失败，请重试'
    speakShowFeedback.value = true
  }
}

const resetSpeakForm = () => {
  Object.assign(speakForms.speak, speakFormDefaults())
}

const submitSpeakForm = () => {
  sendSpeakData()
}

const sendSpeakData = async () => {
  if (speakForms.speak.isEncrypted && (!speakForms.speak.password || !speakForms.speak.passwordHint)) {
    speakFeedbackMessage.value = '密码和提示不能为空'
    speakShowFeedback.value = true
    return
  }
  if (!speakForms.speak.content.trim()) {
    speakFeedbackMessage.value = '内容不能为空'
    speakShowFeedback.value = true
    return
  }

  const payload = {
    isEncrypted: speakForms.speak.isEncrypted,
    isAnonymous: speakForms.speak.isAnonymous,
    password: speakForms.speak.password,
    passwordHint: speakForms.speak.passwordHint,
    content: speakForms.speak.content,
    subtype: speakForms.speak.subtype,
    publicRange: speakForms.speak.publicRange,
    userid: localStorage.getItem('userid'),
    username: localStorage.getItem('username')
  }

  try {
    const response = await axios.post('https://www.aworld.wiki/api/iteminfo/add_speak/', payload)
    speakFeedbackMessage.value = response.data.message || '提交成功'
    speakShowFeedback.value = true
    speakDialogs.speak = false
    emit('refreshList')
    emit('refresh-list')
  } catch (error) {
    speakFeedbackMessage.value = '提交失败，请稍后重试'
    speakShowFeedback.value = true
  } finally {
    resetSpeakForm()
    setTimeout(() => {
      speakShowFeedback.value = false
    }, 3000)
  }
}

const opFeedbackMessage = ref('')
const opShowFeedback = ref(false)
const opDialogVisible = ref(false)
const opDialogTitle = ref('')

function opFormDefaults() {
  return {
    subtype: '',
    publicRange: 99999999,
    content: '',
    itemtype: '',
    item0id: 0,
    item0title: '',
    item0type: '',
    item1id: 0,
    mylabel: null,
    isAnonymous: false,
    isEncrypted: false,
    password: '',
    passwordHint: '',
    ...buildUserContext()
  }
}

const opForm = reactive(opFormDefaults())
const opFormRef = ref(null)

const opDialogDefaultSchema = {
  showSubtype: false,
  showPublicRange: false,
  showMyLabel: false,
  showConnectId: false,
  showEncrypted: false,
  showAnonymous: false,
  showContent: true,
  requireContent: false,
  requireTagSelection: false,
  requireConnectId: false,
  placeholder: '',
  subtypeOptions: []
}

const opDialogSchemas = {
  评论: {
    showSubtype: true,
    showPublicRange: true,
    showEncrypted: true,
    showAnonymous: true,
    requireContent: true,
    placeholder: '请输入评论内容',
    subtypeOptions: [
      { label: '支持肯定', value: '支持肯定' },
      { label: '反对异议', value: '反对异议' },
      { label: '另类解释', value: '另类解释' },
      { label: '细化补充', value: '细化补充' },
      { label: '提问质疑', value: '提问质疑' },
      { label: '其他', value: '其他' }
    ]
  },
  分享: {
    showSubtype: true,
    showPublicRange: true,
    placeholder: '请输入分享内容',
    subtypeOptions: [{ label: '强烈推荐', value: '强烈推荐' }]
  },
  关联: {
    showSubtype: true,
    showConnectId: true,
    requireConnectId: true,
    placeholder: '请输入关联说明',
    subtypeOptions: [
      { label: '互相佐证', value: '互相佐证' },
      { label: '互相矛盾', value: '互相矛盾' },
      { label: '补充细化', value: '补充细化' },
      { label: '概括总结', value: '概括总结' }
    ]
  },
  纠错: {
    showSubtype: true,
    requireContent: true,
    placeholder: '请输入纠错内容',
    subtypeOptions: [
      { label: '整体事实', value: '整体事实' },
      { label: '文字表达', value: '文字表达' },
      { label: '部分细节', value: '部分细节' }
    ]
  },
  举报: {
    showSubtype: true,
    showAnonymous: true,
    requireContent: true,
    placeholder: '请输入举报说明',
    subtypeOptions: [
      { label: '造谣传谣', value: '造谣传谣' },
      { label: '暴力色情', value: '暴力色情' },
      { label: '霸凌他人', value: '霸凌他人' },
      { label: '盈利广告', value: '盈利广告' },
      { label: '其他行为', value: '其他行为' }
    ]
  },
  加标签: {
    showMyLabel: true,
    requireTagSelection: true,
    placeholder: '请输入标签附言'
  },
  关注: {
    showSubtype: true,
    showContent: false,
    subtypeOptions: [{ label: '特别关注', value: '特别关注' }]
  },
  屏蔽: {
    showAnonymous: true,
    placeholder: '请输入屏蔽原因'
  },
  加入: {
    placeholder: '请输入加入说明'
  }
}

const opDialogConfig = computed(() => ({
  ...opDialogDefaultSchema,
  ...(opDialogSchemas[opDialogTitle.value] || {})
}))

const opShowSubtype = computed(() => opDialogConfig.value.showSubtype)
const opShowPublicRange = computed(() => opDialogConfig.value.showPublicRange)
const opShowMyLabel = computed(() => opDialogConfig.value.showMyLabel)
const opShowConnectId = computed(() => opDialogConfig.value.showConnectId)
const opShowEncrypted = computed(() => opDialogConfig.value.showEncrypted)
const opShowAnonymous = computed(() => opDialogConfig.value.showAnonymous)
const opShowContent = computed(() => opDialogConfig.value.showContent)
const opSubtypeOptions = computed(() => opDialogConfig.value.subtypeOptions)
const opPublicRangeOptions = ref([{ label: '所有用户', value: 99999999 }])
const opMyLabelOptions = ref([])
const opContentPlaceholder = computed(() => opDialogConfig.value.placeholder || `请输入${opDialogTitle.value}的内容`)

const loadOpMyLabelOptions = async () => {
  const payload = {
    user_id: localStorage.getItem('userid'),
    op_type: '获取我的标签'
  }
  try {
    const response = await axios.post('https://www.aworld.wiki/api/opinfo/get_oplist/', payload)
    opMyLabelOptions.value = response.data.map((item) => ({ label: item.item0title, value: item.item0id }))
  } catch (error) {
    opFeedbackMessage.value = '加载标签失败，请重试'
    opShowFeedback.value = true
  }
}

const loadOpPublicRangeOptions = async () => {
  const payload = {
    user_id: localStorage.getItem('userid'),
    op_type: '获取范围值'
  }
  try {
    const response = await axios.post('https://www.aworld.wiki/api/opinfo/get_oplist/', payload)
    const dynamic = response.data.map((item) => ({ label: item.item0title, value: item.item0id }))
    opPublicRangeOptions.value = [
      { label: '所有用户', value: 99999999 },
      { label: '仅我本人', value: 10000000 },
      ...dynamic
    ]
  } catch (error) {
    opFeedbackMessage.value = '加载范围失败，请重试'
    opShowFeedback.value = true
  }
}

const resetOpForm = () => {
  Object.assign(opForm, opFormDefaults())
}

const showOpDialog = (text) => {
  resetOpForm()
  opDialogTitle.value = text
  opDialogVisible.value = true
  opForm.itemtype = text
  opForm.item0id = props.itemObject?.item_id ?? 0
  opForm.item0type = props.itemObject?.item_type ?? ''
  opForm.item0title = props.itemObject?.item_type === '段落'
    ? `${props.itemObject?.sparefield1 ?? ''}${props.itemObject?.item_title ?? ''}`
    : props.itemObject?.item_title ?? ''
}

const submitOpForm = async () => {
  const dialogConfig = opDialogConfig.value

  if (dialogConfig.requireTagSelection && !opForm.item1id) {
    ElMessage.error('加标签值不能为空')
    return
  }
  if (dialogConfig.requireConnectId && !opForm.item1id) {
    ElMessage.error('关联ID不能为空')
    return
  }
  if (opForm.isEncrypted && (!opForm.password || !opForm.passwordHint)) {
    ElMessage.error('密码和提示不能为空')
    return
  }
  if (dialogConfig.requireContent && !(opForm.content || '').trim()) {
    const messageMap = {
      评论: '评论内容不能为空',
      纠错: '纠错内容不能为空',
      举报: '举报内容不能为空'
    }
    ElMessage.error(messageMap[opDialogTitle.value] || '内容不能为空')
    return
  }

  const payload = {
    username: localStorage.getItem('username'),
    userid: localStorage.getItem('userid'),
    ...opForm
  }

  try {
    const response = await axios.post('https://www.aworld.wiki/api/opinfo/add_op/', payload)
    if (response.data.success) {
      opFeedbackMessage.value = response.data.message || '提交成功'
      opShowFeedback.value = true
      opDialogVisible.value = false
    } else {
      opFeedbackMessage.value = response.data.message || '提交失败'
      opShowFeedback.value = true
    }
  } catch (error) {
    opFeedbackMessage.value = '提交失败，请稍后重试'
    opShowFeedback.value = true
  } finally {
    resetOpForm()
    setTimeout(() => {
      opShowFeedback.value = false
      opFeedbackMessage.value = ''
    }, 3000)
  }
}

const visibleActions = computed(() =>
  normalizedActionKeys.value
    .map((key) => {
      switch (key) {
        case '新增':
          return {
            key,
            label: '新增',
            icon: Plus,
            disabled: false,
            onClick: () => {
              createDialogs.add = true
            }
          }
        case '发言':
          return {
            key,
            label: '发言',
            icon: Microphone,
            disabled: false,
            onClick: () => {
              speakDialogs.speak = true
            }
          }
        case '立论':
          return {
            key,
            label: '立论',
            icon: Microphone,
            disabled: false,
            onClick: () => emit('action', '立论')
          }
        case '换一批':
          return {
            key,
            label: '换一批',
            icon: Refresh,
            disabled: false,
            onClick: () => emit('action', '换一批')
          }
        case '加入':
          return {
            key,
            label: '加入',
            icon: Plus,
            disabled: false,
            onClick: () => showOpDialog('加入')
          }
        case '关注':
          return {
            key,
            label: '关注',
            icon: Star,
            disabled: false,
            onClick: () => showOpDialog('关注')
          }
        case '评论':
          return {
            key,
            label: '评论',
            icon: Comment,
            disabled: false,
            onClick: () => showOpDialog('评论')
          }
        case '分享':
          return {
            key,
            label: '分享',
            icon: Share,
            disabled: false,
            onClick: () => showOpDialog('分享')
          }
        case '顶':
          return {
            key,
            label: '顶',
            icon: null,
            disabled: false,
            onClick: () => emit('action', '顶')
          }
        case '踩':
          return {
            key,
            label: '踩',
            icon: null,
            disabled: false,
            onClick: () => emit('action', '踩')
          }
        default:
          return null
      }
    })
    .filter(Boolean)
)
</script>

<style scoped>
.opline {
  display: inline-flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 0;
}

.opline-group,
.expandline {
  display: inline-flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 0;
}

.custom-button {
  display: inline-flex;
  align-items: center;
  font-size: 18px;
  padding: 0;
  margin: 0;
}

.label-button {
  display: inline-flex;
  align-items: center;
  padding: 0;
  margin: 0;
  pointer-events: none;
  color: #909399;
}

.button-text {
  margin: 0;
  padding: 0;
  font-size: 18px;
  color: inherit;
}

.my-icon {
  display: inline-flex;
  align-items: center;
  font-size: 18px;
  margin-right: 0px;
}

.compact-icon {
  margin-right: 0;
}

.opline-divider {
  margin: 0 8px;
  height: 22px;
}

.dialog-footer-text {
  display: inline-flex;
  align-items: center;
  gap: 0;
}

.feedback-inline {
  margin-left: 8px;
  color: #909399;
}

.opline :deep(.el-form-item__label) {
  font-size: 18px;
}

.opline :deep(.el-dialog__body) {
  font-size: 16px;
}
</style>
