# ビルドステージ
FROM python:3.9-slim-buster

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係ファイルをコピー
COPY requirements.txt .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install uvicorn

# アプリケーションのソースコードをコピー
COPY ./app /app/app

# ポート8000を公開
EXPOSE 8000

# アプリケーションを実行
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
