from rest_framework import serializers

from .models import SelectedField


class SelectedFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectedField
        fields = (
            'id',
            'name',
        )