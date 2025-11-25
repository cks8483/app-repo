# 1. 베이스 이미지 선택 (가볍고 안정적인 slim 버전 추천)
FROM python:3.9-slim

# 2. 작업 디렉터리 설정
WORKDIR /app

# 3. requirements.txt를 먼저 복사하여 의존성 설치 (레이어 캐싱 활용)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 소스 코드 복사
COPY src/ .

# 5. 컨테이너가 5000번 포트를 사용함을 명시
EXPOSE 5000

# 6. 컨테이너 실행 명령어 (개발 서버 대신 gunicorn 사용)
#    -w 4: 4개의 워커 프로세스 사용
#    -b 0.0.0.0:5000: 모든 네트워크 인터페이스의 5000번 포트에 바인딩
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "app:app"]