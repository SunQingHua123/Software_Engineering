import os

# 项目根目录
project_root = os.path.dirname(os.path.abspath(__file__))

# 目录和文件结构
structure = {
    "migrations": [],
    "database": ["__init__.py", "models.py", "init_db.py"],
    "modules": {
        "auth": ["__init__.py", "controllers.py", "models.py", "views.py"],
        "users": ["__init__.py", "controllers.py", "models.py", "views.py"],
        "books": ["__init__.py", "controllers.py", "models.py", "views.py"],
        "reviews": ["__init__.py", "controllers.py", "models.py", "views.py"],
        "circles": ["__init__.py", "controllers.py", "models.py", "views.py"],
        "messages": ["__init__.py", "controllers.py", "models.py", "views.py"],
        "friendships": ["__init__.py", "controllers.py", "models.py", "views.py"],
    },
    "static": {
        "css": ["styles.css"],
        "js": ["scripts.js"],
        "images": []
    },
    "templates": [
        "base.html", "index.html", "login.html", "register.html", "profile.html",
        "book_form.html", "book_list.html", "circle_form.html", "circle_list.html",
        "message_list.html", "friend_list.html", "review_form.html"
    ],
    ".": ["app.py", "config.py", "requirements.txt", "README.md"]
}

# 创建目录和文件
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            os.makedirs(path, exist_ok=True)
            for file_name in content:
                file_path = os.path.join(base_path, name, file_name)
                if not os.path.exists(file_path):
                    with open(file_path, 'w') as file:
                        pass

# 运行脚本创建结构
if __name__ == "__main__":
    create_structure(project_root, structure)
    print("项目结构创建完成！")
