import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('CORE')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
# app.conf.beat_schedule = {
#     '<NAME>': {
#         'task': '<function_name>',
#         'schedule': crontab(minute=00, hour=3),
#         'args': (),
#         'enabled': True
#     }
# }