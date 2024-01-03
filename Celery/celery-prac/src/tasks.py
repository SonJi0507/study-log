from celery import Celery

app = Celery("tasks", broker="pyamqp://localhost:5672//")


@app.task
def add(x, y):
    return x + y
