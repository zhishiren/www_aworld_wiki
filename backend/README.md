# Django 后端 API

基于Django和Django REST Framework构建的后端API服务。

## 🚀 快速开始

### 1. 安装依赖
```bash
cd backend
pip install -r requirements.txt
```

### 2. 环境配置
```bash
# 复制环境变量模板
cp .env.example .env
# 编辑 .env 文件，填入真实的配置值
```

### 3. 数据库迁移
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. 创建超级用户
```bash
python manage.py createsuperuser
```

### 5. 运行开发服务器
```bash
python manage.py runserver
```

## 📁 项目结构
```
backend/
├── manage.py              # Django管理脚本
├── requirements.txt       # Python依赖
├── .env.example          # 环境变量模板
├── project_config/       # Django项目配置
│   ├── settings.py       # 项目设置
│   ├── urls.py          # URL路由
│   └── wsgi.py          # WSGI配置
└── api_app/             # API应用
    ├── models.py        # 数据模型
    ├── views.py         # 视图函数
    ├── serializers.py   # 序列化器
    └── migrations/      # 数据库迁移
```

## 🔧 技术栈
- **框架**: Django 5.0.2
- **API**: Django REST Framework
- **数据库**: MySQL
- **缓存**: Redis
- **认证**: JWT (Simple JWT)

## 🌐 API接口
服务运行在 `http://localhost:8000`

- `/admin/` - Django管理后台
- `/api/iteminfo/` - 项目信息接口
- `/api/auth/` - 认证相关接口

## ⚠️ 注意事项
- 生产环境请务必修改SECRET_KEY
- 设置正确的数据库连接信息
- 配置环境变量而不是硬编码敏感信息