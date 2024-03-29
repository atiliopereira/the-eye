import os

from celery import Celery

from the_eye import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_eye.settings')
app = Celery('the_eye')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
