from django.core.management.base import BaseCommand
from apps.hikes.models import Hike
from apps.applications.models import Application
import random


class Command(BaseCommand):
    help = 'Создаёт 10 фейковых походов и случайные заявки (0–5)'

    def handle(self, *args, **options):
        if Hike.objects.exists():
            self.stdout.write("Фейковые данные уже созданы.")
            return

        for i in range(10):
            hike = Hike.objects.create(
                name=f"Поход {i+1}",
                photo=f"https://picsum.photos/seed/{random.randint(1,1000)}/800/600",
                description=f"Длинное описание похода {i+1}",
                short_description=f"Краткое описание похода {i+1}"
            )
            for j in range(random.randint(0, 5)):
                Application.objects.create(
                    hike=hike,
                    name=f"Участник {j+1}",
                    email=f"user{j+1}@example.com",
                    phone=f"+123456789{j}"
                )

        self.stdout.write("Фейковые данные успешно созданы.")
