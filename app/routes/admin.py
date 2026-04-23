from flask import Blueprint, render_template, request, redirect, url_for, flash

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/', methods=['GET'])
def dashboard():
    """
    後台儀表板首頁
    - 處理: 驗證店家身分，計算今日營業額或未完成訂單數量
    - 輸出: 渲染 admin/dashboard.html
    """
    pass

@admin_bp.route('/orders', methods=['GET'])
def manage_orders():
    """
    店家訂單管理列表
    - 處理: 取出該店家收到的所有訂單 (依照時間與狀態排序)
    - 輸出: 渲染 admin/orders.html
    """
    pass

@admin_bp.route('/orders/<int:id>/status', methods=['POST'])
def update_order_status(id):
    """
    更新訂單狀態 (接單、可取餐等)
    - 接收: status (from form)
    - 處理: 更新 Order.status
    - 輸出: 重導向至 /admin/orders
    """
    pass

@admin_bp.route('/menu', methods=['GET'])
def manage_menu():
    """
    店家菜單管理列表
    - 處理: 取出該店家的所有 MenuItem
    - 輸出: 渲染 admin/menu.html
    """
    pass

@admin_bp.route('/menu/new', methods=['POST'])
def add_menu_item():
    """
    新增菜單品項
    - 接收: name, price, description
    - 處理: 建立新 MenuItem
    - 輸出: 重導向至 /admin/menu
    """
    pass

@admin_bp.route('/menu/<int:id>/update', methods=['POST'])
def update_menu_item(id):
    """
    編輯菜單品項 (如更新價格或上下架)
    - 接收: price, is_available 等
    - 處理: 更新對應的 MenuItem
    - 輸出: 重導向至 /admin/menu
    """
    pass
