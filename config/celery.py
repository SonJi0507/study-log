import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings",  # Djnago settings file 위치 ( celery setting이 위치한 파일)
)

app = Celery('config')
app.conf.timezone = 'Asia/Seoul'
app.conf.beat_schedule = {
    "test-periodic-job": {
        "task": "api.tasks.test_periodic_task",
        "schedule": crontab(
            minute=0
        )
    }
}
app.config_from_object(
    "django.conf:settings",
    namespace="CELERY"
)

app.autodiscover_tasks()
