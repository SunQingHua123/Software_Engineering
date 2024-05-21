# Software_Engineering
2024春季学期软件工程code

Software_Engineering/
│
├── src/
│   ├── __init__.py
│   ├── main.py            # 应用的入口点
│
├── application/
│   ├── __init__.py
│   ├── application.py     # 应用配置和初始化代码
│   └── services/          # 应用服务层
│       ├── __init__.py
│       ├── auth_service.py # 认证服务
│       ├── user_service.py  # 用户服务
│       ├── book_service.py  # 书籍服务
│       ├── review_service.py # 书评服务
│       ├── circle_service.py # 圈子服务
│       └── message_service.py # 消息服务
│
├── modules/
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── models.py       # 认证模块的数据模型
│   │   ├── controllers.py   # 认证模块的业务逻辑
│   │   └── views.py         # 认证模块的GUI视图
│   ├── users/
│   │   ├── __init__.py
│   │   ├── models.py        # 用户模块的数据模型
│   │   ├── controllers.py    # 用户模块的业务逻辑
│   │   └── views.py          # 用户模块的GUI视图
│   ├── books/
│   │   ├── __init__.py
│   │   ├── models.py        # 书籍模块的数据模型
│   │   ├── controllers.py   # 书籍模块的业务逻辑
│   │   └── views.py         # 书籍模块的GUI视图
│   ├── reviews/
│   │   ├── __init__.py
│   │   ├── models.py        # 书评模块的数据模型
│   │   ├── controllers.py   # 书评模块的业务逻辑
│   │   └── views.py         # 书评模块的GUI视图
│   ├── circles/
│   │   ├── __init__.py
│   │   ├── models.py        # 圈子模块的数据模型
│   │   ├── controllers.py   # 圈子模块的业务逻辑
│   │   └── views.py         # 圈子模块的GUI视图
│   └── messages/
│       ├── __init__.py
│       ├── models.py        # 消息模块的数据模型
│       ├── controllers.py   # 消息模块的业务逻辑
│       └── views.py         # 消息模块的GUI视图
│
├── database/
│   ├── __init__.py
│   ├── models.py           # 数据库模型基类
│   ├── session.py          # 数据库会话管理
│   ├── schema.sql          # 数据库初始化脚本
│   └── alembic/            # Alembic 迁移目录（如果使用）
│       ├── __init__.py
│       ├── env.py
│       └── versions/
│
├── utils/
│   ├── __init__.py
│   ├── common.py           # 通用工具函数
│   ├── config.py           # 配置文件读取
│   └── logging.py          # 日志配置
│
├── tests/
│   ├── __init__.py
│   ├── test_auth.py        # 认证模块的单元测试
│   ├── test_users.py       # 用户模块的单元测试
│   ├── test_books.py       # 书籍模块的单元测试
│   ├── test_reviews.py     # 书评模块的单元测试
│   ├── test_circles.py     # 圈子模块的单元测试
│   └── test_messages.py    # 消息模块的单元测试
│
├── static/
│   └── ...                 # 静态文件，如图片、样式等（如果使用）
├── templates/
│   └── ...                 # 模板文件，如HTML模板（如果使用）
├── .gitignore
├── README.md
├── requirements.txt       # 项目依赖
