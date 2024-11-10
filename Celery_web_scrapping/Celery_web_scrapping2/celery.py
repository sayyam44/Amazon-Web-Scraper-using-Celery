# This module to define the Celery application instance
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Celery_web_scrapping2.settings")
app = Celery("Celery_web_scrapping2")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()