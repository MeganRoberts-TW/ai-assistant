from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_assistant_project.settings')

app = Celery('ai_assistant_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
