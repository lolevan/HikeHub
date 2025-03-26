from django.db import models


class Hike(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='hikes/')
    description = models.TextField()
    short_description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
