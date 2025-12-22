# XSS Vulnerability & Mitigation Demo (XSS 攻防演練實驗室)

本專案演示了 Web 應用程式中常見的 XSS (Cross-Site Scripting) 攻擊原理，以及如何使用 Python 後端進行防禦。

## 專案功能

- **v1.0**: 實作反射型 XSS 攻擊 (Reflected XSS)。
- **攻擊模式 (Vulnerable)**: 模擬未經過濾的後端，允許執行 `<script>` 注入。
- **防禦模式 (Secure)**: 使用 Python `html.escape()` 進行字元過濾 (Sanitization)。
- **15 種 Payload**: 內建多種攻擊腳本供測試 (彈窗、更換背景、讀取 Cookie 等)。

## 技術架構

- **Backend**: Python 3.10, Flask
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Deployment**: PythonAnywhere

## 如何執行 (Local Development)

1. 安裝套件：
   ```bash
   pip install -r requirements.txt
   ```

2. 執行程式：
   ```bash
   python app.py
   ```

3. 開啟瀏覽器訪問 `http://127.0.0.1:5000`