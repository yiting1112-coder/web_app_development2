# 路由設計文件 (Routes Design)

這份文件定義了「逢甲大學校園美食資訊平台」的所有後端路由、HTTP 方法以及對應的 Jinja2 模板。專案採用 Flask Blueprint 來模組化路由，分為 `auth` (身分驗證)、`main` (前台功能)、`admin` (店家後台管理) 三大區塊。

## 1. 路由總覽表格

### Auth 模組 (前綴: `/auth`)
| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| :--- | :--- | :--- | :--- | :--- |
| 註冊頁面 | GET | `/auth/register` | `auth/register.html` | 顯示註冊表單 |
| 處理註冊 | POST | `/auth/register` | — | 接收表單並建立 User，重導向至登入 |
| 登入頁面 | GET | `/auth/login` | `auth/login.html` | 顯示登入表單 |
| 處理登入 | POST | `/auth/login` | — | 驗證帳密，寫入 Session，重導向至首頁 |
| 處理登出 | GET | `/auth/logout` | — | 清除 Session，重導向至首頁 |

### Main 模組 (前綴: 無)
| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| :--- | :--- | :--- | :--- | :--- |
| 首頁 (店家列表) | GET | `/` | `main/index.html` | 顯示所有店家列表與搜尋列 |
| 店家專頁與菜單 | GET | `/restaurant/<int:id>` | `main/restaurant_detail.html`| 顯示單一店家資訊與其 MenuItems |
| 結帳頁面 | GET | `/checkout` | `main/checkout.html` | 顯示購物車內容與選擇取餐時間 |
| 送出訂單 | POST | `/checkout` | — | 建立 Order 與 OrderItem，重導向訂單狀態 |
| 歷史訂單列表 | GET | `/orders` | `main/orders.html` | 顯示登入使用者的所有訂單 |
| 單筆訂單狀態 | GET | `/order/<int:id>` | `main/order_status.html` | 顯示單筆訂單詳細資訊與目前狀態 |

### Admin 模組 (前綴: `/admin`)
| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| :--- | :--- | :--- | :--- | :--- |
| 後台儀表板 | GET | `/admin/` | `admin/dashboard.html` | 顯示營業概況與今日未結訂單 |
| 訂單管理頁面 | GET | `/admin/orders` | `admin/orders.html` | 列表顯示店家所有訂單 |
| 更新訂單狀態 | POST | `/admin/orders/<int:id>/status`| — | 接收狀態變更，更新後重導向回列表 |
| 菜單管理頁面 | GET | `/admin/menu` | `admin/menu.html` | 列表顯示店家所有菜單品項 |
| 新增菜單品項 | POST | `/admin/menu/new` | — | 接收表單新增 MenuItem，重導向回列表 |
| 編輯菜單品項 | POST | `/admin/menu/<int:id>/update`| — | 接收表單更新價格/上下架狀態 |

---

## 2. 每個路由的詳細說明

### Main: 送出訂單 (`POST /checkout`)
- **輸入**：表單內的餐點 ID 清單、數量、預計取餐時間 (pickup_time)。
- **處理邏輯**：
  1. 檢查使用者是否登入 (`@login_required`)。
  2. 計算總金額 (`total_price`)。
  3. 呼叫 `Order.create()` 建立主檔。
  4. 迴圈呼叫 `OrderItem.create()` 建立明細。
- **輸出**：`redirect(url_for('main.order_status', id=new_order.id))`。
- **錯誤處理**：如果必填欄位缺失，使用 `flash()` 提示並導回 `/checkout` 頁面。

### Admin: 更新訂單狀態 (`POST /admin/orders/<id>/status`)
- **輸入**：隱藏表單傳遞的 `status` 值 (例如 'accepted', 'ready')。
- **處理邏輯**：
  1. 檢查是否為店家登入且該訂單屬於該店家。
  2. 呼叫 `Order.get_by_id(id)` 取出訂單。
  3. 呼叫 `order.update_status(status)`。
- **輸出**：`redirect(url_for('admin.orders'))`。
- **錯誤處理**：若非該店家訂單，回傳 403 Forbidden。

---

## 3. Jinja2 模板清單

所有的 HTML 檔案都將繼承自 `base.html`：
- `templates/base.html` (包含 Navbar, Flash 訊息顯示區, Footer)

**Auth 相關：**
- `templates/auth/login.html`
- `templates/auth/register.html`

**Main 相關 (前台)：**
- `templates/main/index.html`
- `templates/main/restaurant_detail.html`
- `templates/main/checkout.html`
- `templates/main/orders.html`
- `templates/main/order_status.html`

**Admin 相關 (後台)：**
- `templates/admin/dashboard.html`
- `templates/admin/orders.html`
- `templates/admin/menu.html`
