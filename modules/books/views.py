import os
import sys

# 将上级目录添加到系统路径中，以便导入模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")
from flask import Blueprint, render_template, request, redirect, url_for
from modules.books.controllers import create_book, get_books, search_books, get_book_by_id, update_book, delete_book

books_bp = Blueprint('books', __name__, template_folder='../../templates')

@books_bp.route('/')
def index():
    search = request.args.get('search')
    sort = request.args.get('sort')
    books = search_books(search, sort) if search else get_books(sort)
    return render_template('book_list.html', books=books)

@books_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        published_date = request.form['published_date']
        isbn = request.form['isbn']
        create_book(title, author, published_date, isbn)
        return redirect(url_for('books.index'))
    return render_template('book_form.html', form_title='添加书籍', book=None)

@books_bp.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit(book_id):
    book = get_book_by_id(book_id)
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        published_date = request.form['published_date']
        isbn = request.form['isbn']
        update_book(book_id, title, author, published_date, isbn)
        return redirect(url_for('books.index'))
    return render_template('book_form.html', form_title='编辑书籍', book=book)

@books_bp.route('/delete/<int:book_id>', methods=['POST'])
def delete(book_id):
    delete_book(book_id)
    return redirect(url_for('books.index'))
