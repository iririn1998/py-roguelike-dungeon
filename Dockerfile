# Python 3.12のslim版を使用（軽量）
FROM python:3.12-slim

# 作業ディレクトリを設定
WORKDIR /app

# アプリケーションのソースコードをコピー
COPY . .

# アプリケーションを実行
CMD ["python", "main.py"]

