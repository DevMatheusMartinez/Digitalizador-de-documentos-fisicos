from rest_framework import serializers

from .models import SelectedField, ConnectionsMysql, UserMan


class SelectedFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectedField
        fields = (
            'id',
            'name',
            'nameBank',
        )

class ConnectionsMysqlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionsMysql
        fields = (
            'id',
            'host',
            'user',
            'password',
            'database',
        )

class UsersManSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMan
        fields = (
            'id',
            'name',
            'email',
            'password',
        )