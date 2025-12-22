from flask import Flask, render_template, request, redirect, url_for
import html
import datetime

app = Flask(__name__)

# 模擬資料庫，用來儲存所有留言
# 格式: [{'content': '...', 'mode': 'secure', 'time': '...'}]
COMMENTS_DB = []

@app.route('/', methods=['GET', 'POST'])
def index():
    # 預設模式為危險 (danger)
    current_mode = 'danger'

    if request.method == 'POST':
        # 1. 獲取使用者輸入
        user_input = request.form.get('content', '')
        mode = request.form.get('mode', 'danger')
        current_mode = mode # 記住使用者的選擇，回傳頁面時保持狀態

        if user_input:
            # 2. 核心邏輯：防禦 vs 不防禦
            if mode == 'secure':
                # 【安全模式】
                # 使用 Python 內建的 html.escape()
                # 它會把 <script> 變成 &lt;script&gt;
                # 這樣瀏覽器顯示時，會看到程式碼文字，但不會執行它
                processed_content = html.escape(user_input)
            else:
                # 【危險模式】
                # 完全不做任何處理，原樣儲存
                # 這就是漏洞所在！
                processed_content = user_input

            # 3. 存入模擬資料庫
            new_comment = {
                'content': processed_content,
                'mode': mode,
                'time': datetime.datetime.now().strftime("%H:%M:%S")
            }
            # 把最新的留言放在最上面
            COMMENTS_DB.insert(0, new_comment)

    return render_template('index.html', comments=COMMENTS_DB, mode=current_mode)

@app.route('/clear', methods=['POST'])
def clear_db():
    # 清空資料庫的路由
    COMMENTS_DB.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)