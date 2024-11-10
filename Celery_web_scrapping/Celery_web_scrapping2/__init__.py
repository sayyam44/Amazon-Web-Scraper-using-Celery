# To make sure that your Celery app is loaded when you start Django
from .celery import app as celery_app

__all__ = ["celery_app"]

# https://realpython.com/asynchronous-tasks-with-django-and-celery/#how-can-you-leverage-celery-for-your-django-app