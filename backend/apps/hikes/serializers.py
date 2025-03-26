from rest_framework import serializers
from .models import Hike


class HikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hike
        fields = ['id', 'name', 'photo', 'description', 'short_description']
