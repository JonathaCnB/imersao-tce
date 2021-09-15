from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    responsible = SerializerMethodField()

    class Meta:
        model = Service
        fields = [
            "id",
            "service",
            "description",
            "responsible",
            "responsible",
            "is_active",
        ]

    def get_responsible(self, obj):
        return obj.responsible.first_name
