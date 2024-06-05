SOFTWARE_ENGINEERING
│
├── app.py                          # 主应用入口
├── config.py                       # 配置文件（包含SECRET_KEY等配置）
├── requirements.txt                # 项目依赖
│
├── /database
│   ├── __init__.py                 # 数据库初始化
│   ├── models.py                   # 数据库模型定义
│   └── init_db.py                  # 数据库初始化脚本
│
├── /modules
│   ├── /auth                       # 认证模块
│   │   ├── __init__.py
│   │   ├── controllers.py          # 认证相关逻辑
│   │   ├── models.py               # 认证相关的数据库模型
│   │   └── views.py                # 认证相关视图
│   │
│   ├── /users                      # 用户模块
│   │   ├── __init__.py
│   │   ├── controllers.py          # 用户相关逻辑
│   │   ├── models.py               # 用户相关的数据库模型
│   │   └── views.py                # 用户相关视图
│   │
│   ├── /books                      # 书籍模块
│   │   ├── __init__.py
│   │   ├── controllers.py          # 书籍相关逻辑
│   │   ├── models.py               # 书籍相关的数据库模型
│   │   └── views.py                # 书籍相关视图
│   │
│   ├── /reviews                    # 书评模块
│   │   ├── __init__.py
│   │   ├── controllers.py          # 书评相关逻辑
│   │   ├── models.py               # 书评相关的数据库模型
│   │   └── views.py                # 书评相关视图
│   │
│   ├── /circles                    # 圈子模块
│   │   ├── __init__.py
│   │   ├── controllers.py          # 圈子相关逻辑
│   │   ├── models.py               # 圈子相关的数据库模型
│   │   └── views.py                # 圈子相关视图
│   │
│   ├── /messages                   # 消息模块
│   │   ├── __init__.py
│   │   ├── controllers.py          # 消息相关逻辑
│   │   ├── models.py               # 消息相关的数据库模型
│   │   └── views.py                # 消息相关视图
│   │
│   └── /friendships                # 好友关系模块
│       ├── __init__.py
│       ├── controllers.py          # 好友关系相关逻辑
│       ├── models.py               # 好友关系相关的数据库模型
│       └── views.py                # 好友关系相关视图
│
├── /static
│   ├── /css
│   │   └── styles.css              # 自定义CSS样式
│   ├── /js
│   │   └── scripts.js              # 自定义JavaScript脚本
│   └── /images                     # 静态图片
│
└── /templates                      # HTML模板文件
    ├── base.html                   # 基础模板
    ├── index.html                  # 首页模板
    ├── login.html                  # 登录页面模板
    ├── register.html               # 注册页面模板
    ├── profile.html                # 个人主页模板
    ├── book_form.html              # 书籍表单模板
    ├── book_list.html              # 书籍列表模板
    ├── circle_form.html            # 圈子表单模板
    ├── circle_list.html            # 圈子列表模板
    ├── message_list.html           # 消息列表模板
    ├── friend_list.html            # 好友列表模板
<<<<<<< HEAD
    └── review_form.html            # 书评表单模板
=======
    └── review_form.html            # 书评表单模板


>>>>>>> 0683aa9d3a68c4971261fe495944511dfc51d059
