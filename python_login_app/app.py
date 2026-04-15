from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production'

# ユーザーデータベース（実際の開発では外部DBを使用）
users = {
    'admin': 'password',
    'user': '123456',
    'guest': 'guest'
}

@app.route('/')
def home():
    """ホーム画面 - ログイン状態をチェック"""
    if 'username' in session:
        return redirect(url_for('success'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """ログイン画面"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # 認証チェック
        if username in users and users[username] == password:
            session['username'] = username
            session['login_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return redirect(url_for('success'))
        else:
            flash('ログインできませんでした。ユーザー名またはパスワードが間違っています。', 'error')
    
    return render_template('login.html')

@app.route('/success')
def success():
    """ログイン成功画面"""
    if 'username' not in session:
        return redirect(url_for('login'))
    
    return render_template('success.html', 
                         username=session['username'],
                         login_time=session.get('login_time', ''))

@app.route('/logout')
def logout():
    """ログアウト"""
    session.pop('username', None)
    session.pop('login_time', None)
    flash('ログアウトしました', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    print("=" * 50)
    print("🔐 Pythonログインアプリ")
    print("=" * 50)
    print("🚀 サーバーを起動中...")
    print("📱 ブラウザで以下のURLにアクセスしてください:")
    print("   http://localhost:5000")
    print("=" * 50)
    print("👥 デモアカウント:")
    print("   admin / password")
    print("   user / 123456")
    print("   guest / guest")
    print("=" * 50)
    app.run(host='0.0.0.0', port=5000, debug=True)