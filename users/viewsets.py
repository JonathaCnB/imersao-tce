from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserFullSerializer


class ListUserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserFullSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data
        service_provider = False
        service_user = False
        password = make_password(data["password"])
        try:
            service_provider = data["service_provider"].title()
        except Exception:
            message = {"detail": "Nenhum perfil de usuário informado"}
        try:
            service_user = data["service_user"].title()
        except Exception:
            message = {"detail": "Nenhum perfil de usuário informado"}

        if not service_user and not service_provider:
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create(
                first_name=data["first_name"],
                last_name=data["last_name"],
                cell_phone=data["cell_phone"],
                email=data["email"],
                password=password,
                cnpj=data["cnpj"],
                address=data["address"],
                number=data["number"],
                complement=data["complement"],
                postal_code=data["postal_code"],
                district=data["district"],
                city=data["city"],
                state=data["state"],
                service_provider=service_provider,
                service_user=service_user,
            )
            user.password = password
            user.save()
            message = {"detail": "Usuário criado com sucesso"}
            return Response(message, status=status.HTTP_201_CREATED)
        except Exception:
            message = {"detail": f"{Exception}"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
