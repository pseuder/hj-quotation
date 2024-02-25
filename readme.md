# 報價單生成系統

## 安裝

- python 環境  
  ` $ pip install -r requirements.txt`

- 建立資料庫  
  `$ python manage.py migrate`

- 將csv中的資料寫入剛建好的資料庫  
  `$ python write_model_from_csv.py`

## 執行

  `$ python manage.py runserver`  
  預設登入帳密為admin/admin

## 操作

- 主要介面
  1. 根據欄位輸入資料
  1. 點擊下一步或點擊上方標籤切換輸入頁面
  1. 完成畫面可於空格中輸入剩餘資訊, 點擊客戶簽名處開啟手寫板
  1. 點擊下載 PDF 保存影像

## 專案描述

- 前端: vue2
- UI 組件: Element UI
- Router: vue-router
- HTML 轉換 PDF: vue-html2pdf
- 手繪版簽名: vue-esign
- 後端: Django, Python
- 資料庫: sqlite

## 開發

- node_modules  
  `$ npm install `

## 部屬pythonanywhere

- File:  
  將整包專案置於使用者目錄底下  
  home/username/hj-quotation


- Console:  
  ` $ pip install -r requirements.txt`

  `$ python manage.py migrate`

  `$ python write_model_from_csv.py`

- Web  
  - 根據實際使用者名稱與專案名稱修改wsgi.py後貼到`WSGI configuration file`中

  - 設置Static files:
    URL: /static/
    Directory: /home/apex890520/hj-quotation/dist/static

  - 點擊Reload