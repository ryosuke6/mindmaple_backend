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
- PostgreSQL

## セットアップと実行

### Dockerを使用した実行（推奨）

1. Dockerとdocker-composeをインストールします。
   - [Docker installation guide](https://docs.docker.com/get-docker/)
   - [Docker Compose installation guide](https://docs.docker.com/compose/install/)

2. プロジェクトのルートディレクトリで以下のコマンドを実行します：

   ```bash
   docker-compose up --build
   ```

   これにより、以下の処理が行われます：
   - Dockerイメージのビルド
   - アプリケーションコンテナの起動
   - PostgreSQLデータベースコンテナの起動

3. アプリケーションは`http://localhost:8000`でアクセス可能になります。

4. 開発中は、ソースコードの変更が自動的に反映されます。

5. アプリケーションを停止するには：

   ```bash
   docker-compose down
   ```

### ローカル環境での実行

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

4. PostgreSQLをインストールし、データベースを作成します。

5. `.env`ファイルを作成し、以下の環境変数を設定します：

   ```bash
   DATABASE_URL=postgresql://username:password@localhost:5432/mindmaple_db
   ```

6. アプリケーションを実行します：

   ```bash
   uvicorn app.main:app --reload
   ```

## データベース

このプロジェクトはPostgreSQLを使用しています。

- Dockerを使用する場合：データベースは自動的にセットアップされます。
- ローカル開発の場合：PostgreSQLをインストールし、`.env`ファイルで接続情報を設定してください。

データベース接続に問題がある場合：
1. PostgreSQLサービスが実行中であることを確認してください。
2. `.env`ファイルの接続情報が正しいことを確認してください。
3. ファイアウォールがポート5432を許可していることを確認してください。

## API ドキュメント

FastAPIは自動的にAPIドキュメントを生成します：

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## テスト

テストを実行するには：

```
pytest
```

## Dockerを使用した実行

Dockerを使用してアプリケーションを実行するには：

1. Dockerとdocker-composeがインストールされていることを確認してください。

2. プロジェクトのルートディレクトリで以下のコマンドを実行します：

   ```bash
   docker-compose up --build
   ```

   これにより、Dockerイメージがビルドされ、コンテナが起動します。

3. アプリケーションは`http://localhost:8000`でアクセス可能になります。

4. 開発中は、ソースコードの変更が自動的に反映されます。

5. アプリケーションを停止するには、別のターミナルウィンドウで以下のコマンドを実行します：

   ```bash
   docker-compose down
   ```

## データベース

このプロジェクトはPostgreSQLを使用しています。Dockerを使用して実行する場合、データベースは自動的にセットアップされます。

ローカルで開発する場合は、`.env`ファイルに以下の環境変数を設定してください：

```
DATABASE

```
## 環境変数の設定

1. プロジェクトのルートディレクトリに`.env`ファイルを作成します。
2. 以下の環境変数を設定してください：

   ```bash
   DATABASE_URL=postgresql://mindmaple:mindmaplepassword@mindmaple_db:5432/mindmaple_db
   POSTGRES_USER=mindmaple
   POSTGRES_PASSWORD=mindmaplepassword
   POSTGRES_DB=mindmaple_db
   ```

   注意: 本番環境では、より安全なパスワードを使用してください。

3. Docker使用時は、`docker-compose.yml`ファイルで環境変数が自動的に読み込まれます。
4. ローカル開発時は、`.env`ファイルが自動的に読み込まれます。
