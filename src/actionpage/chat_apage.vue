<template>
    <div class="chat-wrapper">
        <HelloLogout></HelloLogout>
        <el-row class="firstrow">
            <el-col :span="3"></el-col>
            <el-col :span="18" class="bgcolor_menu_FC">
                <p>这是与其他用户聊天的页面。</p>
            </el-col>
            <el-col :span="3"></el-col>
        </el-row>

        <el-row>
            <el-col :span="3">
                <el-menu :default-active="activeSubIndex0" class="el-menu-vertical-demo bgcolor_menu_FC"
                    @select="subhandleSelect0">
                    <el-menu-item index="01" class="menu-item18">
                        <span>一对一聊</span>
                    </el-menu-item>
                    <el-menu-item index="02" class="menu-item18">
                        <span>群组内聊</span>
                    </el-menu-item>
                    <el-menu-item index="03" class="menu-item18">
                        <span>聊天大厅</span>
                    </el-menu-item>
                    <el-menu-item index="04" class="menu-item18">
                        <span>精华发言</span>
                    </el-menu-item>
                </el-menu>
            </el-col>

            <el-col :span="21" v-if="activeSubIndex0 === '01'">
                <el-row :gutter="20" class="chat-section">
                    <el-col :span="14">
                        <el-card shadow="always" class="panel-card chat-card">
                            <div class="panel-title">
                                <span v-if="activeDirect">{{ activeDirect.alias }}</span>
                                <span v-else>请选择联系人</span>
                                <span v-if="activeDirect" class="panel-subtitle">#{{ activeDirect.id }} ｜ 初次联系于 {{ activeDirect.firstContact }}</span>
                            </div>
                            <div v-if="directMessages.length" class="message-area">
                                <div v-for="msg in directMessages" :key="msg.id"
                                    :class="['message-wrap', { 'from-user': msg.from === 'me' }]">
                                    <div class="message-bubble">
                                        <div class="message-text">{{ msg.text }}</div>
                                        <div class="timestamp">{{ msg.time }}</div>
                                    </div>
                                </div>
                            </div>
                            <div v-else class="empty-hint">请选择左侧联系人查看历史消息。</div>
                            <div class="reply-box">
                                <el-input v-model="draftDirectMessage" type="textarea"
                                    :autosize="{ minRows: 2, maxRows: 4 }" placeholder="这里暂时使用固定示例数据，发送按钮仅做展示"></el-input>
                                <el-button class="send-btn" type="primary" disabled>发送</el-button>
                            </div>
                        </el-card>
                    </el-col>

                    <el-col :span="7">
                        <el-card shadow="always" class="panel-card">
                            <div class="panel-title">私聊联系人</div>
                            <el-input v-model="userSearchTerm" style="width: 100%;"
                                placeholder="请输入用户ID号或名称"
                                class="input-with-select">
                                <template #append>
                                    <el-button type="primary" disabled>查</el-button>
                                </template>
                            </el-input>
                            <div class="chat-list">
                                <div v-for="contact in filteredDirectContacts" :key="contact.id"
                                    :class="['chat-list-item', { active: activeDirectId === contact.id }]"
                                    @click="selectDirectChat(contact.id)">
                                    <div class="chat-list-top">
                                        <span class="chat-avatar" :style="{ backgroundColor: contact.avatarColor }">
                                            {{ getInitial(contact.name) }}
                                        </span>
                                        <div class="chat-name-meta">
                                            <span class="chat-name">{{ contact.alias }}</span>
                                            <span class="chat-id">#{{ contact.id }}</span>
                                        </div>
                                        <el-tag size="small" :type="contact.badgeType">{{ contact.badge }}</el-tag>
                                    </div>
                                    <div class="chat-list-summary">
                                        {{ contact.summary }}
                                    </div>
                                    <div class="chat-list-footer">
                                        <span>{{ contact.lastMessage }}</span>
                                        <el-tag v-if="contact.unread" size="small" type="danger" effect="plain">
                                            未读 {{ contact.unread }}
                                        </el-tag>
                                    </div>
                                </div>
                            </div>
                        </el-card>
                    </el-col>
                </el-row>
            </el-col>

            <el-col :span="21" v-if="activeSubIndex0 === '02'">
                <el-row :gutter="20" class="chat-section">
                    <el-col :span="7">
                        <el-card shadow="always" class="panel-card">
                            <div class="panel-title">我的群组</div>
                            <el-input v-model="groupSearchTerm" style="width: 100%;"
                                placeholder="请输入群组名称或ID"
                                class="input-with-select">
                                <template #append>
                                    <el-button type="primary" disabled>查</el-button>
                                </template>
                            </el-input>
                            <div class="chat-list">
                                <div v-for="group in filteredGroupChats" :key="group.id"
                                    :class="['chat-list-item', { active: activeGroupId === group.id }]"
                                    @click="selectGroupChat(group.id)">
                                    <div class="chat-list-top">
                                        <span class="chat-avatar" :style="{ backgroundColor: group.avatarColor }">
                                            {{ getInitial(group.name) }}
                                        </span>
                                        <div class="chat-name-meta">
                                            <span class="chat-name">{{ group.name }}</span>
                                            <span class="chat-id">#{{ group.id }}</span>
                                        </div>
                                        <el-tag size="small" :type="group.badgeType">{{ group.badge }}</el-tag>
                                    </div>
                                    <div class="chat-list-summary">
                                        最近讨论：{{ group.latestTopic }}
                                    </div>
                                    <div class="chat-list-footer">
                                        <span>{{ group.lastMessage }}</span>
                                        <span>参与者 {{ group.members }}</span>
                                    </div>
                                </div>
                            </div>
                        </el-card>
                    </el-col>

                    <el-col :span="10">
                        <el-card shadow="always" class="panel-card chat-card">
                            <div class="panel-title">
                                <span v-if="activeGroup">{{ activeGroup.name }}</span>
                                <span v-else>请选择群组</span>
                                <span v-if="activeGroup" class="panel-subtitle">{{ activeGroup.description }}</span>
                            </div>
                            <div v-if="groupMessages.length" class="message-area">
                                <div v-for="msg in groupMessages" :key="msg.id"
                                    :class="['message-wrap', { 'from-user': msg.from === 'me' }]">
                                    <div class="message-bubble">
                                        <div class="message-author" v-if="msg.from !== 'me'">{{ msg.author }}</div>
                                        <div class="message-text">{{ msg.text }}</div>
                                        <div class="timestamp">{{ msg.time }}</div>
                                    </div>
                                </div>
                            </div>
                            <div v-else class="empty-hint">选择左侧群组查看最近发言。</div>
                            <div class="reply-box">
                                <el-input v-model="draftGroupMessage" type="textarea"
                                    :autosize="{ minRows: 2, maxRows: 4 }" placeholder="示例界面暂不支持发送"></el-input>
                                <el-button class="send-btn" type="primary" disabled>群发</el-button>
                            </div>
                        </el-card>
                    </el-col>

                    <el-col :span="4">
                        <el-card shadow="always" class="panel-card">
                            <div class="panel-title">群组概览</div>
                            <template v-if="activeGroup">
                                <p class="overview-line"><span class="label">主持人：</span>{{ activeGroup.host }}</p>
                                <p class="overview-line"><span class="label">建立：</span>{{ activeGroup.created }}</p>
                                <p class="overview-line"><span class="label">节奏：</span>{{ activeGroup.cadence }}</p>
                                <div class="overview-tags">
                                    <el-tag v-for="tag in activeGroup.tags" :key="tag" size="small" effect="plain">
                                        {{ tag }}
                                    </el-tag>
                                </div>
                                <el-divider></el-divider>
                                <p class="dense-text">{{ activeGroup.notes }}</p>
                            </template>
                            <template v-else>
                                <p class="dense-text">左侧选择一个群组，可查看入群说明与近期亮点。</p>
                            </template>
                        </el-card>
                    </el-col>
                </el-row>
            </el-col>

            <el-col :span="21" v-if="activeSubIndex0 === '03'">
                <el-row :gutter="20" class="chat-section">
                    <el-col :span="10" v-for="highlight in lobbyHighlights" :key="highlight.id">
                        <el-card shadow="hover" class="panel-card highlight-card">
                            <div class="panel-title">
                                {{ highlight.title }}
                                <el-tag class="ml6" size="small" :type="highlight.tagType" effect="plain">
                                    {{ highlight.tag }}
                                </el-tag>
                            </div>
                            <p class="dense-text">{{ highlight.snippet }}</p>
                            <div class="highlight-meta">
                                <span>实时在线：{{ highlight.participants }}</span>
                                <span>{{ highlight.time }}</span>
                            </div>
                        </el-card>
                    </el-col>
                </el-row>
            </el-col>

            <el-col :span="21" v-if="activeSubIndex0 === '04'">
                <el-row :gutter="20" class="chat-section">
                    <el-col :span="10" v-for="speech in featuredSpeeches" :key="speech.id">
                        <el-card shadow="hover" class="panel-card speech-card">
                            <div class="panel-title">
                                {{ speech.speaker }}
                                <span class="panel-subtitle">{{ speech.role }}</span>
                            </div>
                            <p class="dense-text">“{{ speech.excerpt }}”</p>
                            <div class="speech-meta">
                                <span>赞同 {{ speech.votes }}</span>
                                <span>回应 {{ speech.comments }}</span>
                                <span>{{ speech.date }}</span>
                            </div>
                            <div class="overview-tags">
                                <el-tag v-for="tag in speech.tags" :key="tag" size="small" effect="plain">
                                    {{ tag }}
                                </el-tag>
                            </div>
                        </el-card>
                    </el-col>
                </el-row>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import { ref, computed } from 'vue';
import HelloLogout from '../components/HelloLogout.vue';

export default {
    name: 'chat_apage',
    components: {
        HelloLogout,
    },
    setup() {
        const activeSubIndex0 = ref('01');
        const userSearchTerm = ref('');
        const groupSearchTerm = ref('');
        const draftDirectMessage = ref('');
        const draftGroupMessage = ref('');

        const directContacts = ref([
            {
                id: '90000001',
                name: 'zhao',
                alias: '赵明远',
                badge: '在线',
                badgeType: 'success',
                lastMessage: '昨天 20:14',
                unread: 2,
                avatarColor: '#60a5fa',
                summary: '协作版块共同维护者，正在跟进“北仓整理”项目。',
                relation: '协作者',
                latestCollab: '“北仓整理”项目统筹',
                firstContact: '2022-03-18',
                tags: ['协同治理', '线下见过'],
                notes: '对于流程安排非常严谨，聊天时喜欢先总结要点再讨论细节。',
                messages: [
                    { id: 'm-1', from: 'them', text: '今天的借阅记录我已经整理好了，晚点发你。', time: '昨天 19:55' },
                    { id: 'm-2', from: 'me', text: '辛苦了！我待会儿补上昨天缺的访客数据。', time: '昨天 20:02' },
                    { id: 'm-3', from: 'them', text: '好的，那周五一起汇总给社群管理员。', time: '昨天 20:10' }
                ]
            },
            {
                id: '90000017',
                name: 'liu',
                alias: '刘晓静',
                badge: '离线',
                badgeType: 'info',
                lastMessage: '两天前 11:08',
                unread: 0,
                avatarColor: '#fbbf24',
                summary: '负责“社区天气播报”，常分享实用信息。',
                relation: '信息提供者',
                latestCollab: '天气播报素材整理',
                firstContact: '2021-11-02',
                tags: ['气象', '生活信息'],
                notes: '习惯用语音留言，文字信息偏简短，回复节奏较快。',
                messages: [
                    { id: 'm-4', from: 'me', text: '今天午后看起来会下小雨，记得推送提醒。', time: '两天前 10:55' },
                    { id: 'm-5', from: 'them', text: '收到～我补上外出注意事项。', time: '两天前 11:02' },
                    { id: 'm-6', from: 'me', text: '谢谢！社区不少人反馈很实用。', time: '两天前 11:08' }
                ]
            },
            {
                id: '90000029',
                name: 'chen',
                alias: '陈固',
                badge: '在线',
                badgeType: 'success',
                lastMessage: '本周一 09:30',
                unread: 1,
                avatarColor: '#34d399',
                summary: '公共物品维修志愿者，负责 3 号工具箱。',
                relation: '志愿伙伴',
                latestCollab: '修复 3 号工具箱',
                firstContact: '2023-05-06',
                tags: ['维修', '志愿者'],
                notes: '喜欢直接上手，对于材料库存特别细致。',
                messages: [
                    { id: 'm-7', from: 'them', text: '周末补货的螺丝已经到仓库了，你有空时验一下数量。', time: '本周一 09:12' },
                    { id: 'm-8', from: 'me', text: '收到，今晚下班过去看。', time: '本周一 09:20' },
                    { id: 'm-9', from: 'them', text: '我把旧零件打包放在工具箱底层，记得回收。', time: '本周一 09:30' }
                ]
            }
        ]);

        const groupChats = ref([
            {
                id: 'g-101',
                name: '公共物品协作群',
                badge: '活跃',
                badgeType: 'success',
                lastMessage: '今天 14:05',
                members: 26,
                avatarColor: '#818cf8',
                latestTopic: '共享投影仪借用流程',
                description: '物资共建小组 · 每周四例会',
                host: '吴老师',
                created: '2020-09-10',
                cadence: '每周例会',
                tags: ['物资共建', '共享工具'],
                notes: '成员偏务实，讨论中会记录行动清单，方便复盘。',
                messages: [
                    { id: 'gm-1', from: 'them', author: '陈固', text: '投影仪这周末要给志愿者培训用，保养完记得登记。', time: '今天 13:42' },
                    { id: 'gm-2', from: 'me', author: '我', text: '周六上午我先拿去测试，下午再送回。', time: '今天 13:58' },
                    { id: 'gm-3', from: 'them', author: '吴老师', text: '辛苦你们，记得备份电源线。', time: '今天 14:05' }
                ]
            },
            {
                id: 'g-204',
                name: '社区天气播报团',
                badge: '更新中',
                badgeType: 'warning',
                lastMessage: '昨天 18:20',
                members: 14,
                avatarColor: '#f87171',
                latestTopic: '本周降雨路径预警',
                description: '社区天气播报 · 实时共享',
                host: '刘晓静',
                created: '2021-05-01',
                cadence: '每日简报',
                tags: ['天气', '对外播报'],
                notes: '富含图表和简讯，适合快速提炼重点。',
                messages: [
                    { id: 'gm-4', from: 'them', author: '刘晓静', text: '今晚 8 点左右有弱对流，户外活动注意。', time: '昨天 18:02' },
                    { id: 'gm-5', from: 'me', author: '我', text: '我把提示文案同步到了公告栏。', time: '昨天 18:11' },
                    { id: 'gm-6', from: 'them', author: '周雨', text: '我会补上湿度和能见度的数据。', time: '昨天 18:20' }
                ]
            }
        ]);

        const lobbyHighlights = ref([
            {
                id: 'hall-1',
                title: '公共物品借阅大厅',
                tag: '协同',
                tagType: 'success',
                snippet: '十字路口分会发起“闲置桌椅再利用”，目前征集中，欢迎提供存放点位。',
                participants: 182,
                time: '5 分钟前'
            },
            {
                id: 'hall-2',
                title: '社区服务汇总墙',
                tag: '互助',
                tagType: 'warning',
                snippet: '今日新增 9 个医疗陪护需求，志愿者可在备注区标注可服务时段。',
                participants: 96,
                time: '17 分钟前'
            },
            {
                id: 'hall-3',
                title: '阅读与记录角',
                tag: '分享',
                tagType: 'info',
                snippet: '“城南小记”整理的阅读清单已上线，小伙伴们给出了 32 条推荐语。',
                participants: 58,
                time: '30 分钟前'
            },
            {
                id: 'hall-4',
                title: '技能交换吧',
                tag: '学习',
                tagType: 'primary',
                snippet: '正在匹配电工基础教学与旧物改造课程，欢迎继续登记可分享技能。',
                participants: 143,
                time: '1 小时前'
            }
        ]);

        const featuredSpeeches = ref([
            {
                id: 'speech-1',
                speaker: '林青禾',
                role: '公共图书管理员',
                excerpt: '想象一下，如果把“借阅归还”变成一个大家共同维护的节奏，每个人都会看见自己的贡献。',
                votes: 68,
                comments: 12,
                date: '2024-07-21 21:30',
                tags: ['公共资源', '透明度']
            },
            {
                id: 'speech-2',
                speaker: '顾擎',
                role: '社区治理顾问',
                excerpt: '好社群并不是没有冲突，而是愿意记录与处理，让每一次矛盾变成迭代的养分。',
                votes: 54,
                comments: 9,
                date: '2024-07-19 19:12',
                tags: ['治理经验', '记录习惯']
            },
            {
                id: 'speech-3',
                speaker: '宋未央',
                role: '共享厨房协调员',
                excerpt: '我们把厨房当成实验室，谁提出新点子，谁就负责一次开放日，欢笑比规则更能让人留下。',
                votes: 41,
                comments: 6,
                date: '2024-07-16 20:45',
                tags: ['共享空间', '运营心得']
            }
        ]);

        const activeDirectId = ref(directContacts.value[0]?.id ?? null);
        const activeGroupId = ref(groupChats.value[0]?.id ?? null);

        const filteredDirectContacts = computed(() => {
            const keyword = userSearchTerm.value.trim().toLowerCase();
            if (!keyword) return directContacts.value;
            return directContacts.value.filter((contact) => {
                return [contact.name, contact.alias, contact.id]
                    .join(' ')
                    .toLowerCase()
                    .includes(keyword);
            });
        });

        const filteredGroupChats = computed(() => {
            const keyword = groupSearchTerm.value.trim().toLowerCase();
            if (!keyword) return groupChats.value;
            return groupChats.value.filter((group) => {
                return [group.name, group.id, group.latestTopic]
                    .join(' ')
                    .toLowerCase()
                    .includes(keyword);
            });
        });

        const activeDirect = computed(() =>
            directContacts.value.find((contact) => contact.id === activeDirectId.value) || null
        );

        const directMessages = computed(() => activeDirect.value?.messages ?? []);

        const activeGroup = computed(() =>
            groupChats.value.find((group) => group.id === activeGroupId.value) || null
        );

        const groupMessages = computed(() => activeGroup.value?.messages ?? []);

        const subhandleSelect0 = (index) => {
            activeSubIndex0.value = index;
        };

        const selectDirectChat = (contactId) => {
            activeDirectId.value = contactId;
        };

        const selectGroupChat = (groupId) => {
            activeGroupId.value = groupId;
        };

        const getInitial = (name = '') => (name ? name.charAt(0).toUpperCase() : '?');

        return {
            activeSubIndex0,
            subhandleSelect0,
            userSearchTerm,
            groupSearchTerm,
            draftDirectMessage,
            draftGroupMessage,
            filteredDirectContacts,
            filteredGroupChats,
            activeDirectId,
            activeGroupId,
            directMessages,
            groupMessages,
            activeDirect,
            activeGroup,
            selectDirectChat,
            selectGroupChat,
            lobbyHighlights,
            featuredSpeeches,
            getInitial,
        };
    },
};
</script>

<style scoped>
.chat-wrapper {
    padding-bottom: 24px;
}

.chat-section {
    margin-top: 20px;
}

.panel-card {
    background: #fdfdfd;
    border-radius: 10px;
    min-height: 320px;
}

.panel-title {
    font-size: 20px;
    font-weight: 600;
    color: #535a63;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.panel-subtitle {
    font-size: 14px;
    color: #909399;
    font-weight: 400;
}

.chat-list {
    margin-top: 12px;
    max-height: 420px;
    overflow-y: auto;
    padding-right: 4px;
}

.chat-list-item {
    border: 1px solid transparent;
    border-radius: 10px;
    padding: 12px;
    margin-bottom: 10px;
    background: #f7f9fb;
    cursor: pointer;
    transition: all 0.2s ease;
}

.chat-list-item:hover {
    border-color: #a0cfff;
}

.chat-list-item.active {
    border-color: #409eff;
    background: #eef5ff;
}

.chat-list-top {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 6px;
}

.chat-avatar {
    width: 36px;
    height: 36px;
    border-radius: 8px;
    color: #fff;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
}

.chat-name-meta {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 2px;
}

.chat-name {
    font-size: 16px;
    color: #303133;
}

.chat-id {
    font-size: 12px;
    color: #909399;
}

.chat-list-summary {
    font-size: 13px;
    color: #606266;
    line-height: 1.5;
}

.chat-list-footer {
    margin-top: 6px;
    font-size: 12px;
    color: #909399;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.chat-card {
    display: flex;
    flex-direction: column;
}

.message-area {
    flex: 1;
    min-height: 260px;
    max-height: 400px;
    overflow-y: auto;
    padding-right: 6px;
}

.message-wrap {
    display: flex;
    justify-content: flex-start;
    margin-bottom: 12px;
}

.message-wrap.from-user {
    justify-content: flex-end;
}

.message-bubble {
    max-width: 80%;
    background: #f2f6fc;
    border-radius: 14px;
    padding: 10px 14px;
    color: #303133;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.08);
}

.message-wrap.from-user .message-bubble {
    background: #409eff;
    color: #fff;
}

.message-author {
    font-weight: 600;
    margin-bottom: 4px;
}

.message-text {
    word-break: break-word;
    line-height: 1.6;
}

.timestamp {
    font-size: 12px;
    margin-top: 6px;
    color: rgba(255, 255, 255, 0.7);
}

.message-wrap:not(.from-user) .timestamp {
    color: #909399;
}

.reply-box {
    margin-top: 16px;
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.send-btn {
    align-self: flex-end;
}

.overview-line {
    font-size: 14px;
    color: #606266;
    margin-bottom: 6px;
}

.label {
    color: #909399;
}

.overview-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin: 10px 0;
}

.dense-text {
    font-size: 14px;
    line-height: 1.7;
    color: #606266;
}

.highlight-meta,
.speech-meta {
    margin-top: 12px;
    font-size: 12px;
    color: #80858c;
    display: flex;
    justify-content: space-between;
}

.highlight-card,
.speech-card {
    min-height: 180px;
}

.ml6 {
    margin-left: 6px;
}

.empty-hint {
    min-height: 260px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #909399;
    background: #f5f7fa;
    border-radius: 10px;
}
</style>
