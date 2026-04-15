# Python ログインアプリ

## 概要
PythonのFlaskを使用したブラウザベースのログインアプリケーションです。

## 機能
- ✅ ログイン認証
- ✅ ログイン成功時: "ログインしました" 画面表示
- ✅ ログイン失敗時: "ログインできませんでした" メッセージ表示
- ✅ セッション管理
- ✅ ログアウト機能

## 必要な環境
- Python 3.7以上
- Flask 2.0以上

## インストール・起動方法

### 1. 必要なパッケージをインストール
```bash
pip install Flask
```

### 2. アプリケーションを起動
```bash
cd /tmp/python_login_app
python app.py
```

### 3. ブラウザでアクセス
```
http://localhost:5000
```

## デモアカウント
- **管理者**: admin / password
- **ユーザー**: user / 123456
- **ゲスト**: guest / guest

## ファイル構成
```
python_login_app/
├── app.py                 # メインアプリケーション
├── requirements.txt       # 必要なパッケージ
├── templates/
│   ├── login.html        # ログイン画面
│   └── success.html      # ログイン成功画面
└── README.md             # このファイル
```

## 使用方法
1. ブラウザで http://localhost:5000 にアクセス
2. デモアカウントでログイン
3. ログイン成功/失敗の動作を確認
4. ログアウト機能をテスト

## 技術仕様
- **フレームワーク**: Flask
- **テンプレートエンジン**: Jinja2
- **セッション管理**: Flask Session
- **認証方式**: シンプルな辞書ベース認証