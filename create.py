import os

# 定义项目目录结构
project_structure = {
    "my_project": {
        "src": {
            "__init__.py": "",
            "main.py": "",
            "application": {
                "__init__.py": "",
                "application.py": "",
                "services": {
                    "__init__.py": "",
                    "auth_service.py": "",
                    "user_service.py": "",
                    "book_service.py": "",
                    "review_service.py": "",
                    "circle_service.py": "",
                    "message_service.py": ""
                }
            },
            "modules": {
                "auth": {
                    "__init__.py": "",
                    "models.py": "",
                    "controllers.py": "",
                    "views.py": ""
                },
                "users": {
                    "__init__.py": "",
                    "models.py": "",
                    "controllers.py": "",
                    "views.py": ""
                },
                "books": {
                    "__init__.py": "",
                    "models.py": "",
                    "controllers.py": "",
                    "views.py": ""
                },
                "reviews": {
                    "__init__.py": "",
                    "models.py": "",
                    "controllers.py": "",
                    "views.py": ""
                },
                "circles": {
                    "__init__.py": "",
                    "models.py": "",
                    "controllers.py": "",
                    "views.py": ""
                },
                "messages": {
                    "__init__.py": "",
                    "models.py": "",
                    "controllers.py": "",
                    "views.py": ""
                }
            },
            "utils": {
                "__init__.py": "",
                "common.py": "",
                "config.py": "",
                "logging.py": ""
            }
        },
        "database": {
            "__init__.py": "",
            "models.py": "",
            "session.py": "",
            "schema.sql": "",
            "alembic": {
                "__init__.py": "",
                "env.py": "",
                "versions": {}
            }
        },
        "tests": {
            "__init__.py": "",
            "test_auth.py": "",
            "test_users.py": "",
            "test_books.py": "",
            "test_reviews.py": "",
            "test_circles.py": "",
            "test_messages.py": ""
        },
        "static": {},
        "templates": {},
        "requirements.txt": "",
    }
}

# 函数用于递归创建目录和文件
def create_structure(structure, path=""):
    for key, value in structure.items():
        current_path = os.path.join(path, key) if path else key
        if isinstance(value, dict):
            os.makedirs(current_path, exist_ok=True)
            create_structure(value, current_path)
        elif isinstance(value, str):
            with open(current_path, "w") as f:
                f.write(value)

# 指定项目根目录
project_root = "C:/Users/86150/Desktop/大学课程/2024软件工程/Software_Engineering"

# 创建项目结构
create_structure(project_structure, project_root)

print("Project structure created successfully.")