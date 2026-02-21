from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer
from auth_api.models import User


class UserCreateSerializer(DjoserUserCreateSerializer):
    class Meta(DjoserUserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'password', 'image')