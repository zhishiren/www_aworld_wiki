"""
URL configuration for aworld2024 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
# from django.views import TemplateView
from aworld20240617 import views
# 导入TemplateView
from django.views.generic.base import TemplateView

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from aworld20240617 import views
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  
from aworld20240617.views import ItemInfoViewSet,OperationViewSet,get_first_item, protected_view #这里��加上aworld20240617.views，而不是.views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



router = DefaultRouter()
router.register(r'iteminfo', views.ItemInfoViewSet)
router.register(r'opinfo', views.OperationViewSet)  # 这里已经注册了OperationViewSet

# 添加新的URL路径
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api/get-first-item/', views.get_first_item, name='get_first_item'),
    path('api/ceshi/', views.ceshi, name='ceshi'),  # 配置一个URL路径'ceshi/'来指向ceshi视图函数  
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  #这是测试token的功能，但在网页中暂时不用
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  #这是测试token的功能，但在网页中暂时不用
    path('api/protected/', protected_view, name='protected_view'),
    path('api/users/', views.users_list, name='users_list'),
]


