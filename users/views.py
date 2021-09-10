from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import UserSerializer, UserSerializerWithToken


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["POST"])
def register_user(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name=data["first_name"],
            last_name=data["last_name"],
            username=data["email"],
            cell_phone=data["cell_phone"],
            email=data["email"],
            address=data["address"],
            postal_code=data["postal_code"],
            complement=data["complement"],
            city=data["city"],
            state=data["state"],
            password=make_password(data["password"]),
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except MultiValueDictKeyError:
        message = {"detail": "Parâmetros inválidos"}
    except IntegrityError:
        message = {"detail": "E-mail já cadastrado"}
    return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAdminUser])
def get_users(request):
    users = User.objects.filter(is_active=True)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAdminUser])
def update_user(request, pk):
    user = User.objects.get(id=pk)

    data = request.data

    user.first_name = data["first_name"]
    user.last_name = data["last_name"]
    user.username = data["email"]
    user.email = data["email"]
    user.postal_code = data["postal_code"]
    user.state = data["state"]
    user.address = data["address"]
    user.cell_phone = data["cell_phone"]
    user.complement = data["complement"]
    user.district = data["district"]
    user.city = data["city"]
    user.service_provider = data["service_provider"]
    user.service_user = data["service_user"]
    user.is_staff = data["is_admin"]

    user.save()

    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def delete_user(request, pk):
    user_for_deletion = User.objects.get(id=pk)
    user_for_deletion.is_active = False
    user_for_deletion.save()
    return Response("Usuario deletado")
