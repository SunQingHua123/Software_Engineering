from database.models import create_tables

def init_db():
    create_tables()

if __name__ == '__main__':
    init_db()
