import os
import pika
import boto3
import json
import time
from io import BytesIO
from PIL import Image

# 환경 변수
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'rabbitmq')
MINIO_ENDPOINT = os.getenv('MINIO_ENDPOINT', 'http://minio:9000')
MINIO_ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY', 'admin')
MINIO_SECRET_KEY = os.getenv('MINIO_SECRET_KEY', 'password')

s3 = boto3.client('s3',
                  endpoint_url=MINIO_ENDPOINT,
                  aws_access_key_id=MINIO_ACCESS_KEY,
                  aws_secret_access_key=MINIO_SECRET_KEY)

SOURCE_BUCKET = 'images'
TARGET_BUCKET = 'thumbnails'

# 썸네일 버킷 생성
try:
    s3.create_bucket(Bucket=TARGET_BUCKET)
except:
    pass

def process_image(ch, method, properties, body):
    data = json.loads(body)
    filename = data['filename']
    print(f" [x] Received {filename}")

    try:
        # 1. MinIO에서 원본 다운로드
        file_obj = s3.get_object(Bucket=SOURCE_BUCKET, Key=filename)
        file_content = file_obj['Body'].read()
        
        # 2. 이미지 리사이징 (Pillow)
        img = Image.open(BytesIO(file_content))
        img.thumbnail((100, 100)) # 100x100 썸네일 생성
        
        # 3. 메모리 버퍼에 저장
        buffer = BytesIO()
        img.save(buffer, format=img.format)
        buffer.seek(0)
        
        # 4. MinIO에 썸네일 업로드
        thumb_filename = f"thumb_{filename}"
        s3.upload_fileobj(buffer, TARGET_BUCKET, thumb_filename)
        print(f" [v] Thumbnail created: {thumb_filename}")
        
    except Exception as e:
        print(f" [!] Error processing {filename}: {e}")

    # 작업 완료 신호 (Ack)
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    # RabbitMQ 연결 재시도 로직 (컨테이너가 RabbitMQ보다 빨리 뜰 수 있음)
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
            channel = connection.channel()
            channel.queue_declare(queue='task_queue', durable=True)
            
            # 한 번에 하나씩만 처리 (QoS) - 이게 없으면 한 놈이 독점할 수 있음
            channel.basic_qos(prefetch_count=1) 
            
            channel.basic_consume(queue='task_queue', on_message_callback=process_image)
            print(' [*] Waiting for messages. To exit press CTRL+C')
            channel.start_consuming()
        except pika.exceptions.AMQPConnectionError:
            print("RabbitMQ not ready yet, retrying in 5s...")
            time.sleep(5)

if __name__ == '__main__':
    main()