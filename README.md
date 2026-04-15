# SimpleTask - Backlog風タスク管理システム

![SimpleTask](https://img.shields.io/badge/SimpleTask-v1.0-blue)
![Python](https://img.shields.io/badge/Python-3.7+-green)
![Flask](https://img.shields.io/badge/Flask-2.0+-red)

## 概要
SimpleTaskは、Backlogのようなタスク管理機能を持つWebアプリケーションです。

## 🎯 主な機能
- ✅ **かんばんビュー**: 未着手/進行中/完了の3列表示
- ✅ **タスク作成**: 新しいタスクの起票
- ✅ **タスク一覧**: 全タスクをテーブル形式で表示
- ✅ **子タスク管理**: 各タスクに最大5個の子タスクを追加
- ✅ **ステータス変更**: ドロップダウンでタスクステータスを変更
- ✅ **タスク削除**: 不要なタスクの削除
- ✅ **レスポンシブデザイン**: PC・モバイル対応

## 🚀 クイックスタート

### 必要な環境
- Python 3.7以上
- Flask 2.0以上

### インストール・起動
```bash
# リポジトリをクローン
git clone https://github.com/ユーザー名/simpletask.git
cd simpletask

# 必要なパッケージをインストール
pip install Flask

# アプリケーションを起動
python app.py
```

### ブラウザでアクセス
```
http://localhost:5000
```

## 📱 スクリーンショット

### かんばんビュー
![Kanban View](https://via.placeholder.com/800x400/667eea/ffffff?text=Kanban+View)

### タスク作成
![Create Task](https://via.placeholder.com/800x400/28a745/ffffff?text=Create+Task)

## 🛠️ 技術スタック
- **フロントエンド**: HTML5, CSS3, JavaScript
- **バックエンド**: Python Flask
- **データ保存**: JSON ファイル
- **デザイン**: レスポンシブデザイン

## 📂 ファイル構成
```
simpletask/
├── app.py                 # メインアプリケーション
├── tasks.json            # タスクデータ（自動生成）
├── templates/
│   ├── kanban.html       # かんばんビュー
│   ├── create.html       # タスク作成画面
│   ├── list.html         # タスク一覧画面
│   └── detail.html       # タスク詳細画面
└── README.md             # このファイル
```

## 🔧 開発者向け情報

### API エンドポイント
- `GET /` - かんばんビュー
- `GET /list` - タスク一覧
- `GET /create` - タスク作成画面
- `POST /create` - タスク作成処理
- `GET /task/<id>` - タスク詳細
- `POST /task/<id>/subtask` - 子タスク追加
- `POST /update_status` - ステータス更新
- `POST /delete_task/<id>` - タスク削除

### データ構造
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "タスクタイトル",
      "description": "タスクの説明",
      "status": "todo|progress|done",
      "created_at": "2024-01-01 12:00",
      "subtasks": [
        {
          "id": 1,
          "title": "子タスクタイトル",
          "completed": false
        }
      ]
    }
  ],
  "next_id": 2
}
```

## 🤝 コントリビューション
1. このリポジトリをフォーク
2. 機能ブランチを作成 (`git checkout -b feature/AmazingFeature`)
3. 変更をコミット (`git commit -m 'Add some AmazingFeature'`)
4. ブランチにプッシュ (`git push origin feature/AmazingFeature`)
5. プルリクエストを作成

## 📄 ライセンス
MIT License

## 👨‍💻 作成者
SimpleTask Development Team

---
⭐ このプロジェクトが役に立った場合は、スターをつけてください！
