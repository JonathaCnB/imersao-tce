from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from users.models import User

from .models import Service
from .serializers import ServiceSerializer


class ServiceViewSet(ModelViewSet):
    serializer_class = ServiceSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Service.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        is_active = data["is_active"].title()

        Service.objects.create(
            service=data["service"],
            description=data["description"],
            responsible=user,
            is_active=is_active,
        )
        return Response({"detail": "Serviço cadastrado com sucesso!"})

    def destroy(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        service = Service.objects.get(id=pk)
        service.is_active = False
        service.save()
        return Response({"detail": "Serviço deletado com sucesso!"})

    # Pesquisa de objeto por PK
    def retrieve(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        obj = Service.objects.get(id=pk)
        if not obj.is_active:
            return Response({"detail": "Objeto não localizado"})
        serializer = ServiceSerializer(obj, many=False)
        return Response(serializer.data)
