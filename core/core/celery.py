import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core",broker="amqp://tenant1:tenant1@127.0.0.1:5672/tenant1")

app.config_from_object("django.conf:settings", namespace="CELERY")

# Celery Beat Settings

# app.conf.beat_schedule = {

#     "periodic_add_numbers": {

#         "task": "my_app.tasks.add_numbers",
#         "schedule": crontab(minute="*\1"),

#     },
# }

app.autodiscover_tasks()

@app.task(bind=True)

def debug_task(self):
    print(f"Request: {self.request!r}")