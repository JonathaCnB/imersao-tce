from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Review, Schedule
from .serializers import (
    ReviewSerializer,
    ScheduleSerializer,
    ViewScheduleSerializer,
)


class ScheduleViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def list(self, request, *args, **kwargs):
        user = request.user
        now = datetime.now()
        now_date = datetime.now().date()
        now_time = datetime.now().time()
        qs = Schedule.objects.filter(is_active=True)
        qs = qs.filter(date__gte=now_date)
        qs = qs.filter(hour__gte=now_time)
        if user.service_user:
            qs = qs.filter(user__isnull=True)

        if user.service_provider:
            qs = qs.filter(service__responsible=user)

        serializer = ViewScheduleSerializer(qs, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user = request.user

        return super().create(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
