from flask import Flask, request
import requests
import threading
import time

app = Flask(__name__)

# ユーザーデータベース
users = {'admin': 'password', 'user': '123456', 'guest': 'guest'}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        
        print(f"ログイン試行: {username} / {password}")
        
        if username in users and users[username] == password:
            print("✅ ログイン成功")
            return '''
            <!DOCTYPE html>
            <html lang="ja">
            <head>
                <meta charset="UTF-8">
                <title>ログイン成功</title>
                <style>
                    body { font-family: Arial; text-align: center; margin-top: 150px; background: #e8f5e9; }
                    .message { font-size: 3rem; color: #2e7d32; font-weight: bold; margin-bottom: 2rem; }
                    .container { background: white; max-width: 600px; margin: 0 auto; padding: 3rem; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
                    .icon { font-size: 5rem; margin-bottom: 1rem; }
                    .user { font-size: 1.5rem; color: #333; margin-top: 2rem; }
                    .back-btn { background: #2e7d32; color: white; padding: 1rem 2rem; border: none; border-radius: 8px; font-size: 1.1rem; cursor: pointer; margin-top: 2rem; }
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="icon">✅</div>
                    <div class="message">ログインに成功しました</div>
                    <div class="user">ようこそ、''' + username + '''さん！</div>
                    <button class="back-btn" onclick="location.href='/'">戻る</button>
                </div>
            </body>
            </html>
            '''
        else:
            print("❌ ログイン失敗")
            return '''
            <!DOCTYPE html>
            <html lang="ja">
            <head>
                <meta charset="UTF-8">
                <title>ログイン失敗</title>
                <style>
                    body { font-family: Arial; text-align: center; margin-top: 150px; background: #ffebee; }
                    .message { font-size: 3rem; color: #c62828; font-weight: bold; margin-bottom: 2rem; }
                    .container { background: white; max-width: 600px; margin: 0 auto; padding: 3rem; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
                    .icon { font-size: 5rem; margin-bottom: 1rem; }
                    .detail { font-size: 1.2rem; color: #666; margin-top: 1rem; }
                    .back-btn { background: #c62828; color: white; padding: 1rem 2rem; border: none; border-radius: 8px; font-size: 1.1rem; cursor: pointer; margin-top: 2rem; }
                    .demo { background: #f5f5f5; padding: 1rem; border-radius: 8px; margin-top: 2rem; font-size: 0.9rem; }
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="icon">❌</div>
                    <div class="message">ログインに失敗しました</div>
                    <div class="detail">ユーザー名またはパスワードが間違っています</div>
                    <div class="demo">
                        <strong>デモアカウント:</strong><br>
                        admin / password<br>
                        user / 123456<br>
                        guest / guest
                    </div>
                    <button class="back-btn" onclick="location.href='/'">再試行</button>
                </div>
            </body>
            </html>
            '''
    
    # ログイン画面
    return '''
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>ログイン</title>
        <style>
            body { font-family: Arial; background: #f0f2f5; min-height: 100vh; display: flex; align-items: center; justify-content: center; }
            .container { background: white; padding: 3rem; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); max-width: 400px; width: 100%; }
            .title { font-size: 2rem; color: #333; margin-bottom: 2rem; text-align: center; }
            input { width: 100%; padding: 1rem; margin: 0.5rem 0; border: 2px solid #ddd; border-radius: 8px; font-size: 1rem; }
            button { width: 100%; padding: 1rem; background: #1976d2; color: white; border: none; border-radius: 8px; font-size: 1.1rem; cursor: pointer; margin-top: 1rem; }
            button:hover { background: #1565c0; }
            .demo { background: #e3f2fd; padding: 1rem; border-radius: 8px; margin-bottom: 1rem; font-size: 0.9rem; color: #1976d2; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="title">🔐 ログイン</h1>
            
            <div class="demo">
                <strong>デモアカウント:</strong><br>
                admin / password<br>
                user / 123456<br>
                guest / guest
            </div>
            
            <form method="POST">
                <input type="text" name="username" placeholder="ユーザー名" required>
                <input type="password" name="password" placeholder="パスワード" required>
                <button type="submit">ログイン</button>
            </form>
        </div>
    </body>
    </html>
    '''

def test_app():
    time.sleep(2)
    try:
        print("\n=== ログイン機能テスト ===")
        
        # 成功テスト
        response = requests.post('http://localhost:5002/', data={'username': 'admin', 'password': 'password'})
        if "ログインに成功しました" in response.text:
            print("✅ 成功メッセージ: 正常表示")
        
        # 失敗テスト
        response = requests.post('http://localhost:5002/', data={'username': 'admin', 'password': 'wrong'})
        if "ログインに失敗しました" in response.text:
            print("✅ 失敗メッセージ: 正常表示")
        
        print("=== テスト完了 ===")
        
    except Exception as e:
        print(f"テストエラー: {e}")

if __name__ == '__main__':
    print("🔐 ログインアプリ起動中...")
    print("ポート: 5002")
    
    test_thread = threading.Thread(target=test_app)
    test_thread.daemon = True
    test_thread.start()
    
    app.run(host='127.0.0.1', port=5002, debug=False)