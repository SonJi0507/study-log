import json
import os
import time
from datetime import datetime

from dotenv import load_dotenv
import pika

load_dotenv()

# RabbitMQ 설정
RABBITMQ_HOST = "localhost"
RABBITMQ_PORT = 5672
RABBITMQ_USER = os.getenv("RABBITMQ_DEFAULT_USER")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_DEFAULT_PASS")
QUEUE_NAME = "task_queue"


def get_rabbitmq_connection():
    """RabbitMQ 연결 생성"""
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
    parameters = pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        port=RABBITMQ_PORT,
        credentials=credentials,
        heartbeat=600,
        blocked_connection_timeout=300
    )
    return pika.BlockingConnection(parameters)


def publish_message(channel, message: dict):
    """RabbitMQ에 메시지 발행"""
    try:
        # 메시지 발행
        channel.basic_publish(
            exchange='',
            routing_key=QUEUE_NAME,
            body=json.dumps(message, ensure_ascii=False),
            properties=pika.BasicProperties(
                delivery_mode=2,  # 메시지를 디스크에 저장 (persistent)
                content_type='application/json',
            )
        )
        print(f" [✓] Sent: {message['content']}")
        return True
    except Exception as e:
        print(f" [✗] Failed to publish: {e}")
        return False


def main():
    """Producer 메인 함수"""
    print("=" * 60)
    print("🚀 RabbitMQ Producer Started")
    print("=" * 60)

    connection = None

    try:
        # RabbitMQ 연결
        connection = get_rabbitmq_connection()
        channel = connection.channel()

        # 큐 선언 (durable=True: RabbitMQ 재시작 시에도 유지)
        channel.queue_declare(queue=QUEUE_NAME, durable=True)

        print(f"📡 Connected to RabbitMQ")
        print(f"📦 Queue: {QUEUE_NAME}")
        print(f"🔄 Publishing messages... (Press CTRL+C to stop)\n")

        # 메시지 카운터
        count = 0

        # 지속적으로 메시지 발행
        while True:
            count += 1

            # 다양한 메시지 생성
            messages = [
                {
                    "content": f"Task #{count}: Process data",
                    "priority": 1,
                    "timestamp": datetime.now().isoformat(),
                    "metadata": {"task_id": count, "type": "data_processing"}
                },
                {
                    "content": f"Task #{count}: Send email notification",
                    "priority": 2,
                    "timestamp": datetime.now().isoformat(),
                    "metadata": {"task_id": count, "type": "notification"}
                },
                {
                    "content": f"Task #{count}: Generate report",
                    "priority": 3,
                    "timestamp": datetime.now().isoformat(),
                    "metadata": {"task_id": count, "type": "report"}
                },
            ]

            # 메시지 발행
            message = messages[count % 3]
            publish_message(channel, message)

            # 5초 대기
            time.sleep(5)

    except KeyboardInterrupt:
        print("\n\n⚠️  Shutting down producer...")
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        if connection and connection.is_open:
            connection.close()
            print("✅ Connection closed")
        print("\n👋 Producer stopped")


if __name__ == "__main__":
    main()

