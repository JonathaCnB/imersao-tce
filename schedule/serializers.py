from rest_framework import serializers

from .models import Review, Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ["service", "user", "date", "hour", "is_active"]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["schedule", "user", "rating", "comment", "created_at"]
