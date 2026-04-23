# 系統架構設計 (System Architecture)

這份文件說明了「逢甲大學校園美食資訊平台」的系統架構、選用的技術堆疊、以及專案的資料夾結構。這將作為開發團隊實作時的技術指南。

---

## 1. 技術架構說明

本專案為了快速驗證概念（MVP），選擇了輕量且易於上手的技術堆疊，並採用經典的 MVC（Model-View-Controller）設計模式。

### 選用技術與原因
- **後端框架：Python + Flask**
  - **原因**：Flask 是一個微型 Web 框架，具有極高的靈活性，不會強制規定專案結構。非常適合中小型專案以及快速開發 MVP。
- **模板引擎：Jinja2**
  - **原因**：Jinja2 是 Flask 內建支援的模板引擎，允許在 HTML 中嵌入 Python-like 的語法，由伺服器端渲染（Server-Side Rendering, SSR）後回傳給瀏覽器，不需額外建立前端專案。
- **資料庫：SQLite**
  - **原因**：SQLite 是輕量級的關聯式資料庫，所有資料都儲存在單一檔案中，不需要安裝及維護額外的資料庫伺服器，非常適合初期開發與本地測試。

### MVC 模式說明
專案採用 MVC 模式，各元件負責不同的職責：
- **Model (模型)**：負責與資料庫的互動以及資料結構的定義。通常會使用 ORM (如 SQLAlchemy) 來將 Python 物件映射到資料庫的資料表。
- **View (視圖)**：負責呈現使用者介面。在我們的專案中，是由 `templates/` 資料夾下的 Jinja2 HTML 檔案擔任。
- **Controller (控制器)**：負責接收使用者的 HTTP 請求（Request），調用對應的 Model 處理商業邏輯與資料，最後選擇合適的 View 並將資料傳入以渲染畫面。這部分對應到 Flask 的路由（Routes）。

---

## 2. 專案資料夾結構

專案將採用以下模組化的結構，以便於未來的擴展與維護：

```text
web_app_development2/
├── app/                  ← 應用程式主目錄
│   ├── __init__.py       ← 初始化 Flask 應用程式、設定與擴充套件
│   ├── models/           ← 資料庫模型 (Model)
│   │   ├── user.py       ← 使用者模型 (包含一般使用者與店家)
│   │   ├── restaurant.py ← 店家資訊與菜單模型
│   │   └── order.py      ← 訂單模型
│   ├── routes/           ← Flask 路由 (Controller)
│   │   ├── auth.py       ← 處理註冊、登入與登出
│   │   ├── main.py       ← 前台頁面 (首頁、店家列表、點餐)
│   │   └── admin.py      ← 店家後台管理頁面
│   ├── templates/        ← Jinja2 HTML 模板 (View)
│   │   ├── base.html     ← 所有頁面共用的基礎佈局 (包含 Header/Footer)
│   │   ├── auth/         ← 登入/註冊相關頁面
│   │   ├── main/         ← 店家列表、菜單與購物車頁面
│   │   └── admin/        ← 後台訂單管理與菜單編輯頁面
│   └── static/           ← 靜態資源
│       ├── css/          ← 樣式表
│       ├── js/           ← 客製化 JavaScript (如互動特效)
│       └── images/       ← 網站圖片與店家 Logo
├── instance/             ← 存放機密資料或本地端資料庫
│   └── database.db       ← SQLite 資料庫檔案
├── docs/                 ← 專案相關文件
│   ├── PRD.md            ← 產品需求文件
│   └── ARCHITECTURE.md   ← 系統架構設計 (本文件)
├── requirements.txt      ← Python 專案依賴套件清單
└── app.py                ← 專案啟動入口檔案
```

---

## 3. 元件關係圖

以下是使用者操作時，系統內部的資料流與元件互動流程：

```mermaid
graph TD
    Client[瀏覽器 Browser] -- "1. 發送 HTTP 請求 (例如 GET /restaurants)" --> Controller[Flask Route<br>(Controller)]
    Controller -- "2. 查詢或修改資料" --> Model[Model<br>(Python 類別)]
    Model -- "3. SQL 讀寫" --> DB[(SQLite 資料庫)]
    DB -- "回傳查詢結果" --> Model
    Model -- "回傳 Python 物件" --> Controller
    Controller -- "4. 準備資料並呼叫模板" --> View[Jinja2 Template<br>(View)]
    View -- "5. 渲染為完整的 HTML" --> Controller
    Controller -- "回傳 HTTP 回應" --> Client
```

---

## 4. 關鍵設計決策

1. **採用伺服器端渲染 (SSR)**
   - **決策**：不採用前後端分離架構（如 React/Vue 搭配 API），而是讓 Flask 直接回傳渲染好的 HTML。
   - **原因**：減少專案初期的複雜度，無需管理兩個獨立的專案（前端與後端），能夠最快地打造出可運作的 MVP 並進行驗證。
2. **使用 Blueprints 模組化路由**
   - **決策**：在 `app/routes/` 下將路由分為 `auth`, `main`, `admin` 等不同模組。
   - **原因**：避免將所有的路由邏輯塞在同一個檔案中，提升程式碼的可讀性，也方便未來團隊分工協作。
3. **選擇 SQLite 作為資料庫**
   - **決策**：初期不使用 MySQL 或 PostgreSQL。
   - **原因**：SQLite 零設定成本，直接以檔案形式運作。對於 MVP 的資料量來說已經非常足夠，若未來上線後流量變大，使用 SQLAlchemy 也能很輕易地切換至其他關聯式資料庫。
4. **前端不依賴大型框架**
   - **決策**：前端樣式與互動以 Vanilla CSS 與少量的 Vanilla JavaScript 撰寫，或僅引入基礎的 CSS 框架。
   - **原因**：為了讓專案保持輕量並專注於後端邏輯的實現，同時也能提供夠好的使用者體驗 (動態效果、RWD)。
