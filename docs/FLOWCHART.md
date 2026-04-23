# 流程圖設計 (Flowchart)

這份文件描述了「逢甲大學校園美食資訊平台」的使用者操作路徑（User Flow）、系統資料互動的序列圖（Sequence Diagram）以及各功能的 URL 路由對照表。這將幫助開發團隊在實作路由前，釐清頁面間的跳轉關係與資料流向。

---

## 1. 使用者流程圖（User Flow）

此流程圖展示了學生/老師（一般使用者）與店家管理者在系統中的主要操作路徑。

```mermaid
flowchart LR
    Start([進入網站]) --> Home[首頁 / 店家列表]
    
    Home --> Action{操作選擇}
    Action -->|註冊 / 登入| Auth[身分驗證頁面]
    Action -->|選擇店家| Restaurant[店家專頁 / 數位菜單]
    
    Auth -->|成功登入| Home
    
    %% 一般使用者點餐流程
    Restaurant -->|選擇餐點| Cart[購物車]
    Cart -->|送出訂單| Checkout[結帳與選擇取餐時間]
    Checkout --> OrderStatus[訂單狀態查詢頁]
    
    %% 店家管理流程
    Home -->|若是店家登入| Admin[後台管理儀表板]
    Admin -->|查看訂單| AdminOrders[接單與更新狀態]
    Admin -->|編輯菜單| AdminMenu[菜單上下架]
    
    %% 狀態更新回饋
    AdminOrders -.->|狀態更新通知| OrderStatus
```

---

## 2. 系統序列圖（Sequence Diagram）

以下序列圖以核心的**「使用者送出線上訂單」**流程為例，展示前端瀏覽器、後端 Flask、資料模型與 SQLite 資料庫之間的完整互動過程。

```mermaid
sequenceDiagram
    actor User as 學生/老師
    participant Browser as 瀏覽器
    participant Route as Flask (Controller)
    participant Model as Model (Order)
    participant DB as SQLite 資料庫

    User->>Browser: 在購物車點擊「確認送出訂單」
    Browser->>Route: POST /checkout (包含餐點與取餐時間)
    
    Route->>Route: 驗證登入狀態與資料完整性
    
    Route->>Model: 建立新訂單物件 (Order)
    Model->>DB: INSERT INTO orders (寫入資料庫)
    DB-->>Model: 寫入成功 (回傳新紀錄)
    Model-->>Route: 回傳新訂單 ID
    
    Route-->>Browser: HTTP 302 重導向至訂單狀態頁
    Browser->>Route: GET /order/<id>
    Route->>Model: 查詢訂單資訊
    Model->>DB: SELECT * FROM orders WHERE id = <id>
    DB-->>Model: 回傳資料
    Model-->>Route: 訂單物件
    Route-->>Browser: 渲染 order_status.html (訂單已建立)
    Browser->>User: 顯示「訂單已建立，等待店家接單」
```

---

## 3. 功能清單對照表

開發路由 (Routes) 時，請參考以下對照表建立對應的 URL 與 HTTP 方法：

| 功能模組 | 詳細功能描述 | 建議 URL 路徑 | HTTP 方法 |
| :--- | :--- | :--- | :--- |
| **身分驗證** | 使用者註冊頁面與送出 | `/register` | GET, POST |
| | 使用者登入頁面與送出 | `/login` | GET, POST |
| | 使用者登出 | `/logout` | GET |
| **前台探索** | 首頁 (顯示所有店家列表與搜尋) | `/` 或 `/restaurants` | GET |
| | 檢視單一店家詳細資訊與數位菜單 | `/restaurant/<id>` | GET |
| **線上訂餐** | 檢視購物車與送出結帳 | `/checkout` | GET, POST |
| | 查看使用者的歷史與進行中訂單 | `/orders` | GET |
| | 查看單一訂單的最新狀態 | `/order/<id>` | GET |
| **店家後台** | 後台儀表板首頁 | `/admin` | GET |
| | 店家查看並更新顧客訂單狀態 | `/admin/orders` | GET, POST |
| | 店家新增、修改或下架菜單品項 | `/admin/menu` | GET, POST |
