from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Review, Schedule
from .serializers import ReviewSerializer, ScheduleSerializer


class ScheduleViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ReviewViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
