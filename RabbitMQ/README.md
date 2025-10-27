# RabbitMQ with Python

순수 Python과 RabbitMQ를 사용한 메시지 큐 시스템

## 구조

- **Producer**: RabbitMQ에 지속적으로 메시지를 발행하는 서버
- **Consumer**: RabbitMQ에서 메시지를 소비하고 처리하는 서버

## 시작하기

### 0. `.env.sample`을 같은 위치에 `.env`로 복사하고 필요시 수정합니다.

```bash

### 1. RabbitMQ 시작

```bash
docker-compose up -d
```

RabbitMQ Management UI: http://localhost:15672
- Username: `${.env.RABBITMQ_DEFAULT_USER}`
- Password: `${.env.RABBITMQ_DEFAULT_PASS}`

### 2. 의존성 설치

```bash
uv sync
```

### 3. Producer 실행

터미널 1에서:

```bash
uv run python producer/main.py
```

또는

```bash
run_producer.bat
```

Producer는 5초마다 자동으로 메시지를 발행합니다.

### 4. Consumer 실행

터미널 2에서 (새 터미널):

```bash
uv run python consumer/main.py
```

또는

```bash
run_consumer.bat
```

Consumer는 메시지를 받아서 처리합니다.

## 작동 방식

1. **Producer**가 5초마다 메시지를 RabbitMQ의 `task_queue`에 발행
2. **Consumer**가 큐를 모니터링하며 메시지를 수신
3. Consumer가 메시지를 처리하고 통계 출력
4. 처리 완료 시 Acknowledgment 전송

## 실행 예시

### Producer 출력:
```
============================================================
🚀 RabbitMQ Producer Started
============================================================
📡 Connected to RabbitMQ
📦 Queue: task_queue
🔄 Publishing messages... (Press CTRL+C to stop)

 [✓] Sent: Task #1: Process data
 [✓] Sent: Task #2: Send email notification
 [✓] Sent: Task #3: Generate report
```

### Consumer 출력:
```
============================================================
🚀 RabbitMQ Consumer Started
============================================================
📡 Connected to RabbitMQ
📦 Queue: task_queue
⚙️  QoS: prefetch_count=1
👂 Waiting for messages... (Press CTRL+C to stop)

[✓] Received message:
   Content: Task #1: Process data
   Priority: 1
   Timestamp: 2025-10-27T17:30:00.123456
   📝 Processing data_processing...
   ✓ Completed!
   📊 Total processed: 1
```

## 주요 기능

- ✅ 지속적인 메시지 발행 (Producer)
- ✅ 자동 메시지 소비 (Consumer)
- ✅ 메시지 내구성 (durable queue)
- ✅ 수동 Ack/Nack 처리
- ✅ 에러 처리 및 재시도
- ✅ 처리 통계 출력
- ✅ 여러 Consumer 동시 실행 가능 (부하 분산)

## 여러 Consumer 실행하기

부하 분산을 위해 여러 Consumer를 동시에 실행할 수 있습니다:

```bash
# 터미널 1
uv run python consumer/main.py

# 터미널 2
uv run python consumer/main.py

# 터미널 3
uv run python consumer/main.py
```

RabbitMQ가 자동으로 메시지를 여러 Consumer에게 분산합니다!

## RabbitMQ Management UI

http://localhost:15672 에서:
- 큐 상태 모니터링
- 메시지 통계 확인
- 연결된 클라이언트 확인
- 메시지 직접 발행/조회

## 종료

Producer나 Consumer 종료:
- `CTRL+C` 누르기

RabbitMQ 종료:
```bash
docker-compose down
```


