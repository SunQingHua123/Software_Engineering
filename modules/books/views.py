# modules/books/views.py

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox, QInputDialog
from modules.books.controllers import create_book, get_books, get_book_by_id, search_books, update_book, delete_book

class BookManager(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('书籍管理系统')
        self.setGeometry(100, 100, 600, 400)
        
        layout = QVBoxLayout()
        
        self.searchBar = QLineEdit(self)
        self.searchBar.setPlaceholderText('输入书籍标题搜索...')
        layout.addWidget(self.searchBar)
        
        self.searchButton = QPushButton('搜索', self)
        self.searchButton.clicked.connect(self.searchBooks)
        layout.addWidget(self.searchButton)
        
        self.bookTable = QTableWidget(self)
        self.bookTable.setColumnCount(4)
        self.bookTable.setHorizontalHeaderLabels(['ID', '书名', '作者', '出版日期'])
        layout.addWidget(self.bookTable)
        
        self.addButton = QPushButton('添加书籍', self)
        self.addButton.clicked.connect(self.addBook)
        layout.addWidget(self.addButton)
        
        self.deleteButton = QPushButton('删除书籍', self)
        self.deleteButton.clicked.connect(self.deleteBook)
        layout.addWidget(self.deleteButton)
        
        self.editButton = QPushButton('修改书籍', self)
        self.editButton.clicked.connect(self.editBook)
        layout.addWidget(self.editButton)
        
        self.setLayout(layout)
        self.searchBooks()
    
    def searchBooks(self):
        title = self.searchBar.text()
        books = search_books(title) if title else get_books()
        self.bookTable.setRowCount(len(books))
        
        for row, book in enumerate(books):
            self.bookTable.setItem(row, 0, QTableWidgetItem(str(book.id)))
            self.bookTable.setItem(row, 1, QTableWidgetItem(book.title))
            self.bookTable.setItem(row, 2, QTableWidgetItem(book.author))
            self.bookTable.setItem(row, 3, QTableWidgetItem(book.published_date.strftime('%Y-%m-%d')))
    
    def addBook(self):
        title, ok1 = QInputDialog.getText(self, '书籍标题', '输入书籍标题:')
        author, ok2 = QInputDialog.getText(self, '书籍作者', '输入书籍作者:')
        published_date, ok3 = QInputDialog.getText(self, '出版日期', '输入出版日期 (YYYY-MM-DD):')
        
        if ok1 and ok2 and ok3:
            try:
                create_book(title=title, author=author, published_date=published_date, isbn='', user_id=1)
                QMessageBox.information(self, '成功', '书籍添加成功')
                self.searchBooks()
            except Exception as e:
                QMessageBox.warning(self, '错误', f'书籍添加失败: {e}')
        else:
            QMessageBox.warning(self, '错误', '输入信息不完整')
    
    def deleteBook(self):
        selected_rows = self.bookTable.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, '警告', '请先选中要删除的书籍')
            return
        
        book_id = int(selected_rows[0].data())
        
        try:
            delete_book(book_id)
            QMessageBox.information(self, '成功', '书籍删除成功')
            self.searchBooks()
        except Exception as e:
            QMessageBox.warning(self, '错误', f'书籍删除失败: {e}')
    
    def editBook(self):
        selected_rows = self.bookTable.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, '警告', '请先选中要编辑的书籍')
            return
        
        book_id = int(selected_rows[0].data())
        book = get_book_by_id(book_id)
        
        if book:
            title, ok1 = QInputDialog.getText(self, '书籍标题', '书籍标题:', text=book.title)
            author, ok2 = QInputDialog.getText(self, '书籍作者', '书籍作者:', text=book.author)
            published_date, ok3 = QInputDialog.getText(self, '出版日期', '出版日期 (YYYY-MM-DD):', text=book.published_date.strftime('%Y-%m-%d'))
            
            if ok1 and ok2 and ok3:
                try:
                    update_book(book_id, title=title, author=author, published_date=published_date, isbn=book.isbn)
                    QMessageBox.information(self, '成功', '书籍信息修改成功')
                    self.searchBooks()
                except Exception as e:
                    QMessageBox.warning(self, '错误', f'书籍信息修改失败: {e}')
            else:
                QMessageBox.warning(self, '错误', '输入信息不完整')
        else:
            QMessageBox.warning(self, '错误', '未找到书籍')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    manager = BookManager()
    manager.show()
    sys.exit(app.exec())