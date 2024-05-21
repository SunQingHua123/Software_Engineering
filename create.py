import os

# 定义项目结构
project_structure = {
        "src": ["__init__.py", "main.py"],
        "application": {
            "__init__.py": "",
            "application.py": "",
            "services": ["__init__.py", "auth_service.py", "user_service.py", "book_service.py", "review_service.py", "circle_service.py", "message_service.py"]
        },
        "modules": {
            "auth": ["__init__.py", "models.py", "controllers.py", "views.py"],
            "users": ["__init__.py", "models.py", "controllers.py", "views.py"],
            "books": ["__init__.py", "models.py", "controllers.py", "views.py"],
            "reviews": ["__init__.py", "models.py", "controllers.py", "views.py"],
            "circles": ["__init__.py", "models.py", "controllers.py", "views.py"],
            "messages": ["__init__.py", "models.py", "controllers.py", "views.py"]
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
        "utils": ["__init__.py", "common.py", "config.py", "logging.py"],
        "tests": ["__init__.py", "test_auth.py", "test_users.py", "test_books.py", "test_reviews.py", "test_circles.py", "test_messages.py"],
        "static": {},
        "templates": {},
        "requirements.txt": "",
        ".env": ""
    }

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        elif isinstance(content, list):
            os.makedirs(path, exist_ok=True)
            for item in content:
                item_path = os.path.join(path, item)
                with open(item_path, 'w') as f:
                    pass
        else:
            with open(path, 'w') as f:
                f.write(content)

if __name__ == "__main__":
    base_path = "."
    create_structure(base_path, project_structure)
    print("项目结构已生成！")
