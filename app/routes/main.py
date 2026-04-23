from flask import Blueprint, render_template, request, redirect, url_for, flash

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    """
    首頁 (店家列表)
    - 處理: 取出所有 Restaurant
    - 輸出: 渲染 main/index.html
    """
    pass

@main_bp.route('/restaurant/<int:id>', methods=['GET'])
def restaurant_detail(id):
    """
    店家專頁與數位菜單
    - 處理: 取出指定 Restaurant 及其對應的 MenuItem
    - 輸出: 渲染 main/restaurant_detail.html
    """
    pass

@main_bp.route('/checkout', methods=['GET'])
def checkout_page():
    """
    結帳與確認頁面
    - 處理: 檢查登入狀態，顯示購物車商品與取餐時間表單
    - 輸出: 渲染 main/checkout.html
    """
    pass

@main_bp.route('/checkout', methods=['POST'])
def submit_order():
    """
    送出訂單
    - 處理: 檢查登入，計算總額，建立 Order 與 OrderItem
    - 輸出: 重導向至單筆訂單狀態頁 (order_status)
    """
    pass

@main_bp.route('/orders', methods=['GET'])
def my_orders():
    """
    歷史訂單列表
    - 處理: 根據登入 user_id 取出所有 Order
    - 輸出: 渲染 main/orders.html
    """
    pass

@main_bp.route('/order/<int:id>', methods=['GET'])
def order_status(id):
    """
    單筆訂單狀態
    - 處理: 取出指定 Order 與明細，確認該訂單屬於當前使用者
    - 輸出: 渲染 main/order_status.html
    """
    pass
