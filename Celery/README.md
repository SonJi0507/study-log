Celery
===
참고: https://docs.celeryq.dev/en/stable/getting-started/index.html


## Task Queue란?
Task queue는 스레드나 장비가 작업을 분배하는 매커니즘이다. 
Task queue의 input은 task로 불리는 작업 단위이다. 
전용 worker 프로세스는 수행할 새로운 작업이 있는지 Task Queue를 지속적으로 모니터링한다.

Celery는 메시지로 통신하며 broker를 통해서 worker와 client를 중재한다.
Task를 수행하기 위해서 clinet는 Task Queue에 메세지를 추가하고, broker는 worker에게 해당 메세지를 전달한다.

그리고 이러한 broker의 역할을 위해 RabbitMQ, Redis, AmazonSQS가 필요하다.
(실험적으로 Local 환경 개발을 위해 SQLite를 사용하는 것을 포함하여 여러 실험적인 도구를 사용할 수 있다고 한다.)

## Broker 선택

1. **RabbitMQ** : 배포 환경에서 Celery와 함께 사용하기에 좋다.
2. **Redis** : 갑작스러운 종료나, 정전 발생시 데이터 손실이 발생할 수 있다.
3. AWS SQS
4. SQLAlchemy
- [참고](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/index.html#broker-overview)

## Broker 설치 (RabbitMQ)
docker 환경에서 설치해서 사용했다.
``` sh
docker run -d -p 5672:5672 rabbitmq
```
<img src="./.static/.img/docker-rabbitMQ.png"></img>

