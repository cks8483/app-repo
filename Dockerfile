# 이미지 용량을 줄이기 위해 slim 태그 사용 권장 (python:3.9도 가능)
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 1. requirements 복사 및 설치 (캐시 효율화)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. 소스 코드 전체 복사
COPY . .

# 3. 환경 변수 설정 (Python이 src 모듈을 잘 찾도록)
ENV PYTHONPATH=/app

# 4. 기본 실행 명령: 웹 서버 (Gunicorn)
# -w 4: 워커 프로세스 4개
# src.main:app -> src/main.py 파일의 app 객체 실행
CMD ["gunicorn", "-w", "4", "src.main:app", "--bind", "0.0.0.0:5000"]