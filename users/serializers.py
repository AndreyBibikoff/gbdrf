from rest_framework.serializers import HyperlinkedModelSerializer
from .models import TodoUser


class UserModelSerializerV1(HyperlinkedModelSerializer):
    class Meta:
        model = TodoUser
        fields = ('username', 'first_name', 'last_name', 'email')


class SimpleUserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = TodoUser
        fields = ('username')


class UserModelSerializerV2(HyperlinkedModelSerializer):
    class Meta:
        model = TodoUser
        fields = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser')
