<template>
    <div>
        <el-row>
            <el-col :span="24">
                <img src="	https://z2020-1302616346.cos.ap-hongkong.myqcloud.com/aboutwebsite/aboutus11.jpg"
                    class="bg_image" style="height:270px;width:100%;position: relative;" alt="">
                <div
                    style="color:white;position: absolute; top: 20%; left: 50%; transform: translate(-50%, -50%); z-index: 1; text-align: center;font-size: 30px;">
                    全民参与管理，共享劳动经验
                    <br>
                    一个“共有共享共治”的知识库
                </div>
            </el-col>
        </el-row>
        <el-row style="text-align: left;">
            左翼应及时地发明并建立起自己的智识平台，提出新的意识形态和经济模型、改革媒体、重建阶级力量，按照自己的方式重新配置已有的科技成果，才能实现未来的解放。--安东尼奥·奈格里(Antonio Negri)评《加速主义宣言》
        </el-row>
        <br>
        <el-row>
            <el-col :span="10">
                <el-image style="border:1px solid grey"
                    src="	https://z2020-1302616346.cos.ap-hongkong.myqcloud.com/aboutwebsite/aboutus_1.jpg" :fit="fill">
                </el-image>
            </el-col>
            <el-col :span="14">
                <div class="huanhang" style="text-align:left;">
                    <b class="font20px">片段化阅读</b>
                    <br>
                    如今长篇和空洞的报告文体，已经成为新一代“祭司”和“贵族”装神弄鬼的马戏。劳动者是没时间看长篇大论的。现代心理学认为，人类注意力的最佳范围是150字之内，所以在写作时人脑潜意识里就会把一个小主题凝结成一个相对独立的、150字左右的段落。我们记住的是某些段落。只有把精度细化到文章中的那些段落之上，才是真正对知识进行管理。
                </div>
            </el-col>
        </el-row>
        <br>
        <el-row>
            <el-col :span="14">
                <div class="huanhang" style="text-align:right;">
                    <b class="font20px">隐形知识：水面下的冰山</b>
                    <br>
                    隐形知识是知识片段背后的用户行为：点击量和关注量、评论和解释、支持或反对的意见、用户归类标签，知识片段之间关系（相互矛盾还是互为补充），语句中的强调关键词，用户日常关注和评论等历史行为，这些隐形知识都是组织内员工多次试错后慢慢积累的，极具价值但很难被记录、传播和继承，这是组织内的极为重要但常被忽视的隐形知识。在本网站中，知识片段的各种隐形知识均被挖掘和展示。
                </div>
            </el-col>
            <el-col :span="10">
                <el-image style="border:1px solid grey"
                    src="	https://z2020-1302616346.cos.ap-hongkong.myqcloud.com/aboutwebsite/aboutus_2.jpg" :fit="fill">
                </el-image>
            </el-col>
        </el-row>
        <br>
        <el-row>
            <el-col :span="10">
                <el-image style="border:1px solid grey"
                    src="	https://z2020-1302616346.cos.ap-hongkong.myqcloud.com/aboutwebsite/aboutus_3.jpg" :fit="fill">
                </el-image>
            </el-col>
            <el-col :span="14">
                <div class="huanhang" style="text-align:left;">
                    <b class="font20px">知识的精准推送和无障碍传播</b>
                    <br>
                    传统的科层金字塔体制的信息是自上而下单链分发，封闭、速度慢、多阻塞和死角。在传统的组织内岗位的管理水平严重依赖个人的历史经验和认知水平，只能依靠增加部门和人力来应对业务变化，造成了组织内人力架构的僵化和膨胀，也造成人的单向度化。
                    在组织内利用这种知识库系统，每个用户都是一个转发源，更高效传播给相近岗位用户,将相应的“知识片段”推送给合适的用户，员工更高效的适应多个岗位的知识，促成人的全面发展。
                </div>
            </el-col>
        </el-row>
        <br>

        <el-row> 
            <el-col :span="14">
                <div class="huanhang" style="text-align:right;">
                    <b class="font20px">加入我们</b>
                    <br>
                    摘抄名著精华，制作成段落列表发送管理员；对本站中晦涩文段进行通俗化解释。翻译本站的英文内容，写在文段评论栏。本站使用vuejs+django+mysql+mongodb等技术。
                    计划未来增加的功能：手机端应用，用户加密聊天，数据分布式存储，劳动培训图文社区，众筹捐助，闲置物品捐献等功能，欢迎大家分包协作。我们的QQ群号：771722807。
                    <br>
                    github项目名称：https://github.com/zhishiren/www_aworld_wiki.git
                </div>
            </el-col>
            <el-col :span="10">
                <el-image style="border:1px solid grey"
                    src="	https://z2020-1302616346.cos.ap-hongkong.myqcloud.com/aboutwebsite/aboutus_8.jpg" :fit="fill">
                </el-image>
            </el-col>
        </el-row>


        <!-- 
        <el-row>
            <el-col :span="14">
                <div class="huanhang"  style="text-align:right;">
                <b class="font20px">操作介绍1：查看全站文章+片段化阅读</b>		
                <br>
                点击主页右侧“搜”的按键，可以看见全站文集汇总。
                <br>
                本站所有的文章均是以原文自然段落拆分为片段，用户可以对这些片段进行关注、分享、评论和关联知识等操作。
                <br>
                用户可以通过ID号关联两个相关的知识片段。
                </div>
            </el-col>
            <el-col :span="10">
                <el-image
                    style="border:1px solid grey"
                    src="	https://z2020-1302616346.cos.ap-hongkong.myqcloud.com/aboutwebsite/z75b.gif"
                    :fit="fill">
                </el-image>
            </el-col>
        </el-row>
        <br>
        <el-row>
            <el-col :span="10">
                <el-image
                    style="border:1px solid grey"
                    src="	https://z2020-1302616346.cos.ap-hongkong.myqcloud.com/aboutwebsite/z75new.gif"
                    :fit="fill">
                </el-image>
            </el-col>
            <el-col :span="14">
                <div class="huanhang" style="text-align:left;">
                <b class="font20px">操作介绍2：加密发送言论信息</b>
                <br>	
                所有言论可以选择“明发”和“密发”两种发布形式。
                <br>
                “密发”的内容是经过加密后的符号，默认加密和解密密码均为八个1。你可以在“我的主页-发言密码‘处修改你的发言密码，然后通过一对一的通信方式分享你的解密密码。
                <br>
                </div>
            </el-col>
        </el-row>
        <br>
        <el-row>

            <el-col :span="14">
                <div class="huanhang" style="text-align:right;">
                <b class="font20px">操作介绍3：创建专题观点标签</b>	
                <br>
                本站建立了多个专题观点标签，例如“阅读难点求解”、“与某派对线专用资料包”，用户均可以添加相关知识片段到这些标签里，这样所有的用户都可以共享和协作。
                再例如，免费的或自由的功能性网站介绍。
                </div>
            </el-col>
            <el-col :span="10">
                <el-image
                    style="border:1px solid grey"
                    src="	https://z2020-1302616346.cos.ap-hongkong.myqcloud.com/aboutwebsite/z75c.jpg"
                    :fit="fill">
                </el-image>
            </el-col>
        </el-row>
        <br> -->


    </div>
</template>

<script>

export default {
    name: 'p61View',
    components: {
    }
}
</script>