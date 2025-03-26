from celery import shared_task
import time
from .models import Application


@shared_task
def create_application_task(hike_id, name, email, phone):
    time.sleep(5)  # искусственная задержка
    Application.objects.create(
        hike_id=hike_id,
        name=name,
        email=email,
        phone=phone
    )
