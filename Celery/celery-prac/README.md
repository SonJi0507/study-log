## 사용법
### Broker 실행
``` sh
docker run -d -p 5672:5672 rabbitmq
```

### Celery worker 실행
``` sh
celery -A tasks worker --loglevel=INFO
```