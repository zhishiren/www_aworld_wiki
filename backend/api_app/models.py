from django.db import models
from django.utils import timezone

class ItemInfo(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_title = models.CharField(max_length=100, default='')#这里如果是用户的秘文发言，则显示为“？字的密文”。
    item_content = models.CharField(max_length=1000, blank=True, null=True)#这是各种元素的详细说明，如果是密文，则显示为加密后的文字。
    item_type = models.CharField(max_length=5, default='', help_text='这是用来记录元素的主类型，例如文章或标签')
    item_subtype = models.CharField(max_length=5, blank=True, null=True, help_text='细分类型，例如文章-国家法律或公社契约')
    item_status = models.CharField(max_length=5, default='')
    time_create = models.DateTimeField(default=timezone.now)
    time_effective = models.DateTimeField(blank=True, null=True)
    user0id = models.IntegerField(blank=True, null=True)#这是创建者的信息
    user0name = models.CharField(max_length=100, default='')
    user1id = models.IntegerField(blank=True, null=True)#这是目前管理人员的信息，管理人员是可以变动的。也是用来表示是否为匿名发言者，如果是匿名，字段值为99999999
    user1name = models.CharField(max_length=100, default='')#这是目前管理人员的信息，管理人员是可以变动的。也是用来表示是否为匿名发言者，如果是匿名，字段值为匿名者
    itemXid = models.IntegerField(blank=True, null=True) #这里记录该元素所属的上一层级元素的id。例如文段所属的文集。也用来记录发言范围
    itemXsn = models.IntegerField(blank=True, null=True, help_text='这仅对于段落和数集类型，用来表示他在文集中的顺序')
    attachment = models.IntegerField(blank=True, null=True)#这里用来显示是否有附件附图等，如果不为零，则显示链接。
    sparefield0 = models.CharField(max_length=999, default='', help_text='备用，存登录密码')#在drf中不下传，也存用户发言的解密密码。
    sparefield1 = models.CharField(max_length=99, default='') #这里显示用户设置的密码提示，提供下传，所有用户可见，
    sparefield2 = models.CharField(max_length=99, default='')
    sparefield3 = models.CharField(max_length=99, default='')

    class Meta:
        db_table = 'iteminfo'
        verbose_name = '各种元素的详细信息'
        verbose_name_plural = verbose_name
    
    def to_dict(self):
        return {
            'item_id':self.item_id,
            'item_title':self.item_title,
            'item_type':self.item_type,
            # 其他字段,这里可能会用在redis初始化模块中
        }
    
    
    
#这里加一个申报的操作类型，涉及到用户的加班，休假，收入，借用公共物品等一系列的公共服务。
class Operation(models.Model):
    op_id = models.AutoField(primary_key=True)
    op_type = models.CharField(max_length=5, default='')
    op_status = models.CharField(max_length=5, blank=True, null=True)
    op_range = models.IntegerField(blank=True, null=True)
    op_time = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=99, blank=True, null=True)
    ps_content = models.CharField(max_length=999, blank=True, null=True)
    ps_type = models.CharField(max_length=5, blank=True, null=True)#这里是细分的类型，比如评论中的支持和反对，关联中的互相矛盾等。
    ps_attitude = models.CharField(max_length=5, blank=True, null=True)
    ps_encrypted = models.IntegerField(blank=True, null=True)
    item0id = models.IntegerField(blank=True, null=True)
    item0title = models.CharField(max_length=99, blank=True, null=True)
    item0type = models.CharField(max_length=5, blank=True, null=True)
    item1id = models.IntegerField(blank=True, null=True)
    item1title = models.CharField(max_length=99, blank=True, null=True)
    item1type = models.CharField(max_length=5, blank=True, null=True)
    userXid = models.IntegerField(blank=True, null=True) #这里记录匿名用户的真实id，不下传
    userXname = models.CharField(max_length=99, blank=True, null=True)#这里记录匿名用户的真实name，不下传
    sparefield0 = models.CharField(max_length=99, blank=True, null=True)
    sparefield1 = models.CharField(max_length=99, blank=True, null=True)
    sparefield2 = models.CharField(max_length=99, blank=True, null=True)
    sparefield3 = models.CharField(max_length=99, blank=True, null=True)

    class Meta:
        db_table = 'operation'
        verbose_name = '操作信息'
        verbose_name_plural = verbose_name



class Statistic(models.Model):
    item_id = models.IntegerField(primary_key=True, help_text='相关元素的id号，不能自增，被动写入')
    followed0 = models.IntegerField(blank=True, null=True, help_text='关注-全量')
    followed1 = models.IntegerField(blank=True, null=True, help_text='关注-特别关注')
    followed2 = models.IntegerField(blank=True, null=True, help_text='关注-悄悄关注-仅对用户')
    like = models.IntegerField(blank=True, null=True, help_text='赞')
    unlike = models.IntegerField(blank=True, null=True, help_text='踩')
    share0 = models.IntegerField(blank=True, null=True, help_text='分享-全量')
    share1 = models.IntegerField(blank=True, null=True, help_text='分享-强烈推荐')
    replied0 = models.IntegerField(blank=True, null=True, help_text='评论或回复-全量')
    replied1 = models.IntegerField(blank=True, null=True, help_text='评论或回复-点赞支持')
    replied2 = models.IntegerField(blank=True, null=True, help_text='评论或回复-吐槽异议')
    replied3 = models.IntegerField(blank=True, null=True, help_text='评论或回复-质疑困惑')
    contain = models.IntegerField(blank=True, null=True, help_text='包含内容的数量')
    link0 = models.IntegerField(blank=True, null=True, help_text='关联-全量')
    link1 = models.IntegerField(blank=True, null=True, help_text='关联-互补互证')
    link2 = models.IntegerField(blank=True, null=True, help_text='关联-互相矛盾')
    time_update = models.DateTimeField(blank=True, null=True, help_text='更新时间')
    searched = models.IntegerField(blank=True, null=True, help_text='某元素搜索后选中查看的数量')
    searched_word = models.CharField(max_length=99, blank=True, null=True, help_text='仅用户可见，用户搜索的')
    sparefield0 = models.CharField(max_length=99, blank=True, null=True)
    sparefield1 = models.CharField(max_length=99, blank=True, null=True)
    sparefield2 = models.CharField(max_length=99, blank=True, null=True)
    sparefield3 = models.CharField(max_length=99, blank=True, null=True)
    

    class Meta:
        db_table = 'statistic'
        verbose_name = '各种元素的统计表'
        verbose_name_plural = verbose_name