<!-- 这是各类用户，各类知识点，各个段落，文章等的详情信息页面
在页面中{{  detailData?.item_id }}中的？是在页面onmount阶段变量尚未渲染可能造成加载失败，所以先行进行判断。
$route.params.id是要先判断id是否大于99999999，区分普通元素还是用户言论。

这里的密文点击解密的功能，点击之后显示密文提示，也可以直接连接到用户聊天界面。

这里需要根据不同的item_type，显示不同的内容，例如发言，物品，人物，群组，问答，辩论，文章，段落，知识点，用户，标签，投票等。
不同的item_type对应不同的el-menu-item，
例如如果是文章，则显示为“段落列表”，“评论评价”，“推荐阅读”，“内容管理”，关注分享，标签关联
如果是用户，则显示为“用户动态”，“评论评价”，“关注分享”，
如果是段落，则显示为“评论评价”，“标签关联”，“推荐阅读”，“内容管理”，关注分享，段落列表
如果是物品，则显示为流转记录，评论评价，关注分享，内容管理，（流转记录中含有借还事件，对上一个用户的使用情况评价，有没有什么新增破损）
如果是群组，则显示为成员列表，用户动态，关注分享，评论评价
如果是标签，则显示为标签内含，评论评价，关注分享，内容管理
如果是发言，则显示为评论评价，关注分享，内容管理，推荐阅读，标签关联，发言合集，
如果是辩论，则显示为辩论现场，回答合集
-->
 




<template>
    <div>
        <HelloLogout></HelloLogout>
        <br>
        <el-row>
            <el-col :span="3"></el-col>
            <el-col :span="18">
                    <el-card shadow="always" v-if="detailData?.item_type === '发言'">
                        <el-descriptions title="" column="1">
                            <el-descriptions-item>
                                <span class="speech-line">
                                    <span class="speech-author">{{ detailData?.user1name || detailData?.user1id || '匿名' }}</span>
                                    <span class="speech-separator">：</span>
                                    <span
                                      class="speech-content"
                                      :class="{ 'cipher-text': speechDetail.isCipher, 'cipher-block': speechDetail.isCipher }"
                                    >{{ speechDetail.displayText || '暂无内容' }}</span>
                                    <span v-if="speechDetail.isCipher" class="cipher-hint">点击解密</span>
                                    <span class="speech-time">{{ formatTime(detailData?.time_create) }}</span>
                                </span>
                            </el-descriptions-item>
                        </el-descriptions>
                        <el-descriptions title="" column="4">
                            <el-descriptions-item label="标识ID号:">{{ detailData?.item_id }}</el-descriptions-item>
                            <el-descriptions-item label="发言类型:">{{ detailData?.item_subtype || '未分类' }}</el-descriptions-item>
                            <el-descriptions-item label="发言状态:">{{ detailData?.item_status || '未知' }}</el-descriptions-item>
                            <el-descriptions-item label="公开范围:">{{ detailData?.itemXid || '未公开' }}</el-descriptions-item>
                        </el-descriptions>

                    </el-card>

                    <el-card shadow="always" v-if="detailData?.item_type === '物品'">
                        <el-descriptions title="" column="1">
                            <el-descriptions-item label="物品名称:">{{  detailData?.item_title }}</el-descriptions-item>
                        </el-descriptions>
                        <el-descriptions title="" column="4">
                            <el-descriptions-item label="标识ID号:">{{  detailData?.item_id }}</el-descriptions-item>
                            <el-descriptions-item label="目前状态:">{{  detailData?.item_status }}</el-descriptions-item>
                            <el-descriptions-item label="管理人员:">{{  detailData?.user1id }}</el-descriptions-item>
                            <el-descriptions-item label="物品类型:">{{  detailData?.item_subtype }}</el-descriptions-item>
                        </el-descriptions>
                        <el-descriptions title="" column="1">
                            <el-descriptions-item label="备注说明:">{{ detailData?.item_content }}
                                <span class="a_grey" v-if="!showCarousel" @click="showCarousel = true">-3项附件|点击查看-</span>
                            </el-descriptions-item>
                            <!-- 所在地区:江苏；上架时间20200101，捐赠人:9000002；目前借用人:90000004；该书是2020年版，安那其出版社，九成新。 -->
                            
                        </el-descriptions>

                        <el-carousel v-if="showCarousel" :interval="4000" type="card" height="200px">  
                            <el-carousel-item v-for="(imageUrl, index) in imageUrls" :key="index">  
                                <el-image style="width: auto; height: auto" :src="imageUrl" fit="cover" />  
                            </el-carousel-item>  
                        </el-carousel>  
                    </el-card>
                    <el-card shadow="always" v-if="detailData?.item_type === '言论'">
                        <el-descriptions title="" column="1">
                            <el-descriptions-item label="">
                                <span class="font30px">zhao:“</span>
                                <span
                                    style="background-color:lightgrey;font-weight: bold;font-size: 24px;color: brown;">11字密文</span>
                                <span class="font30px">”</span>
                                <span>点击解密</span>
                            </el-descriptions-item>
                        </el-descriptions>
                        <br>
                        <el-descriptions title="" column="4">
                            <el-descriptions-item label="标识ID号:">{{  detailData?.item_id}}</el-descriptions-item>
                            <el-descriptions-item label="属性分类:">{{  detailData?.item_subtype}}</el-descriptions-item>
                            <el-descriptions-item label="目前状态:">{{  detailData?.item_status}}</el-descriptions-item>
                            <el-descriptions-item label="公开范围:">{{  detailData?.itemXid}}</el-descriptions-item>
                            <!-- <el-descriptions-item label="布时间:">20210101-11:11</el-descriptions-item> -->
                            <!-- <el-descriptions-item label="可见范围:">测试测试测试</el-descriptions-item> -->
                        </el-descriptions>
                    </el-card>
                <!-- 这里可以设计一些形容人的词汇：古道热肠，聪明绝顶，言论怪异，让人困扰，胡说八道，说谎成性，装逼十足，欠缺礼貌，恐吓骚扰，虚假宣传，色情低俗，暴力血腥 -->
                
                <UserInfoCard :itemData="detailData" v-if="detailData?.item_type === '人物'" />

                <el-card shadow="always" v-if="detailData?.item_type === '群组'">
                    <el-row>
                        <el-col :span="8"
                            style="border: 1px dashed lightgrey; display: flex; justify-content: center; align-items: center;">
                            <img src="https://z2024-1302616346.cos.ap-nanjing.myqcloud.com/underconstruction.jpg"
                                style="width: 100%; height: auto;">
                        </el-col>
                        <el-col :span="14">
                            <el-descriptions title="" column="1" style="margin-left: 10px;">
                                <el-descriptions-item label="群组名称:">{{  detailData?.item_title }}</el-descriptions-item>
                                <el-descriptions-item label="类型与ID:">{{ detailData?.item_subtype }}｜{{ detailData?.item_id }}</el-descriptions-item>
                                <!-- 这里是群组的类型，例如西撒总公社，一级公社，二级公社，自建小组，现实团体 -->
                                <el-descriptions-item label="所在地区:">{{ detailData?.sparefield1 }}</el-descriptions-item>
                                <!-- 这里如果是西撒公社，则显示为公社的别称 -->
                                <el-descriptions-item label="轮值管理:">
                                    <router-link :to="{ name: 'DetailPage', params: { id: detailData?.user1id } }" target="_blank" class="a_grey">  {{ detailData?.user1id }}</router-link>
                                </el-descriptions-item>
                                <el-descriptions-item label="目前状态:">{{ detailData?.item_status }}</el-descriptions-item>
                                <el-descriptions-item label="数据统计:">ceshi</el-descriptions-item>
                                <el-descriptions-item label="介绍说明:">{{ detailData?.item_content }}</el-descriptions-item>
                                    <!-- 这是团体的介绍说明，请输入六十至八十字。���是团体的介绍说明，请输入六十至八十字。这是团体的介绍说明，请输入六十至八十字。这是团体的介绍说明，请输入六十至八十字。 -->
                            </el-descriptions>
                        </el-col>
                        <el-col :span="2">
                            <span>
                                <el-button key="info" type="info" text class="custom-button">
                                    <el-icon class="my-icon">
                                        <ChatLineSquare />
                                    </el-icon>群聊
                                </el-button>
                            </span>
                            <!-- <br>

                            <span>
                                <el-button key="info" type="info" text class="custom-button">
                                    <el-icon class="my-icon">
                                        <Edit />
                                    </el-icon>修改
                                </el-button>
                            </span> -->
                        </el-col>
                    </el-row>
                </el-card>

 

                <el-card shadow="always" v-if="detailData?.item_type === '问答'">
                    <el-descriptions title="" column="1">
                        <el-descriptions-item label="提问标题:">{{ detailData?.item_title }}</el-descriptions-item>
                    </el-descriptions>
                    <el-descriptions title="" column="4">
                        <el-descriptions-item label="标识ID号:">{{ detailData?.item_id }}</el-descriptions-item>
                        <el-descriptions-item label="目前状态:">{{ detailData?.item_status }}</el-descriptions-item>
                        <el-descriptions-item label="提问时间:">{{ detailData?.createtime }}</el-descriptions-item>
                        <el-descriptions-item label="提问人员:">{{ detailData?.user1id }}</el-descriptions-item>
                    </el-descriptions>
                    <el-descriptions title="" column="1">
                        <el-descriptions-item label="详细问题:">{{ detailData?.item_content }}</el-descriptions-item>
                        <!-- 这这是提问的详细问题。回答的答案是附言的形式。 -->
                    </el-descriptions>
                </el-card>

                <el-card shadow="always" v-if="detailData?.item_type === '辩论'">
                    <el-descriptions title="" column="1">
                        <el-descriptions-item label="辩论标题:">{{ detailData?.item_title }}</el-descriptions-item>
                    </el-descriptions>
                    <el-descriptions title="" column="4">
                        <el-descriptions-item label="标识ID号:">{{ detailData?.item_id }}</el-descriptions-item>
                        <el-descriptions-item label="目前状态:">{{ detailData?.item_status }}</el-descriptions-item>
                        <el-descriptions-item label="创建时间:">{{ detailData?.createtime }}</el-descriptions-item>
                        <el-descriptions-item label="管理人员:">{{ detailData?.user1id }}</el-descriptions-item>
                    </el-descriptions>
                    <el-descriptions title="" column="1">
                        <el-descriptions-item label="备注说明:">{{ detailData?.item_content }}</el-descriptions-item>
                        <!-- 正方：不需要郭嘉。���是安批和马批之间的辩论。 -->
                    </el-descriptions>
                </el-card>



                <el-card shadow="always" v-if="detailData?.item_type === '文章'">
                    <el-descriptions title="" column="1">
                        <el-descriptions-item label="文章标题:">{{ detailData?.item_title }}</el-descriptions-item>
                    </el-descriptions>
                    <el-descriptions title="" column="4">
                        <el-descriptions-item label="标识ID号:">{{ detailData?.item_id }}</el-descriptions-item>
                        <el-descriptions-item label="可用状态:">{{ detailData?.item_status }}</el-descriptions-item>
                        <el-descriptions-item label="管理人员:">{{ detailData?.user1id }}</el-descriptions-item>
                        <el-descriptions-item label="属性分类:">测试测试测试</el-descriptions-item>
                    </el-descriptions>
                    <el-descriptions title="" column="1">
                        <el-descriptions-item label="备注说明:">{{ detailData?.item_content }}，生效时间:{{ detailData?.createtime }},-原文附件下载-</el-descriptions-item>
                            <!-- 所属行业，所属细分学科，所属地区，发行人等信息。点击查看统计数据，试测试测测你测试。 -->
                        
                    </el-descriptions>
                </el-card>
               
                <el-card shadow="always" v-if="detailData?.item_type === '投票'">
                    <el-descriptions title="" column="1">
                        <el-descriptions-item label="投票名称:">{{ detailData?.item_title }}</el-descriptions-item>
                    </el-descriptions>
                    <el-descriptions title="" column="4">
                        <el-descriptions-item label="标识ID号:">{{ detailData?.item_id }}</el-descriptions-item>
                        <el-descriptions-item label="可用状态:">{{ detailData?.item_status }}</el-descriptions-item>
                        <el-descriptions-item label="开始时间:">{{ detailData?.createtime }}</el-descriptions-item>
                        <el-descriptions-item label="点击投票:">-点击投票-</el-descriptions-item>
                        <el-descriptions-item label="归属团体:">{{ detailData?.user0id }}</el-descriptions-item>
                        <el-descriptions-item label="管理人员:">{{ detailData?.user1id }}</el-descriptions-item>
                        <el-descriptions-item label="截止时间:">{{ detailData?.sparefield0 }}</el-descriptions-item>
                        <el-descriptions-item label="投票结果:">-点击查看-</el-descriptions-item>

                    </el-descriptions>
                    <el-descriptions title="" column="1">
                        <el-descriptions-item label="备注说明:">{{ detailData?.item_content }}</el-descriptions-item>
                            <!-- 这里可以是公社或协会契约全本，或者段落。某职位的选举。该职位的基本功能，任职时间一年。我们将全文进行修改。点击之后显示投票结果。也可以查看相关投票结果。 -->
                        
                    </el-descriptions>
                </el-card>
           
                
                <el-card shadow="always" v-if="detailData?.item_type === '标签'">
                    <el-descriptions title="" column="1">
                        <el-descriptions-item label="标签名称:">{{ detailData?.item_title }}</el-descriptions-item>
                    </el-descriptions>
                    <el-descriptions title="" column="4">
                        <el-descriptions-item label="标识ID号:">{{ detailData?.item_id }}</el-descriptions-item>
                        <el-descriptions-item label="可用状态:">{{ detailData?.item_status }}</el-descriptions-item>
                        <el-descriptions-item label="创建时间:">{{ detailData?.item_createtime }}</el-descriptions-item>
                        <el-descriptions-item label="管理人员:">{{ detailData?.user1id }}</el-descriptions-item>
                    </el-descriptions>
                    <el-descriptions title="" column="1">
                        <el-descriptions-item label="备注说明:">{{ detailData?.item_content }}</el-descriptions-item>
                        <!-- 所属行业，所属细分学科，所属地区，发行人等信息，点击查看统计数据。 -->
                    </el-descriptions>
                </el-card>

                <el-card shadow="always" v-if="detailData?.item_type === '劳动任务'">
                    <el-descriptions title="" column="1">
                        <el-descriptions-item label="工作任务:">{{ detailData?.item_title }}</el-descriptions-item>
                    </el-descriptions>
                    <el-descriptions title="" column="4">
                        <el-descriptions-item label="标识ID号:">{{ detailData?.item_id }}</el-descriptions-item>
                        <el-descriptions-item label="工作类型:">{{ detailData?.item_subtype }}</el-descriptions-item>
                        <el-descriptions-item label="归属组织:">{{ detailData?.user0id }}</el-descriptions-item>
                        <el-descriptions-item label="管理人员:">{{ detailData?.user1id }}</el-descriptions-item>
                    </el-descriptions>
                    <el-descriptions title="" column="1">
                        <el-descriptions-item label="备注说明:">{{ detailData?.item_content }}</el-descriptions-item>
                        <!-- 重要性：工作难度，工作强度，所属地区，发行人等信息，点击查看统计数据。 -->
                    </el-descriptions>
                </el-card>

                <el-card shadow="always" v-if="detailData?.item_type === '公共服务'">
                    <el-descriptions title="" column="1">
                        <el-descriptions-item label="公共服务:">{{ detailData?.item_title }}</el-descriptions-item>
                    </el-descriptions>
                    <el-descriptions title="" column="4">
                        <el-descriptions-item label="标识ID号:">{{ detailData?.item_id }}</el-descriptions-item>
                        <el-descriptions-item label="创建时间:">{{ detailData?.createtime }}</el-descriptions-item>
                        <el-descriptions-item label="目前状态:">{{ detailData?.item_status }}</el-descriptions-item>
                        <el-descriptions-item label="轮值管理:">{{ detailData?.user1id }}</el-descriptions-item>
                    </el-descriptions>
                    <el-descriptions title="" column="1">
                        <el-descriptions-item label="备注说明:">{{ detailData?.item_content }}</el-descriptions-item>
                    </el-descriptions>
                </el-card>
        
                <el-card shadow="always" v-if="detailData?.item_type === '段落'">
                    <el-descriptions title="" column="1">
                        <el-descriptions-item label="段落标题:">
                            <span>{{ detailData?.item_title }}</span>
                            <span style="float: right;">打印<el-divider direction="vertical" />段序:{{ detailData?.itemXsn }}<el-divider direction="vertical" />上段<el-divider direction="vertical" />下段</span>
                        </el-descriptions-item>
                        <el-descriptions-item label="所属文章:">
                            <router-link :to="{ name: 'DetailPage', params: { id: detailData?.itemXid} }" target="_blank" class="a_black">
                                {{ detailData?.sparefield1 }}   
                            </router-link>
                        </el-descriptions-item>
                    </el-descriptions>
                    <el-descriptions title="" column="4">
                        <el-descriptions-item label="标识ID号:">{{ detailData?.item_id }}</el-descriptions-item>
                        <el-descriptions-item label="目前状态:">{{ detailData?.item_status }}</el-descriptions-item>
                        <el-descriptions-item label="管理人员:">{{ detailData?.user1id ? detailData?.user1id : detailData?.user0id }}</el-descriptions-item>
                        <el-descriptions-item label="属性分类:">{{ detailData?.item_subtype }}</el-descriptions-item>
                        <!-- <el-descriptions-item label="生效时间:">{{ detailData?.time_effective ? detailData?.time_effective : '暂无信息' }}</el-descriptions-item> -->
                    </el-descriptions>
                    <el-descriptions title="" column="1">
                        <el-descriptions-item label="段落正文:">{{ detailData?.item_content }}</el-descriptions-item>
                    </el-descriptions>
                </el-card>



            </el-col>
            <el-col :span="3">

            </el-col>
        </el-row>



        <!-- 动态功能标签，根据不同元素类型展示不同的面板 -->
        <el-row style="max-width: 100%; overflow-x: hidden;">
            <el-col :span="3">
                <el-menu
                  :default-active="activeTabIndex"
                  class="el-menu-vertical-demo bgcolor_menu_FC"
                  @select="handleTabSelect"
                >
                  <el-menu-item
                    v-if="isTabVisible('段落列表')"
                    :index="tabIndexOf('段落列表')"
                    class="menu-item18"
                  >
                    <span>段落列表</span>
                  </el-menu-item>
                  <el-menu-item
                    v-if="isTabVisible('评论评价')"
                    :index="tabIndexOf('评论评价')"
                    class="menu-item18"
                  >
                    <span>评论评价</span>
                  </el-menu-item>
                  <el-menu-item
                    v-if="isTabVisible('推荐阅读')"
                    :index="tabIndexOf('推荐阅读')"
                    class="menu-item18"
                  >
                    <span>推荐阅读</span>
                  </el-menu-item>
                  <el-menu-item
                    v-if="isTabVisible('内容管理')"
                    :index="tabIndexOf('内容管理')"
                    class="menu-item18"
                  >
                    <span>内容管理</span>
                  </el-menu-item>
                  <el-menu-item
                    v-if="isTabVisible('关注分享')"
                    :index="tabIndexOf('关注分享')"
                    class="menu-item18"
                  >
                    <span>关注分享</span>
                  </el-menu-item>
                  <el-menu-item
                    v-if="isTabVisible('标签关联')"
                    :index="tabIndexOf('标签关联')"
                    class="menu-item18"
                  >
                    <span>标签关联</span>
                  </el-menu-item>
                  <el-menu-item
                    v-if="isTabVisible('用户动态')"
                    :index="tabIndexOf('用户动态')"
                    class="menu-item18"
                  >
                    <span>用户动态</span>
                  </el-menu-item>
                  <el-menu-item
                    v-if="isTabVisible('流转记录')"
                    :index="tabIndexOf('流转记录')"
                    class="menu-item18"
                  >
                    <span>流转记录</span>
                  </el-menu-item>
                  <el-menu-item
                    v-if="isTabVisible('成员列表')"
                    :index="tabIndexOf('成员列表')"
                    class="menu-item18"
                  >
                    <span>成员列表</span>
                  </el-menu-item>
                  <el-menu-item
                    v-if="isTabVisible('标签内含')"
                    :index="tabIndexOf('标签内含')"
                    class="menu-item18"
                  >
                    <span>标签内含</span>
                  </el-menu-item>
                  <el-menu-item
                    v-if="isTabVisible('知识解读')"
                    :index="tabIndexOf('知识解读')"
                    class="menu-item18"
                  >
                    <span>知识解读</span>
                  </el-menu-item>
                  <el-menu-item
                    v-if="isTabVisible('发言合集')"
                    :index="tabIndexOf('发言合集')"
                    class="menu-item18"
                  >
                    <span>发言合集</span>
                  </el-menu-item>
                  <el-menu-item
                    v-if="isTabVisible('回答合集')"
                    :index="tabIndexOf('回答合集')"
                    class="menu-item18"
                  >
                    <span>回答合集</span>
                  </el-menu-item>
                  <el-menu-item
                    v-if="isTabVisible('辩论现场')"
                    :index="tabIndexOf('辩论现场')"
                    class="menu-item18"
                  >
                    <span>辩论现场</span>
                  </el-menu-item>
                  <el-menu-item
                    v-if="isTabVisible('投票详情')"
                    :index="tabIndexOf('投票详情')"
                    class="menu-item18"
                  >
                    <span>投票详情</span>
                  </el-menu-item>
                </el-menu>
            </el-col>

            <el-col :span="21">
                <template v-if="activeTabLabel">
                    <template v-if="activeTabLabel === '段落列表'">
                        <el-row class="firstrow">
                            <Opline
                                actions="新增"
                                :showprops="activeTabLabel"
                                :item-object="detailData"
                                expand-text="展开查看更多"
                                @expand="handleExpand"
                            />
                        </el-row>
                    </template>
                    <template v-else-if="activeTabLabel === '评论评价'">
                        <el-row class="firstrow">
                            <Opline
                                actions="评论,顶,踩"
                                :showprops="activeTabLabel"
                                :item-object="detailData"
                                expand-text="展开查看更多"
                                @expand="handleExpand"
                            />
                        </el-row>
                    </template>
                    <template v-else-if="activeTabLabel === '推荐阅读'">
                        <el-row class="firstrow">
                            <Opline
                                actions="换一批"
                                :showprops="activeTabLabel"
                                :item-object="detailData"
                                expand-text="展开查看更多"
                                @expand="handleExpand"
                            />
                        </el-row>
                    </template>
                    <template v-else-if="activeTabLabel === '内容管理'">
                        <el-row class="firstrow">
                            <Opline
                                actions="修改"
                                :showprops="activeTabLabel"
                                :item-object="detailData"
                                expand-text="展开查看更多"
                                @expand="handleExpand"
                            />
                        </el-row>
                    </template>
                    <template v-else-if="activeTabLabel === '关注分享'">
                        <el-row class="firstrow">
                            <Opline
                                actions="关注,分享"
                                :showprops="activeTabLabel"
                                :item-object="detailData"
                                expand-text="展开查看更多"
                                @expand="handleExpand"
                            />
                        </el-row>
                    </template>
                    <template v-else-if="activeTabLabel === '标签关联'">
                        <el-row class="firstrow">
                            <Opline
                                actions="加标签"
                                :showprops="activeTabLabel"
                                :item-object="detailData"
                                expand-text="展开查看更多"
                                @expand="handleExpand"
                            />
                        </el-row>
                    </template>
                    <template v-else-if="activeTabLabel === '用户动态'">
                        <el-row class="firstrow">
                            <Opline
                                actions="发言"
                                :showprops="activeTabLabel"
                                :item-object="detailData"
                                expand-text="展开查看更多"
                                @expand="handleExpand"
                            />
                        </el-row>
                    </template>
                    <template v-else-if="activeTabLabel === '成员列表'">
                        <el-row class="firstrow">
                            <Opline
                                actions="加入"
                                :showprops="activeTabLabel"
                                :item-object="detailData"
                                expand-text="展开查看更多"
                                @expand="handleExpand"
                            />
                        </el-row>
                    </template>
                    <template v-else-if="activeTabLabel === '标签内含'">
                        <el-row class="firstrow">
                            <Opline
                                actions="新增"
                                :showprops="activeTabLabel"
                                :item-object="detailData"
                                expand-text="展开查看更多"
                                @expand="handleExpand"
                            />
                        </el-row>
                    </template>
                    <template v-else-if="activeTabLabel === '辩论现场'">
                        <el-row class="firstrow">
                            <Opline
                                actions="立论"
                                :showprops="activeTabLabel"
                                :item-object="detailData"
                                expand-text="展开查看更多"
                                @expand="handleExpand"
                            />
                        </el-row>
                    </template>
                    <template v-else-if="activeTabLabel === '回答合集'">
                        <el-row class="firstrow">
                            <Opline
                                actions="评论"
                                :showprops="activeTabLabel"
                                :item-object="detailData"
                                expand-text="展开查看更多"
                                @expand="handleExpand"
                            />
                        </el-row>
                    </template>
                    <el-card v-else class="tab-placeholder" shadow="never">
                        {{ tabDescriptions[activeTabLabel] || '该功能模块正在完善中。' }}
                    </el-card>
                </template>
                <el-empty v-else description="暂无可用标签" />
            </el-col>
        </el-row>

    </div>
</template>

<script>

import { ref, onMounted, computed, watch } from 'vue';  
import axios from 'axios';
import { useRoute } from 'vue-router';  
import HelloLogout from '../components/HelloLogout.vue';
// import OperationRow from '../components/OperationRow.vue';
import Subpage_debate from '../detail_subpage/Subpage_debate.vue';
import { ElLoading } from 'element-plus'; // 导入 ElLoading
import Opline from '../components/Opline.vue';
import UserInfoCard from '../components/UserInfoCard.vue'
import { formatTimestamp } from '@/utils/myfunctions';
import { ChatLineSquare } from '@element-plus/icons-vue';



export default {
    name: 'DetailPage',
    components: {
        HelloLogout,
        // OperationRow,
        Subpage_debate,
        Opline,
        UserInfoCard,
        ChatLineSquare
    },


    setup() {

        const detailData = ref(null)  
        const route = useRoute()  
        const localUserId = Number(localStorage.getItem('userid')); // 转化为数值型
        console.log(localUserId);
        const loadingInstance = ref(null); // 定义 loadingInstance
        const showLoading = () => {
            loadingInstance.value = ElLoading.service({ // 开始加载
                lock: true,
                text: '加载中...', // 增大字体
                spinner: 'el-icon-loading',
                background: 'rgba(0, 0, 0, 0.7)',
                customClass: 'custom-loading-text',
            });
        };
        const hideLoading = () => {
            if (loadingInstance.value) {
                loadingInstance.value.close(); // 结束加载
            }
        };
        
        onMounted(async () => {  
            showLoading(); // 显示加载
            try {  
                const { id } = route.params;  
                const response = await axios.post('https://www.aworld.wiki/api/iteminfo/show_all_iteminfo/' ,{ id: id });  
                detailData.value = response.data;  
            } catch (error) {  
                console.error('Failed to fetch data:', error);  
            };
            hideLoading(); // 隐藏加载
        });


        const showCarousel = ref(false);  
        // Check if the name exists on the server  
        const imageUrls = ref([
            'https://z2024-1302616346.cos.ap-nanjing.myqcloud.com/10000001kk.jpg',
            'https://z2024-1302616346.cos.ap-nanjing.myqcloud.com/10000001er.jpg',
            'https://z2024-1302616346.cos.ap-nanjing.myqcloud.com/10000001%E6%AD%A3%E9%9D%A2.jpg'
        ]);




        const menuConfig = {
            '文章': ['段落列表', '评论评价', '推荐阅读', '内容管理', '关注分享', '标签关联'],
            '用户': ['用户动态', '评论评价', '关注分享'],
            '人物': ['用户动态', '评论评价', '关注分享'],
            '段落': ['评论评价', '标签关联', '推荐阅读', '内容管理', '关注分享', '段落列表'],
            '物品': ['流转记录', '评论评价', '关注分享', '内容管理'],
            '群组': ['成员列表', '用户动态', '关注分享', '评论评价'],
            '标签': ['标签内含', '评论评价', '关注分享', '内容管理'],
            '知识点': ['知识解读', '评论评价', '关注分享', '内容管理'],
            '发言': ['评论评价', '关注分享', '内容管理', '推荐阅读', '标签关联', '发言合集'],
            '问答': ['回答合集', '评论评价', '关注分享'],
            '辩论': ['辩论现场', '回答合集'],
            '投票': ['投票详情', '评论评价', '关注分享']
        };
        const defaultMenu = ['关注分享', '评论评价'];

        const tabIndexMap = {
            '关注分享': 'tab_follow_share',
            '评论评价': 'tab_comment_review',
            '推荐阅读': 'tab_recommend',
            '内容管理': 'tab_content_manage',
            '标签关联': 'tab_tag_relation',
            '用户动态': 'tab_user_activity',
            '段落列表': 'tab_paragraph_list',
            '流转记录': 'tab_transfer_records',
            '成员列表': 'tab_member_list',
            '标签内含': 'tab_tag_internal',
            '知识解读': 'tab_knowledge_analysis',
            '发言合集': 'tab_speech_collection',
            '回答合集': 'tab_answer_collection',
            '辩论现场': 'tab_debate_scene',
            '投票详情': 'tab_vote_detail'
        };

        const indexToLabel = Object.fromEntries(Object.entries(tabIndexMap).map(([label, index]) => [index, label]));

        const tabSequence = [
            '段落列表',
            '评论评价',
            '推荐阅读',
            '内容管理',
            '关注分享',
            '标签关联',
            '用户动态',
            '流转记录',
            '成员列表',
            '标签内含',
            '知识解读',
            '发言合集',
            '回答合集',
            '辩论现场',
            '投票详情'
        ];

        const visibleTabList = computed(() => {
            const type = detailData.value?.item_type;
            const configured = menuConfig[type];
            const labels = Array.isArray(configured) && configured.length ? configured : defaultMenu;
            return labels.filter((label) => tabIndexMap[label]);
        });

        const visibleTabSet = computed(() => new Set(visibleTabList.value));

        const pickFirstVisibleIndex = (tabs) => {
            if (!tabs.length) return '';
            const available = new Set(tabs);
            for (const label of tabSequence) {
                if (!available.has(label)) continue;
                const index = tabIndexMap[label];
                if (index) return index;
            }
            return '';
        };

        const activeTabIndex = ref('');
        watch(visibleTabList, (tabs) => {
            if (!tabs.length) {
                activeTabIndex.value = '';
                return;
            }
            const currentLabel = indexToLabel[activeTabIndex.value];
            if (currentLabel && tabs.includes(currentLabel)) {
                return;
            }
            activeTabIndex.value = pickFirstVisibleIndex(tabs);
        }, { immediate: true });

        const activeTabLabel = computed(() => indexToLabel[activeTabIndex.value] || '');

        const isTabVisible = (label) => visibleTabSet.value.has(label);
        const tabIndexOf = (label) => tabIndexMap[label];

        const handleTabSelect = (index) => {
            const label = indexToLabel[index];
            if (label && visibleTabSet.value.has(label)) {
                activeTabIndex.value = index;
            }
        };

        const tabDescriptions = {
            '段落列表': '展示当前文章的段落目录，支持快速跳转。',
            '流转记录': '借还记录、使用评价与新增破损将在此呈现。',
            '成员列表': '展示群组成员信息及角色。',
            '标签内含': '列出该标签下关联的内容。',
            '发言合集': '汇总该发言相关的延展讨论。',
            '知识解读': '梳理知识点的背景与延伸阅读。',
            '投票详情': '显示投票选项、进度及结果。',
            '辩论现场': '呈现正反双方的核心观点。',
            '回答合集': '汇总问答或辩论中的精彩回复。'
        };

        const handleExpand = () => {};

        const normalizeTimestamp = (value) => {
            if (value === null || value === undefined || value === '') {
                return null;
            }
            if (value instanceof Date) {
                const time = value.getTime();
                return Number.isNaN(time) ? null : time;
            }
            if (typeof value === 'number') {
                return value < 1e12 ? value * 1000 : value;
            }
            if (typeof value === 'string') {
                const trimmed = value.trim();
                if (!trimmed) return null;
                if (/^\d+$/.test(trimmed)) {
                    const numeric = Number(trimmed);
                    return numeric < 1e12 ? numeric * 1000 : numeric;
                }
                const parsed = new Date(trimmed).getTime();
                return Number.isNaN(parsed) ? null : parsed;
            }
            const parsed = new Date(value).getTime();
            return Number.isNaN(parsed) ? null : parsed;
        };

        const formatTime = (value) => {
            const ms = normalizeTimestamp(value);
            if (ms === null) {
                if (typeof value === 'string' && value.trim()) {
                    return value;
                }
                return '暂无时间';
            }
            return formatTimestamp(ms);
        };

        const speechDetail = computed(() => {
            const data = detailData.value;
            if (!data || data.item_type !== '发言') {
                return {
                    label: '发言内容:',
                    displayText: '',
                    isCipher: false
                };
            }

            const spare = data.sparefield1;
            const hasCipher = typeof spare === 'string'
                ? spare.trim().length > 0
                : spare !== null && spare !== undefined && spare !== '';

            const displayText = hasCipher
                ? (data.item_title || '')
                : (data.item_content || '');

            return {
                label: hasCipher ? '密文内容:' : '明文内容:',
                displayText,
                isCipher: hasCipher
            };
        });

        return {
            imageUrls,
            showCarousel,
            detailData,
            localUserId,
            speechDetail,
            formatTime,
            activeTabIndex,
            activeTabLabel,
            isTabVisible,
            tabIndexOf,
            handleTabSelect,
            tabDescriptions,
            handleExpand
        };
    },
};  
</script>

<style scoped>
.login {
    width: 1280px;
    margin: 0 auto;
}

.header {
    width: 1280px;
    background-color: #708090;
    ;
    height: 40px;
    color: white;
    font-size: 40px;
    line-height: 40px;
    text-align: left;
    padding: 0;
}



.menu-item {
    font-size: 20px;
    color: gray !important;
}

.menu-item18 {
    font-size: 18px;
    /* color: gray !important; */
    text-align: center;
}

.el-menu-vertical-demo {
    border-right: none !important;
}

.aside-left {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    justify-content: space-between;
    width: 120px;
    height: 450px;

}

.font30px {
    font-size: 30px;
    font-family: 'Microsoft YaHei';
    font-weight: bolder;
}

.flat-button {
    margin-bottom: 0px !important;
    padding: 15px;
    height: 56px;
    border: none;
    border-radius: 4px;
    background-color: #fff;
    color: #666;
    font-size: 25px;
    cursor: pointer;
}

.flat-button:hover {
    background-color: #f2f2f2;
}

::v-deep .el-descriptions__label {
    font-size: 18px;

}

::v-deep .el-descriptions__content {
    font-size: 18px;
    color: grey;
}

::v-deep .el-descriptions__cell {
    padding-bottom: 0 !important;
    /* 或需要调整padding来去除间距 */
}


.my-date-picker .el-date-picker__input {  
  width: 200px;  
}  




.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}

.el-row {
  max-width: 100%;
  overflow-x: hidden;
}

.el-text.truncated {  
  display: inline-block; /* 或者 block，根据你的布局需要 */  
  white-space: nowrap;  
  overflow: hidden;  
  text-overflow: ellipsis;  
  max-width: 300px; /* 或者具体的宽度值，如 150px */  
  font-size: 20px;
}
.speech-line {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 6px;
  font-size: 19px;
  color: #2f3b52;
}

.speech-author {
  font-weight: 600;
  color: #1f2d3d;
}

.speech-separator {
  color: #2f3b52;
}

.speech-content {
  color: #2f3b52;
}

.speech-time {
  margin-left: auto;
  color: #7c889c;
  font-size: 19px;
}

.cipher-block {
  display: inline-block;
  padding: 2px 6px;
  border-radius: 4px;
  background-color: lightgray;
}

.cipher-text {
  font-weight: 600;
  letter-spacing: 1px;
  color: brown;
}

.cipher-hint {
  margin-left: 8px;
  font-size: 14px;
  color: #909399;
  font-weight: 400;
}

</style>
