from django.shortcuts import render  
from django.http import JsonResponse  
from django.views.decorators.csrf import csrf_exempt  
from django.views.decorators.http import require_http_methods  
from django.core.cache import cache  
from django.contrib.auth import login  
from django.contrib.auth.models import User  
from django.contrib.auth.hashers import make_password  
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework import (  
    permissions,  
    viewsets,  
    generics,  
    mixins,  
    serializers,  
    status as http_status,  
    exceptions as rf_exceptions  
)  
from rest_framework.decorators import api_view  
from rest_framework.response import Response  
from .models import ItemInfo  
from .serializers import ItemInfoSerializer
from rest_framework_simplejwt.tokens import (  
    RefreshToken,  
    AccessToken  
)  
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.utils import timezone
from rest_framework import status
from django.core.cache import cache
from django.db.models import Model
import json
from .models import Operation  
from .serializers import OperationSerializer  
from django.utils import timezone
from django.utils.crypto import get_random_string
import hashlib
from django.utils.dateparse import parse_datetime
from django.db.models import Q  # 确保导入 Q 对象
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db.models import Case, When, Value, IntegerField
from django.db import transaction


#这里加一个函数，用来搜索某个用户加入的群组，关注的标签，关注的用户包括特别关注，关注的知识元素包括特别关注，屏蔽的用户等
#其中加入的群组和关注的标签，需要返回对象列表，其中含有id、type和title。
#这里在用户登录的时候查询一次，存入redis后，备用。
#列表命名可以为labels、ranges、users、susers、items、sitems，其中susers为特别关注的用户


#这里写两个方法，get_itemlist和get_oplist,可以输入多个参数，
#写两个方法，get_itemdetail,get_opdetail，可以输入多个参数，

#redis缓存，关注列表和当日新闻列表，把今天的新闻列表中正常有效的，全部提取到redis中，某个用户再调阅时就在其中筛选。


#增删改查：对speak的比较特殊。增speak先item后op，删和改speak先op后item，查item不用op，

#加标签操作，标签id应写入item1，调阅时全部调阅。

#测试使用ftp上传文件，并调阅,CESHI


class IsItemOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user0id == request.user.id

class ItemInfoViewSet(viewsets.ModelViewSet):
    queryset = ItemInfo.objects.all()
    serializer_class = ItemInfoSerializer

    @action(detail=False, methods=['post'], url_path='register')
    # 这里是用户注册的模块，手机端和pc端都是共用的。
    def register(self, request):
        try:
            username = request.data.get('username', '').strip()
            if not username or len(username) < 3:
                return Response(
                    {"error": "用户名长度不能小于3位"}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            password1 = request.data.get('password1')
            password2 = request.data.get('password2')

            if not username or not password1 or not password2:
                return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)
            # 检查密码是否相等
            if password1 != password2:
                return Response({"error": "Passwords do not match."}, status=status.HTTP_400_BAD_REQUEST)
            # 检查用户名是否已存在
            with transaction.atomic():
                if ItemInfo.objects.filter(item_title=username).exists():
                    return Response({"error": "该用户名已经被注册."}, status=status.HTTP_400_BAD_REQUEST)
                # 添加数据验证
                if len(password1) < 6:
                    return Response(
                        {"error": "密码长度不能小于6位"}, 
                        status=status.HTTP_400_BAD_REQUEST
                    )
                # 创建用户
                item_info = ItemInfo(
                    item_title=username,
                    sparefield0=make_password(password1),  # 存储加密后的密码在 sparefield0 字段
                    time_create=timezone.now(),
                    item_status='正常有效' , 
                    item_type='人物' , # 
                    item_subtype='注册用户'  ,# 
                    attachment=0,#代表用户头像还没已经上传
                )
                item_info.save()
            return Response({"message": "注册成功!","userid": item_info.item_id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {"error": f"注册失败: {str(e)}"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=False, methods=['post'], url_path='login')
    # 这里是用户登陆的模块，手机端和pc端都是共用的。
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password0')

        if not username or not password:
            return Response({"error": "用户名和密码不能为空"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = ItemInfo.objects.get(item_title=username)
        except ItemInfo.DoesNotExist:
            return Response({"error": "用户不存在"}, status=status.HTTP_404_NOT_FOUND)
        
        if not check_password(password, user.sparefield0):  
            return Response({"error": "密码错误"}, status=status.HTTP_400_BAD_REQUEST)  
   
        user.save()
        return Response({"message": "登录成功", "userid": user.item_id}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path='show_itemlist')
    #这是调阅各个模块中符合条件的元素列表
    #这里要注意，可以把各种状态的段落都查询出来，例如有些段落被删除了，但有些用户也想看。在前端可以显示为灰色，标识为已删除等。
    def show_itemlist(self, request):
        item_type = request.data.get('item_type')  # 从请求中获取 item_type 参数
        id = request.data.get('id')  # 获取传入的 id 参数

        if item_type == '全文目录':
            # 选择 item_type 为文章，而 itemXid=id 的段落记录，以 itemXsn 从小到大的规律排列
            items = ItemInfo.objects.filter(
                item_type='段落',
                itemXid=id
            ).order_by('itemXsn')
        
        elif item_type == 'm推荐阅读':
            # 获取 item_id 为 10000005 的记录
            first_item = ItemInfo.objects.filter(item_id=10000005).first()
            
            # 随机获取9条段落记录，排除指定的 itemXid
            excluded_ids = [10001001, 10001004, 10001003, 10000947, 10000948, 10000949, 10000984, 10000991]
            random_items = ItemInfo.objects.filter(
                item_type='段落',
                item_status='正常有效'
            ).exclude(itemXid__in=excluded_ids).order_by('?')[:9]
            
            # 将 first_item 和 random_items 合并
            items = [first_item] + list(random_items)
        
        elif item_type == 'm朋友组织':
            # 获取人物和群组记录
            items = ItemInfo.objects.filter(
                item_type__in=['人物', '群组'],
                item_status='正常有效'
            ).order_by('-time_create')[:30]

        serializer = ItemInfoSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 在 ItemInfoViewSet 类中添加搜索方法
    @action(detail=False, methods=['post'], url_path='search_items')
    def search_items(self, request):
        keyword = request.data.get('keyword', '').strip()
        
        if not keyword:
            return Response(
                {"error": "请输入搜索关键词"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        try:
            # 使用 Case/When 创建自定义排序字段
            # 段落类型的记录将获得较大的排序值，从而排在后面
            items = ItemInfo.objects.filter(
                Q(item_title__icontains=keyword) |  # 标题包含关键词
                Q(item_content__icontains=keyword),  # 内容包含关键词
                item_status='正常有效'  # 只搜索状态为正常有效的记录
            ).exclude(
                item_type='发言'  # 排除发言类型的记录
            ).annotate(
                custom_order=Case(
                    When(item_type='段落', then=Value(2)),
                    default=Value(1),
                    output_field=IntegerField(),
                )
            ).order_by(
                'custom_order',  # 首先按自定义排序（非段落在前）
                '-time_create'   # 然后按创建时间倒序
            )
            
            serializer = ItemInfoSerializer(items, many=True)
            
            # 返回搜索结果
            return Response({
                "total": len(items),  # 返回找到的记录总数
                "items": serializer.data,  # 返回序列化后的数据
                "message": f"找到 {len(items)} 条相关记录"
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {"error": f"搜索失败: {str(e)}"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


#以下功能是调阅某个元素的所有信息注意，当调阅一个用户言论元素时，要隐藏用户真实的userid和name，只能
    @action(detail=False, methods=['post'], url_path='show_all_iteminfo')
    def show_all_iteminfo(self, request):
        id = request.data.get('id')  
        fetchtype = request.data.get('fetchtype') if 'fetchtype' in request.data else None  

        if fetchtype is None:
            try:  
                item = ItemInfo.objects.get(item_id=id)  
                serializer = ItemInfoSerializer(item)  # 创建序列化器实例
                
                # 检查 user1id 是否为 99999999，匿名者
                if item.user1id == 99999999:
                    response_data = serializer.data
                    # 不下传 user0id 和 user0name
                    response_data.pop('user0id', None)
                    response_data.pop('user0name', None)
                else:
                    response_data = serializer.data  # 包所有字段
                #在这个if语句中，在加入查询user_id和id在op表中是否存在op_type为关注，状态为正常有效的记录，如果有则在response_data中加入一个字段is_followed，值为True，否则为False
                user_id = request.data.get('user_id')
                if user_id:
                    is_followed = Operation.objects.filter(
                        user_id=user_id,
                        item0id=id,
                        op_type='关注',
                        op_status='正常有效'
                    ).exists()
                    response_data['is_followed'] = is_followed
                return Response(response_data, status=status.HTTP_200_OK)  
            except ItemInfo.DoesNotExist:  
                return Response({"error": "该元素信息不存在"}, status=status.HTTP_404_NOT_FOUND) 
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        if fetchtype == 'fetchPrevious':
            try:
                # Fetch the current item
                item = ItemInfo.objects.get(item_id=id)
                # Check if itemXsn is greater than 0 before decrementing
                if item.itemXsn > 0:
                    previous_item = ItemInfo.objects.filter(itemXid=item.itemXid, itemXsn=item.itemXsn - 1).first()
   
                    if previous_item:
                        serializer = ItemInfoSerializer(previous_item)
                        response_data = serializer.data
                        user_id = request.data.get('user_id')
                        if user_id:
                            is_followed = Operation.objects.filter(
                                user_id=user_id,
                                item0id=previous_item.item_id,
                                op_type='关注',
                                op_status='正常有效'
                            ).exists()
                            response_data['is_followed'] = is_followed
                        return Response(response_data, status=status.HTTP_200_OK)
                    else:
                        return Response(
                            {"error": "这是第一段，没有更前面的内容了"},
                            status=status.HTTP_404_NOT_FOUND
                        )
                else:
                    return Response(
                        {"error": "这是第一段，没有更前面的内容了"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            except ItemInfo.DoesNotExist:
                return Response({"error": "该元素信息不存在"}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        if fetchtype == 'fetchNext':
            try:
                # Fetch the current item
                item = ItemInfo.objects.get(item_id=id)
                next_item = ItemInfo.objects.filter(itemXid=item.itemXid, itemXsn=item.itemXsn + 1).first()
                if next_item:
                    serializer = ItemInfoSerializer(next_item)
                    response_data = serializer.data
                    user_id = request.data.get('user_id')
                    if user_id:
                        is_followed = Operation.objects.filter(
                            user_id=user_id,
                            item0id=next_item.item_id,
                            op_type='关注',
                            op_status='正常有效'
                        ).exists()
                        response_data['is_followed'] = is_followed
                    return Response(response_data, status=status.HTTP_200_OK)
                else:
                    return Response(
                        {"error": "这是最后一段，没有更多内容了"},
                        status=status.HTTP_404_NOT_FOUND
                    )
            except ItemInfo.DoesNotExist:
                return Response({"error": "该元素信息不存在"}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



#这里若是不加密写入，则将发言内容写入到item表中item_content中，精简内容写入item_title中，
# 之后将发言内容op表中的ps_content中，
# 若是加密写入，首先加密的文字写入ps_content，精简内容例如X字写入到item0title中，发言密码写入备注0中，发言提示写在备注1中。
#发言内容均不可以为空。
#若读取时应判断，如果是加密发，则输出item_title或item0title，
#如果是非加密发言，则输出ps_content

    @action(detail=False, methods=['post'], url_path='add_speak')
    def add_speak(self, request):
  
        item_content = request.data.get('content')
        is_Anonymous = request.data.get('isAnonymous')
        is_encrypted = request.data.get('isEncrypted')
        password = request.data.get('password')
        password_hint = request.data.get('passwordHint')
        user1id=request.data.get('userid')
        user1name=request.data.get('username')

        #这里需要现实的业务逻辑判断，
        #首先计算item_content的字数长度，存入到变量content_length中。
        #再截取item_content的前十个字，存入到item_title中
        #当is_Anonymous为真时，则标识user1id和user1name为99999999和匿名者，
        #当is_encrypted为真时，则将password用加放置在sparefield0中，password_hint密提示放在sparefield1中，在item_title中写入“user1name的content_length字密文”
 
        # 去 <b> 和 </b> 标签，因为这以后会写入到title中，<b>标签会造成乱码 # 计算内容长度
        item_title = item_content.replace('<b>', '').replace('</b>', '')
        # 截取前十个字
        item_title = item_title[:10] + "..."  # 添加 "..." 到截取的标题后
        content_length = 0

        if is_Anonymous:
            user1id = 99999999
            user1name = "匿名者"
    
        # 处理加密情况!!!!!!
        if is_encrypted:
            # 使用 SHA256 加密密码
            
            hashed_password = hashlib.sha256(password.encode()).hexdigest()  # 加密密码
            # item_title = f"{user1name}的{content_length}字密文"
            content_length = len(item_title)
            item_title = f"{content_length}字密文"
            sparefield0 = hashed_password
            sparefield1 = password_hint

        else:
            sparefield0 = ""
            sparefield1 = ""
    
        # 创建新的 ItemInfo 记录作为发言
        speak_item = ItemInfo(
            item_subtype=request.data.get('subtype'),
            itemXid=request.data.get('publicRange'),
            user0id=request.data.get('userid'),
            user0name=request.data.get('username'),
            time_create=timezone.now(),
            item_status='正常有效',
            item_type='发言',
            item_title=item_title,
            item_content=item_content,
            user1id=user1id,
            user1name=user1name,
            sparefield0=sparefield0,
            sparefield1=sparefield1,
        )
        speak_item.save()

        # 创建 Operation 记录，以下更换spea_item的元素
        operation = Operation(
            op_type = '发言',
            op_status = '正常有效',
            op_range = request.data.get('publicRange'),
            op_time = timezone.now(),
            user_id = request.data.get('userid'),
            user_name = request.data.get('username'),
            ps_content = item_content,
            ps_type = request.data.get('subtype'),
            ps_attitude = '',
            ps_encrypted = content_length,
            item0id = speak_item.item_id,
            item0title = speak_item.item_title,
            item0type = '发言',
            item1id = 0,
            item1title = '',
            item1type = '',
            userXid = user1id,#这里隐藏了匿名者的id，用来下传
            userXname = user1name,#这里记录匿名用户的真实name，不下传
            sparefield0=sparefield0,
            sparefield1=sparefield1,
            sparefield2 = '',
            sparefield3 = '',
        )
        operation.save()

        return Response({"message": "发言成功", "speakId": speak_item.item_id}, status=status.HTTP_201_CREATED)      
            
            

#在这里要写一个op表的模型，用来写入用户的各种行为数据，例如关注了或者分享了等。
class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    
#这里原来是在用户发言放在op表中的情况下写的调阅信息，目前作废不用
    @action(detail=False, methods=['post'], url_path='show_all_opinfo')
    def show_all_opinfo(self, request):
        id = request.data.get('id')  
        try:  
            op = Operation.objects.get(op_id=id)  
            serializer = OperationSerializer(op)  
            return Response(serializer.data, status=status.HTTP_200_OK)  
        except Operation.DoesNotExist:  
            return Response({"error": "该元素信息不存在"}, status=status.HTTP_404_NOT_FOUND) 
            
#这里我想加个模块，接受前端来的op_id，然后查询该op_id的记录，并返回给前端

    @action(detail=False, methods=['post'], url_path='query_op_by_id')
    def query_op_by_id(self, request):
        """根据op_id查询操作记录并返回给前端"""
        op_id = request.data.get('op_id')  
        
        if not op_id:
            return Response({"error": "缺少op_id参数"}, status=status.HTTP_400_BAD_REQUEST)
            
        try:  
            op = Operation.objects.get(op_id=op_id)  
            serializer = OperationSerializer(op)  
            return Response({
                "success": True,
                "data": serializer.data,
                "message": "查询成功"
            }, status=status.HTTP_200_OK)  
        except Operation.DoesNotExist:  
            return Response({"error": "未找到该op_id对应的记录"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": f"查询失败: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



#这里的作用是该元的所有的用户操作记录，用在detailpage表中。
# 这里根据传入的情景场合功能的参数，可以分为获取公开范围的值获取我的标签，获取今日新闻，获取相关元素的用户操作记录获取相关元的关联记录，获取我关注屏蔽的用户数据，取某群组内的信息，获取某用户的操作历史
#在这里可以先将涉及用户本人的操作记录查询来，再存入到redis中，然后前端调阅时，先从redis中查询，如果没有则查询数��库，查到后存入redis，然后返回前端


    @action(detail=False, methods=['post'], url_path='get_oplist')  
    def get_oplist(self, request):  
        user_id = request.data.get('user_id')  # 修改为从 request.data 获取 user_id
        op_type = request.data.get('op_type')  # 新增的可选参数

        if user_id is None:  # 检查user_id是否存在
            return Response({"error": "少用户ID"}, status=status.HTTP_400_BAD_REQUEST)  
        
        try:  
            # 使用filter来过滤所有匹配item0id的记录  
            operations = Operation.objects.filter(user_id=user_id) # 根据user_id过滤并按op_time降序排列
            # if not operations:  
            #     return Response({"error": "没有找到匹配该元素的记录"}, status=status.HTTP_404_NOT_FOUND)  
#这里需要重估一下，需要判断operations是否存在么？

            if op_type == '获取范围值':
                operations = operations.filter(op_type='加入', item0type='群组').order_by('-op_time')  # 根据作类型过滤
            elif op_type == '获取我的标签':
                operations = operations.filter(op_type='关注', item0type='标签').order_by('-op_time')  # 根据作类型过滤
            elif op_type == 'm关注收藏':
                operations = operations.filter(op_type='关注', op_status='正常有效').order_by('-op_time')
    
            elif op_type == 'm用户动态':
                operations = operations.filter(
                    userXid=user_id,
                    op_range=99999999,
                    op_type__in=['发言', '分享'],  # 查询 op_type 为 '发言' 或 '分享'
                    op_status='正常有效'
                ).order_by('-op_time')[:10]
            elif op_type == '新闻动态-用户动态' or op_type == 'm新闻动态':
                #这里的我关注的知识元素的内容动态，包括关联，加标签，
                try:
                    operations0 = operations.filter(op_type='关注', op_status='正常有效', item0type='人物')  # 根据操作类型过滤
                    item0_ids = list(operations0.values_list('item0id', flat=True))
                    
                    # 确保 user_id 是有效的整数
                    if user_id is not None:
                        item0_ids.append(int(user_id))  # 添加用户本人到列表中，确保为数字格式
                    
                    item0_ids.extend([10000046])  # 添加固定的ID
                    item0_ids = list(set(item0_ids))  # 去除重复的ID
                    
                    # 确保 item0_ids 不为空
                    if item0_ids:
                        operations = Operation.objects.filter(
                            user_id__in=item0_ids,
                            op_type__in=['发言', '分享'],  # 查询 op_type 为 '发言' 或 '分享'
                            op_status='正常有效'
                        ).order_by('-op_time')
                    else:
                        operations = []  # 如果 item0_ids 为空，返回空列表
                except Exception as e:
                    return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            elif op_type == '新闻动态-内容动态':
                #这里的我关注的知识元素的内容动态，包括关联，加标签，
                operations0 = operations.filter(op_type='关注', op_status='正常有效')  # 根据操作类型过滤
                operations0 = operations0.exclude(item0type='人物')  # 根据作类型滤
                item0_ids = list(operations0.values_list('item0id', flat=True))
                operations1 = Operation.objects.filter(
                    item0id__in=item0_ids,
                    op_type='关联',  # 查询 op_type 为 '发言' 或 '分享'
                    op_status='正常有效')
                operations2 = Operation.objects.filter(
                    item1id__in=item0_ids,
                    op_type='加标签',  # 查询 op_type 为 '发言' 或 '分享'
                    op_status='正常有效')
                # 合并两个查询集并去重
                operations = operations1.union(operations2).order_by('-op_time')
                
            serializer = OperationSerializer(operations, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)  
        
        except Exception as e:  
            # 捕获任何可能的异常，并返回错误响应  
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        #里加一个功能，当我们调阅用户操作列表时，新增一个判断字段，如果匿名者是用户本人则如何，详细代码最下


   
            
#这里增加一个新增用户操作的命令，
#这里还要继续判断，如果是关注，关联，加标签，加群组，屏蔽，采纳等操作，则需要先查询是否有相关的记录，
#如果是关联，则需要同时添加两条记录，如果是加标签，则需要将标签加入到item1中，
#这里是手机端和pc端通用的模块
    @action(detail=False, methods=['post'], url_path='add_op')
    def add_op(self, request):
        data = request.data

        # 从请求数据中提取所需字段
        user_id = data.get('userid')
        username = data.get('username')
        op_type = data.get('itemtype')  # 操作类型
        item0id = data.get('item0id')
        item0title = data.get('item0title')
        item0type = data.get('item0type')
        item1id = data.get('item1id', 0)
        subtype = data.get('subtype')
        op_range = data.get('publicRange')
        content = data.get('content')
        is_encrypted = data.get('isEncrypted', False)
        is_Anonymous = data.get('isAnonymous', False)
        password = data.get('password', '')
        password_hint = data.get('passwordHint', '')
        userXid = 99999999
        userXname = "匿名者"


#这里需要判断，如果段落的话，item0或item1，应该要加入段落所属的文章名

        # 理加密情况
        if is_encrypted:
            # 使用 SHA256 加密密码
            hashed_password = hashlib.sha256(password.encode()).hexdigest()  # 加密密码
        else:
            hashed_password = ""

        if is_Anonymous == False:
            userXid = user_id
            userXname = username

        # 创建 Operation 记录
        operation_data = {
            'op_type': op_type,
            'op_status': '正常有效',
            'op_range': op_range,
            'op_time': timezone.now(),
            'user_id': user_id,
            'user_name': username,
            'ps_content': content,
            'ps_type': subtype,
            'ps_attitude': '',  # 可以根据需要设置
            'ps_encrypted': is_encrypted,
            'item0id': item0id,
            'item0title': item0title,
            'item0type': item0type,
            'item1id': item1id,
            'item1title': '',  # 可以根据需要设置
            'item1type': '',  # 可以根据需要设置
            'userXid': userXid,  # 这里可能需要根据实际情况调整
            'userXname': userXname,  # 这里可能需要根据实际情况调整
            'sparefield0': hashed_password,  # 存储加密后的密码
            'sparefield1': password_hint if is_encrypted else '',
            'sparefield2': '',
            'sparefield3': '',
        }

        try:
            # 这是如果是关注的话，就要查询是否有相关item0id和user_id的关注记录，如果有则不添加，如果没有则添加，
            if op_type == '关注':
                existing_op = Operation.objects.filter(user_id=user_id, item0id=item0id, op_type='关注').first()
                if existing_op:
                    return Response({'success': False, 'message': '已经关注过该元素'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    # 如果没有关注，则添加关注记录
                    Operation.objects.create(user_id=user_id, item0id=item0id, op_type='关注')
                    return Response({'success': True, 'message': '关注成功'}, status=status.HTTP_201_CREATED)
            # 如果op_type是'关联'，则保存两次，交换item0id和item1id
            if op_type == '关联':
                # 保存第一次记录
                operation = Operation(**operation_data)
                operation.save()

                # 交换item0id和item1id
                operation_data['item0id'], operation_data['item1id'] = operation_data['item1id'], operation_data['item0id']
                
                # 保存第二次记录
                operation = Operation(**operation_data)
                operation.save()
            else:
                # 其他情况只保存一次
                operation = Operation(**operation_data)
                operation.save()

            return Response({'success': True, 'message': '操作已成功添加', 'op_id': operation.op_id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# 以上是我django的代码设计，我这里向加一个方法show_mtodaynews的功能，即接收到前端传来的userid然后查询Operation表中字段user_id=userid，且op_type为关注的记录，再抽取这些记录中关注的item0type为“用户”的所有item0id，再查Operation表中字段user_id为这些item0id的所有记录，返回前端

# class RedisCacheManager:
#     @staticmethod
#     def set_list(key, queryset, timeout=None):
#         data = [item.to_dict() for item in queryset]
#         cache.set(key, json.dumps(data), timeout)

#     @staticmethod
#     def get_list(key):
#         data = cache.get(key)
#         return json.loads(data) if data else None

#     @staticmethod
#     def delete(key):
#         cache.delete(key)

# class OperationViewSet(viewsets.ModelViewSet):
#     queryset = Operation.objects.all()
#     serializer_class = OperationSerializer

#     def fetch_and_cache_followed_operations(self, userid):
#         """查询关注的记录并存入缓存"""
#         cache_key = f"followed_operations_{userid}"
#         followed_operations = RedisCacheManager.get_list(cache_key)

#         if followed_operations is None:
#             # 如果缓存中没有，查询数据库
#             followed_operations = Operation.objects.filter(user_id=userid, op_type='关注', item0type='用户')
#             if not followed_operations.exists():
#                 return None  # 返回 None 表示没找到记录

#             # 将关注的记录存入缓存
#             RedisCacheManager.set_list(cache_key, followed_operations, timeout=3600)

#         return followed_operations

#     @action(detail=False, methods=['post'], url_path='show_mtodaynews')
#     def show_mtodaynews(self, request):
#         userid_str = request.data.get('userid')
        
#         if userid_str is None:
#             return Response({"error": "缺少必要的userid参数"}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             userid = int(userid_str)
#         except ValueError:
#             return Response({"error": "userid 必须是一个有效的数字"}, status=status.HTTP_400_BAD_REQUEST)

#         # 获取关注的记录
#         followed_operations = self.fetch_and_cache_followed_operations(userid)
#         if followed_operations is None:
#             return Response({"message": "没有找到关注的用户记录"}, status=status.HTTP_404_NOT_FOUND)

#         # 提取关注的 item0ids
#         followed_item0ids = followed_operations.values_list('item0id', flat=True)

#         # 尝试从缓存中获取相关的操作记录
#         related_cache_key = f"mtodaynews_{userid}"
#         related_operations = RedisCacheManager.get_list(related_cache_key)

#         if related_operations is None:
#             # 如果缓存中没有，查询数据库
#             related_operations = Operation.objects.filter(user_id__in=followed_item0ids)
#             if not related_operations.exists():
#                 return Response({"message": "没有到相关的操记录"}, status=status.HTTP_404_NOT_FOUND)

#             # 将相关的操作记录存入缓存
#             RedisCacheManager.set_list(related_cache_key, related_operations, timeout=3600)

#         # 序列化结果
#         serializer = OperationSerializer(related_operations, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# 在 add_op和delete_op 方法中：在成功关注或取消关注操作后，调用 update_followed_operations_cache 方法更缓存。

#  # 更新缓存
#         self.update_followed_operations_cache(user.id)
        
# def update_followed_operations_cache(self, userid):
#     """更新关注的记录缓存"""
#     cache_key = f"followed_operations_{userid}"
#     followed_operations = Operation.objects.filter(user_id=userid, op_type='关注', item0type='用户')
#     RedisCacheManager.set_list(cache_key, followed_operations, timeout=3600)


#这是测试的模块
class RedisCacheManager:
    @staticmethod
    def set_list(key, queryset, timeout=None):
        # 添加序列化错误处理
        try:
            data = [item.to_dict() for item in queryset]
            cache.set(key, json.dumps(data), timeout)
        except (AttributeError, TypeError) as e:
            logger.error(f"Cache serialization error: {str(e)}")
            return None

    @staticmethod
    def get_list(key):
        data = cache.get(key)
        return json.loads(data) if data else None

    @staticmethod
    def delete(key):
        cache.delete(key)
        
        
def get_users_list():
    cache_key = 'users_list'
    users = RedisCacheManager.get_list(cache_key)
    if not users:
        users = list(ItemInfo.objects.filter(item_subtype='注册用户'))  # 转换为列表
        RedisCacheManager.set_list(cache_key, users, timeout=3600)
    return users

@api_view(['GET'])
def users_list(request):
    users = get_users_list()
    serializer = ItemInfoSerializer(users, many=True)
    return Response(serializer.data)
    
    
    



#这是测试用的模块
@api_view(['GET'])
def get_first_item(request):
    try:
        # first_item = ItemInfo.objects.order_by('item_id').all()
        first_item = ItemInfo.objects.order_by('item_id').first()
        # first_item_id = first_item.item_type if first_item else None
        if first_item:
            # serializer = ItemInfoSerializer(first_item)
            # return Response(serializer.data)
            
            response_data = {
                'item_id': first_item.item_id,
                'item_title': first_item.item_title,
            }
            return Response(response_data)
            
            
        return Response({'message': 'No items found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({'message': 'This is a protected view accessible only with a valid JWT.'})


@csrf_exempt
@require_http_methods(["GET"])
def ceshi(request):
    try:
        # 假设JWT是通过HTTP头部的Authorization传递的，格式为 "Bearer <token>"
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            raise Exception("Authorization header is missing.")
        # 分割Bearer和Token
        parts = auth_header.split()
        if parts[0].lower() != 'bearer':
            raise Exception("Authorization header must start with Bearer")
        elif len(parts) == 1:
            raise Exception("Token not found")
        elif len(parts) > 2:
            raise Exception("Authorization header must be Bearer token")
        token = parts[1]
        try:
            # 尝试解析和验证JWT
            refresh_token = RefreshToken(token)
            # 如果token效，可以访问其payload中的数据，例如：
            # user_id = refresh_token.payload.get('user_id')
            # 这里是测试代码，如果JWT有效，返回成功信息
            return JsonResponse({'message': 'JWT is valid'})
        except (InvalidToken, TokenError) as e:
            # 如果JWT无效，抛出异常
            raise Exception("Invalid token") from e
        #如果你收到了 {"error": "Authorization header is missing."} 的响应，这意味着你的请求没有包含必要的 Authorization头部信息，或者头部信息没有按照预期的格式发送。为了解这个问题，请确保你在发送请求时包含了正确的 Authorization 头部，并且它的格式是 Bearer <your-token>，其中 <your-token> 是你通过 rest_framework_simplejwt 生成的JWT。以下是一些示例，展示了如何在不同的客户端中设置 Authorization 头部：curl -H "Authorization: Bearer your-token-here" http://your-server-url/your-endpoint/
            
        # # 以下是测试redis，首先设置redis缓存  
        # cache.set('my_key', 'hello, world', 300)  # 缓存数据 300 秒  
        # # 获取redis缓存  
        # first_item_id = cache.get('my_key')  
        # return JsonResponse({'first_item_id': first_item_id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    

def index(request):  
    return render(request, 'index.html')
    
    
    
    
     
# from django.db.models import Case, When, Value, IntegerField
# from rest_framework import viewsets
# from .models import YourModel
# from .serializers import YourModelSerializer

# class YourModelViewSet(viewsets.ModelViewSet):
#     queryset = YourModel.objects.all()
#     serializer_class = YourModelSerializer

#     def get_queryset(self):
#         user_id = self.request.query_params.get('id')
        
#         queryset = YourModel.objects.annotate(
#             isaaa=Case(
#                 When(userid=user_id, kkk=999, then=Value(1)),
#                 default=Value(0),
#                 output_field=IntegerField()
#             )
#         )
        
#         return queryset
# ```

# 这个实现的关键点如下:

# 1. 我们使用 `annotate()` 方法来添加一个新的字段 `isaaa` 到查询结中。

# 2. 在 `annotate()` 中,我们使用 `Case` 表达式来定义条件逻辑。

# 3. `When` 子句定义了条件: 当 `userid` 等于请求的 `id` 参数且 `kkk` 字段为 999 时。

# 4. 如果条件满足,`then=Value(1)` 将 `isaaa` 设为 1。

# 5. `default=Value(0)` 确保在条件不满足时 `isaaa` 被设置为 0。

# 6. `output_field=IntegerField()` 指定 `isaaa` 字段的类型为整数。

# 在你的序列化器中,确保包含 `isaaa` 段:

# ```python
# class YourModelSerializer(serializers.ModelSerializer):
#     isaaa = serializers.IntegerField()

#     class Meta:
#         model = YourModel
#         fields = ['id', 'userid', 'kkk', 'isaaa', ...]  # 包含所有你需要的字段











