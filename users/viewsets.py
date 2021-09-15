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
