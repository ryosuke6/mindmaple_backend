# MindMaple バックエンド

MindMapleのバックエンドAPIは、FastAPIを使用して構築されたタスク管理アプリケーションです。

## 機能

- ユーザー認証
- タスク管理（作成、読み取り、更新、削除）
- イベント管理

## 技術スタック

- FastAPI
- SQLAlchemy
- Pydantic
- SQLite（開発用）

## セットアップ

1. リポジトリをクローンします：

   ```bash
   git clone https://github.com/yourusername/mindmaple.git
   cd mindmaple/mindmaple_back
   ```

2. 仮想環境を作成し、アクティベートします：

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linuxの場合
   venv\Scripts\activate  # Windowsの場合
   ```

3. 依存関係をインストールします：

   ```bash
   pip install -r requirements.txt
   ```

4. 環境変数を設定します：

   `.env`ファイルを作成し、必要な環境変数を設定します。

5. アプリケーションを実行します：

   ```bash
   uvicorn app.main:app --reload
   ```

   アプリケーションは`http://localhost:8000`で実行されます。

## API ドキュメント

FastAPIは自動的にAPIドキュメントを生成します。以下のURLでアクセスできます：

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## テスト

テストを実行するには：

```
pytest
```
