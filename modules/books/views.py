# modules/books/views.py

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox
from .controllers import create_book, get_books, get_book_by_id, search_books, update_book, delete_book
import datetime

class BookManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("书籍管理")
        self.setGeometry(300, 300, 600, 400)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)
        
        self.book_list = QListWidget()
        self.layout.addWidget(self.book_list)
        
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("书籍标题")
        self.layout.addWidget(self.title_input)
        
        self.author_input = QLineEdit()
        self.author_input.setPlaceholderText("书籍作者")
        self.layout.addWidget(self.author_input)
        
        self.date_input = QLineEdit()
        self.date_input.setPlaceholderText("出版日期 (YYYY-MM-DD)")
        self.layout.addWidget(self.date_input)
        
        self.isbn_input = QLineEdit()
        self.isbn_input.setPlaceholderText("ISBN")
        self.layout.addWidget(self.isbn_input)
        
        self.add_button = QPushButton("添加书籍")
        self.add_button.clicked.connect(self.add_book)
        self.layout.addWidget(self.add_button)
        
        self.update_button = QPushButton("更新书籍")
        self.update_button.clicked.connect(self.update_book)
        self.layout.addWidget(self.update_button)
        
        self.delete_button = QPushButton("删除书籍")
        self.delete_button.clicked.connect(self.delete_book)
        self.layout.addWidget(self.delete_button)
        
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("搜索书籍")
        self.layout.addWidget(self.search_input)
        
        self.search_button = QPushButton("搜索")
        self.search_button.clicked.connect(self.search_books)
        self.layout.addWidget(self.search_button)
        
        self.load_books()
        
    def load_books(self):
        self.book_list.clear()
        books = get_books()
        for book in books:
            self.book_list.addItem(f"{book.id}: {book.title} - {book.author}")

    def add_book(self):
        title = self.title_input.text()
        author = self.author_input.text()
        try:
            published_date = datetime.datetime.strptime(self.date_input.text(), "%Y-%m-%d")
        except ValueError:
            published_date = None
        isbn = self.isbn_input.text()
        user_id = 1  # 假设当前用户ID为1
        create_book(title, author, published_date, isbn, user_id)
        self.load_books()
        
    def update_book(self):
        selected_item = self.book_list.currentItem()
        if selected_item:
            book_id = int(selected_item.text().split(":")[0])
            title = self.title_input.text()
            author = self.author_input.text()
            try:
                published_date = datetime.datetime.strptime(self.date_input.text(), "%Y-%m-%d")
            except ValueError:
                published_date = None
            isbn = self.isbn_input.text()
            update_book(book_id, title, author, published_date, isbn)
            self.load_books()
            
    def delete_book(self):
        selected_item = self.book_list.currentItem()
        if selected_item:
            book_id = int(selected_item.text().split(":")[0])
            delete_book(book_id)
            self.load_books()
            
    def search_books(self):
        query = self.search_input.text()
        books = search_books(query)
        self.book_list.clear()
        for book in books:
            self.book_list.addItem(f"{book.id}: {book.title} - {book.author}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BookManager()
    window.show()
    sys.exit(app.exec())
