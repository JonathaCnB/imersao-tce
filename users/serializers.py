from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    id = serializers.SerializerMethodField(read_only=True)
    is_admin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "name", "is_admin", "score"]

    def get_id(self, obj):
        return obj.id

    def get_is_admin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if name == "":
            name = obj.email
        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "name", "is_admin", "token"]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    id = serializers.SerializerMethodField(read_only=True)
    is_admin = serializers.SerializerMethodField(read_only=True)
    state = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "email",
            "cell_phone",
            "is_admin",
            "state",
            "address",
            "city",
            "state",
            "service_provider",
            "service_user",
        ]

    def get_id(self, obj):
        return obj.id

    def get_is_admin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if name == "":
            name = obj.email
        return name

    def get_state(self, obj):
        return obj.get_state_display()
