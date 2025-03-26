from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Устанавливаем переменную окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Создаем приложение Celery
app = Celery('hikehub')

# Загружаем конфигурацию из настроек Django с префиксом CELERY
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически ищем задачи в установленных приложениях Django
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
