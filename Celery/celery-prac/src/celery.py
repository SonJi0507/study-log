from celery import Celery

app = Celery(
    "src",
    backend="rpc://",
    broker="pyamqp://localhost:5672//",
    include=["src.tasks"],
)

app.conf.update(
    result_expire=3600,
)

if __name__ == "__main__":
    app.start()
