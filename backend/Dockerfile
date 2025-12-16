# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Prevent Python from writing pyc files to disc & buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
# requirements.txt를 먼저 복사하여 코드 변경 시에도 캐시를 활용할 수 있게 합니다.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Run the application
# main.py가 있는 위치에서 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]