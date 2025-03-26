from rest_framework import serializers
from .models import Application


class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['name', 'email', 'phone']


class ApplicationSerializer(serializers.ModelSerializer):
    hike_name = serializers.ReadOnlyField(source='hike.name')

    class Meta:
        model = Application
        fields = ['id', 'name', 'email', 'phone', 'created_at', 'cancelled', 'hike_name']
        read_only_fields = ['id', 'created_at', 'cancelled', 'hike_name']
