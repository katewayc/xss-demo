from flask import Flask, render_template, request, redirect, url_for, session # 引入 session
import html
import datetime
import os

app = Flask(__name__)

# 必須設定 Secret Key 才能使用 session，隨便設定一個字串即可
app.secret_key = os.urandom(24) 

@app.route('/', methods=['GET', 'POST'])
def index():
    # 從 session 取得該使用者的留言列表，如果沒有則建立空的
    if 'my_comments' not in session:
        session['my_comments'] = []
    
    current_mode = 'danger'

    if request.method == 'POST':
        user_input = request.form.get('content', '')
        mode = request.form.get('mode', 'danger')
        current_mode = mode

        if user_input:
            if mode == 'secure':
                processed_content = html.escape(user_input)
            else:
                processed_content = user_input

            new_comment = {
                'content': processed_content,
                'mode': mode,
                'time': datetime.datetime.now().strftime("%H:%M:%S")
            }
            
            # 更新 session 中的列表 (注意：Flask session 修改 list 需要重新指定)
            temp_list = session['my_comments']
            temp_list.insert(0, new_comment)
            session['my_comments'] = temp_list

    return render_template('index.html', comments=session['my_comments'], mode=current_mode)

@app.route('/clear', methods=['POST'])
def clear_db():
    # 只清空該使用者的 session 資料
    session.pop('my_comments', None)
    return redirect(url_for('index'))
