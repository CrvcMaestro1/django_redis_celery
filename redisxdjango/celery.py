import os

from celery import Celery
from celery.schedules import crontab

from redisxdjango.settings import REDIS_SERVER_URL

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'redisxdjango.settings')

app = Celery('redisxdjango')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.update(
    BROKER_URL=REDIS_SERVER_URL
)

app.conf.beat_schedule = {
    'reboot-cache-main-crontab': {
        'task': 'posts.tasks.reboot_cache_main_crontab',
        'schedule': crontab(minute="*"),
    },
}
