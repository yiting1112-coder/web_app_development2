from flask import Blueprint, render_template, request, redirect, url_for, flash

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['GET'])
def register_page():
    """顯示註冊表單頁面"""
    pass

@auth_bp.route('/register', methods=['POST'])
def register():
    """
    處理註冊邏輯
    - 接收: username, email, password, role
    - 處理: 雜湊密碼，建立 User 物件
    - 輸出: 重導向至登入頁面
    """
    pass

@auth_bp.route('/login', methods=['GET'])
def login_page():
    """顯示登入表單頁面"""
    pass

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    處理登入邏輯
    - 接收: email, password
    - 處理: 驗證帳密，將 user_id 寫入 session
    - 輸出: 重導向至首頁
    """
    pass

@auth_bp.route('/logout', methods=['GET'])
def logout():
    """
    處理登出邏輯
    - 處理: 清除 session 中的 user_id
    - 輸出: 重導向至首頁
    """
    pass
