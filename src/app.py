import os
import pika
import boto3
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# 환경 변수 설정
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'rabbitmq')
MINIO_ENDPOINT = os.getenv('MINIO_ENDPOINT', 'http://minio:9000')
MINIO_ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY', 'admin')
MINIO_SECRET_KEY = os.getenv('MINIO_SECRET_KEY', 'password')

# S3(MinIO) 클라이언트 연결
s3 = boto3.client('s3',
                  endpoint_url=MINIO_ENDPOINT,
                  aws_access_key_id=MINIO_ACCESS_KEY,
                  aws_secret_access_key=MINIO_SECRET_KEY)

BUCKET_NAME = 'images'

# 버킷이 없으면 생성 (초기화)
try:
    s3.create_bucket(Bucket=BUCKET_NAME)
except:
    pass

@app.route('/')
def index():
    return "<h1>이미지 썸네일 서비스</h1><p>/upload 로 POST 요청을 보내세요.</p>"

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    filename = file.filename
    
    # 1. MinIO에 원본 저장
    s3.upload_fileobj(file, BUCKET_NAME, filename)
    
    # 2. RabbitMQ에 작업 메시지 전송
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    
    message = json.dumps({'filename': filename})
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(delivery_mode=2) # 메시지 영속성
    )
    connection.close()
    
    return jsonify({"message": f"Upload success. Task queued for {filename}"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)