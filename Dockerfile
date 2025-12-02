FROM python:3.9

# 작업 디렉토리
WORKDIR /app

# requirements 먼저 복사 → layer 최적화
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 전체 복사
COPY . .

# Gunicorn 실행 (src/main.py 안의 app 객체)
CMD ["gunicorn", "src.main:app", "--bind", "0.0.0.0:5000"]
