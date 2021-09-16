from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from services.models import Service

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
        data = request.data
        service = Service.objects.get(id=data["service"])
        if service.responsible != user:
            message = {"detail": "Serviço inválido"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        if user.service_provider:
            Schedule.objects.create(
                service=service, date=data["date"], hour=data["hour"]
            )
            return Response({"detail": "Horário cadastrado."})
        else:
            return Response(
                {"detail": "Você não tem permissão para cadastrar horários."}
            )

    def update(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        user = request.user
        qs = Schedule.objects.get(id=pk)
        if not qs.user:
            qs.user = user
            qs.save()

            return Response({"detail": "Horário reservado"})
        else:
            return Response({"detail": "Horário já foi reservado reservado"})


class ReviewViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
