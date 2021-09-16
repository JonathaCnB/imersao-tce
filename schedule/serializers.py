from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import Review, Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ["id", "service", "user", "date", "hour", "is_active"]


class ViewScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            "id",
            "get_responsible",
            "get_description_service",
            "user",
            "date",
            "hour",
            "is_active",
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "schedule", "user", "rating", "comment", "created_at"]
