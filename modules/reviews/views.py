import os
import sys

# 将上级目录添加到系统路径中，以便导入模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")
from flask import Blueprint, render_template, request, redirect, url_for
from modules.reviews.controllers import ReviewService

reviews_bp = Blueprint('reviews', __name__, template_folder='../../templates')

@reviews_bp.route('/')
def index():
    reviews = ReviewService.get_all_reviews()
    return render_template('review_list.html', reviews=reviews)

@reviews_bp.route('/delete/<int:review_id>', methods=['POST'])
def delete(review_id):
    ReviewService.delete_review(review_id)
    return redirect(url_for('reviews.index'))

@reviews_bp.route('/statistics')
def statistics():
    stats = ReviewService.review_statistics()
    return render_template('review_statistics.html', stats=stats)

@reviews_bp.route('/recommend')
def recommend():
    limit = request.args.get('limit', default=10, type=int)
    recommended_reviews = ReviewService.recommend_reviews(limit)
    return render_template('review_recommendations.html', reviews=recommended_reviews)

@reviews_bp.route('/create', methods=['POST'])
def create():
    content = request.form.get('content')
    rating = request.form.get('rating')
    user_id = request.form.get('user_id')
    book_id = request.form.get('book_id')
    
    # 验证表单数据
    if not content or not rating or not user_id or not book_id:
        # 处理缺少参数的情况
        return "缺少必要的参数", 400
    
    try:
        rating = int(rating)
        if rating < 1 or rating > 5:
            # 处理评分范围不正确的情况
            return "评分必须在1到5之间", 400
    except ValueError:
        # 处理评分不是整数的情况
        return "评分必须是整数", 400
    
    ReviewService.create_review(content, rating, user_id, book_id)
    
    return redirect(url_for('reviews.index'))