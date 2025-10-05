from .models import ItemInfo
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Operation  
  
class OperationSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Operation  
        exclude = ('user_id', 'user_name','sparefield0')  # 这里为了隐藏匿名发言者的真实用户信息，只调取userXid的信息,'sparefield0'是用户的发言密码，也不能下传


class ItemInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemInfo
        exclude = ('sparefield0',) 

