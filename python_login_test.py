from flask import Flask, request
import requests
import threading
import time

app = Flask(__name__)

# ユーザーデータベース
users = {'admin': 'password', 'user': '123456', 'guest': 'guest'}

@app.route('/', methods=['GET', 'POST'])
def login():
    """ログイン処理"""
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        
        print(f"ログイン試行: {username} / {password}")
        
        if username in users and users[username] == password:
            print("✅ ログイン成功！")
            return f'''
            <!DOCTYPE html>
            <html lang="ja">
            <head>
                <meta charset="UTF-8">
                <title>ログイン成功</title>
                <style>
                    body {{ font-family: Arial; text-align: center; margin-top: 100px; background: linear-gradient(135deg, #28a745, #20c997); color: white; }}
                    .container {{ background: white; color: #333; max-width: 500px; margin: 0 auto; padding: 3rem; border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.2); }}
                    .success-icon {{ font-size: 5rem; color: #28a745; margin-bottom: 1rem; }}
                    .title {{ font-size: 2.5rem; color: #28a745; margin-bottom: 1rem; font-weight: bold; }}
                    .message {{ font-size: 1.2rem; margin-bottom: 2rem; }}
                    .user-info {{ background: #f8f9fa; padding: 2rem; border-radius: 15px; margin: 2rem 0; border: 2px solid #28a745; }}
                    .user-name {{ font-size: 1.5rem; color: #28a745; font-weight: bold; margin-bottom: 1rem; }}
                    .python-badge {{ background: #3776ab; color: white; padding: 0.5rem 1rem; border-radius: 15px; margin-bottom: 1rem; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="python-badge">🐍 Python Flask</div>
                    <div class="success-icon">✅</div>
                    <h1 class="title">ログインしました</h1>
                    <p class="message">ログインが正常に完了しました</p>
                    
                    <div class="user-info">
                        <div class="user-name">ようこそ、{username}さん！</div>
                        <p>認証状態: <strong style="color: #28a745;">認証済み</strong></p>
                        <p>セッション: <strong style="color: #28a745;">アクティブ</strong></p>
                    </div>
                    
                    <p style="color: #666; margin-top: 2rem;">Powered by Python Flask</p>
                </div>
            </body>
            </html>
            '''
        else:
            print("❌ ログイン失敗")
            return f'''
            <!DOCTYPE html>
            <html lang="ja">
            <head>
                <meta charset="UTF-8">
                <title>ログイン</title>
                <style>
                    body {{ font-family: Arial; background: linear-gradient(135deg, #667eea, #764ba2); min-height: 100vh; display: flex; align-items: center; justify-content: center; }}
                    .container {{ background: white; padding: 2.5rem; border-radius: 15px; box-shadow: 0 15px 35px rgba(0,0,0,0.2); max-width: 420px; text-align: center; }}
                    .logo {{ font-size: 2.5rem; color: #667eea; margin-bottom: 1rem; font-weight: bold; }}
                    .error {{ background: #f8d7da; color: #721c24; padding: 1rem; border-radius: 8px; margin-bottom: 1.5rem; font-weight: bold; }}
                    input {{ width: 100%; padding: 1rem; margin: 0.5rem 0; border: 2px solid #e1e5e9; border-radius: 10px; font-size: 1rem; }}
                    button {{ width: 100%; padding: 1rem; background: linear-gradient(135deg, #667eea, #764ba2); color: white; border: none; border-radius: 10px; font-size: 1.1rem; cursor: pointer; margin-top: 1rem; }}
                    .demo-info {{ background: #e3f2fd; padding: 1.5rem; border-radius: 10px; margin-bottom: 1.5rem; font-size: 0.9rem; color: #1976d2; text-align: left; }}
                    .python-badge {{ background: #3776ab; color: white; padding: 0.25rem 0.75rem; border-radius: 15px; font-size: 0.8rem; margin-bottom: 1rem; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="python-badge">🐍 Python Flask</div>
                    <div class="logo">🔐</div>
                    <h1 style="color: #333; margin-bottom: 2rem;">ログイン</h1>
                    
                    <div class="error">
                        ❌ ログインできませんでした<br>
                        ユーザー名またはパスワードが間違っています
                    </div>
                    
                    <div class="demo-info">
                        <h4 style="margin-bottom: 0.75rem;">📋 デモアカウント</h4>
                        <div><strong>管理者:</strong> admin / password</div>
                        <div><strong>ユーザー:</strong> user / 123456</div>
                        <div><strong>ゲスト:</strong> guest / guest</div>
                    </div>
                    
                    <form method="POST">
                        <input type="text" name="username" placeholder="ユーザー名" required value="{username}">
                        <input type="password" name="password" placeholder="パスワード" required>
                        <button type="submit">ログイン</button>
                    </form>
                    
                    <p style="color: #666; font-size: 0.9rem; margin-top: 1rem;">Powered by Python Flask</p>
                </div>
            </body>
            </html>
            '''
    
    # 初回アクセス時のログイン画面
    return '''
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>ログイン</title>
        <style>
            body { font-family: Arial; background: linear-gradient(135deg, #667eea, #764ba2); min-height: 100vh; display: flex; align-items: center; justify-content: center; }
            .container { background: white; padding: 2.5rem; border-radius: 15px; box-shadow: 0 15px 35px rgba(0,0,0,0.2); max-width: 420px; text-align: center; }
            .logo { font-size: 2.5rem; color: #667eea; margin-bottom: 1rem; font-weight: bold; }
            input { width: 100%; padding: 1rem; margin: 0.5rem 0; border: 2px solid #e1e5e9; border-radius: 10px; font-size: 1rem; }
            button { width: 100%; padding: 1rem; background: linear-gradient(135deg, #667eea, #764ba2); color: white; border: none; border-radius: 10px; font-size: 1.1rem; cursor: pointer; margin-top: 1rem; }
            .demo-info { background: #e3f2fd; padding: 1.5rem; border-radius: 10px; margin-bottom: 1.5rem; font-size: 0.9rem; color: #1976d2; text-align: left; }
            .python-badge { background: #3776ab; color: white; padding: 0.25rem 0.75rem; border-radius: 15px; font-size: 0.8rem; margin-bottom: 1rem; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="python-badge">🐍 Python Flask</div>
            <div class="logo">🔐</div>
            <h1 style="color: #333; margin-bottom: 0.5rem;">ログイン</h1>
            <p style="color: #666; margin-bottom: 2rem;">Pythonログインアプリ</p>
            
            <div class="demo-info">
                <h4 style="margin-bottom: 0.75rem;">📋 デモアカウント</h4>
                <div><strong>管理者:</strong> admin / password</div>
                <div><strong>ユーザー:</strong> user / 123456</div>
                <div><strong>ゲスト:</strong> guest / guest</div>
            </div>
            
            <form method="POST">
                <input type="text" name="username" placeholder="ユーザー名" required>
                <input type="password" name="password" placeholder="パスワード" required>
                <button type="submit">ログイン</button>
            </form>
            
            <p style="color: #666; font-size: 0.9rem; margin-top: 1rem;">Powered by Python Flask</p>
        </div>
    </body>
    </html>
    '''

def test_login_app():
    """ログインアプリのテスト"""
    time.sleep(2)
    try:
        print("\n=== Python ログインアプリ テスト ===")
        
        # 1. ログイン画面の表示テスト
        print("1. ログイン画面をテスト中...")
        response = requests.get('http://localhost:5001/')
        if "ログイン" in response.text and "デモアカウント" in response.text:
            print("✅ ログイン画面: 正常に表示")
        else:
            print("❌ ログイン画面: エラー")
        
        # 2. 正しいログインのテスト
        print("2. 正しいログイン情報でテスト...")
        response = requests.post('http://localhost:5001/', data={'username': 'admin', 'password': 'password'})
        if "ログインしました" in response.text and "ようこそ、adminさん" in response.text:
            print("✅ ログイン成功: 正常に表示")
        else:
            print("❌ ログイン成功: エラー")
        
        # 3. 間違ったログインのテスト
        print("3. 間違ったログイン情報でテスト...")
        response = requests.post('http://localhost:5001/', data={'username': 'admin', 'password': 'wrong'})
        if "ログインできませんでした" in response.text:
            print("✅ ログイン失敗: 正常にエラー表示")
        else:
            print("❌ ログイン失敗: エラー処理に問題")
        
        # 4. 複数アカウントのテスト
        print("4. 複数アカウントをテスト...")
        accounts = [('user', '123456'), ('guest', 'guest')]
        for username, password in accounts:
            response = requests.post('http://localhost:5001/', data={'username': username, 'password': password})
            if "ログインしました" in response.text:
                print(f"✅ {username}アカウント: ログイン成功")
            else:
                print(f"❌ {username}アカウント: ログイン失敗")
        
        print("\n=== テスト完了 ===")
        print("Pythonログインアプリは正常に動作しています！")
        
    except Exception as e:
        print(f"❌ テストエラー: {e}")

if __name__ == '__main__':
    print("=" * 60)
    print("🐍 Python Flask ログインアプリ")
    print("=" * 60)
    print("🚀 サーバーを起動中... (ポート5001)")
    print("📱 ローカル環境では http://localhost:5001 でアクセス可能")
    print("=" * 60)
    print("👥 デモアカウント:")
    print("   admin / password")
    print("   user / 123456") 
    print("   guest / guest")
    print("=" * 60)
    
    # テストを別スレッドで実行
    test_thread = threading.Thread(target=test_login_app)
    test_thread.daemon = True
    test_thread.start()
    
    # Flaskアプリを起動
    app.run(host='127.0.0.1', port=5001, debug=False)