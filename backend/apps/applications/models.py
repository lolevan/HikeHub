from django.db import models
from apps.hikes.models import Hike


class Application(models.Model):
    hike = models.ForeignKey(Hike, on_delete=models.CASCADE, related_name='applications')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    cancelled = models.BooleanField(default=False)

    def __str__(self):
        return f"Application #{self.id} for {self.hike.name}"
