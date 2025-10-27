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

# 통계
stats = {
    "total_processed": 0,
    "total_failed": 0,
    "start_time": datetime.now()
}


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


def process_message(message_data: dict):
    """메시지 처리 로직"""
    # 실제 비즈니스 로직 구현
    task_type = message_data.get("metadata", {}).get("type", "unknown")

    print(f"   📝 Processing {task_type}...")

    # 처리 시간 시뮬레이션
    time.sleep(1)

    print(f"   ✓ Completed!")


def callback(ch, method, properties, body):
    """메시지 콜백 함수"""
    try:
        # 메시지 파싱
        message = json.loads(body.decode())

        print(f"\n[✓] Received message:")
        print(f"   Content: {message.get('content', 'N/A')}")
        print(f"   Priority: {message.get('priority', 'N/A')}")
        print(f"   Timestamp: {message.get('timestamp', 'N/A')}")

        # 메시지 처리
        process_message(message)

        # 처리 완료 확인 (Acknowledgment)
        ch.basic_ack(delivery_tag=method.delivery_tag)

        # 통계 업데이트
        stats["total_processed"] += 1

        print(f"   📊 Total processed: {stats['total_processed']}")

    except json.JSONDecodeError as e:
        print(f"\n[✗] Invalid JSON: {e}")
        # JSON 파싱 실패 시 메시지 제거 (재시도 안 함)
        ch.basic_ack(delivery_tag=method.delivery_tag)
        stats["total_failed"] += 1

    except Exception as e:
        print(f"\n[✗] Error processing message: {e}")
        # 에러 발생 시 메시지를 다시 큐에 넣음 (재시도)
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
        stats["total_failed"] += 1


def main():
    """Consumer 메인 함수"""
    print("=" * 60)
    print("🚀 RabbitMQ Consumer Started")
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

        # QoS 설정: 한 번에 하나의 메시지만 처리
        # 이렇게 하면 여러 Consumer가 있을 때 부하 분산이 잘 됨
        channel.basic_qos(prefetch_count=1)

        print(f"⚙️  QoS: prefetch_count=1")
        print(f"👂 Waiting for messages... (Press CTRL+C to stop)\n")

        # 메시지 소비 시작
        channel.basic_consume(
            queue=QUEUE_NAME,
            on_message_callback=callback,
            auto_ack=False  # 수동 확인 모드
        )

        # 무한 루프로 메시지 대기
        channel.start_consuming()

    except KeyboardInterrupt:
        print("\n\n⚠️  Shutting down consumer...")

        # 최종 통계
        runtime = (datetime.now() - stats["start_time"]).total_seconds()
        print("\n" + "=" * 60)
        print("📊 Final Statistics:")
        print("=" * 60)
        print(f"✓ Total processed: {stats['total_processed']}")
        print(f"✗ Total failed: {stats['total_failed']}")
        print(f"⏱  Runtime: {runtime:.2f} seconds")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ Error: {e}")

    finally:
        if connection and connection.is_open:
            connection.close()
            print("✅ Connection closed")
        print("\n👋 Consumer stopped")


if __name__ == "__main__":
    main()

