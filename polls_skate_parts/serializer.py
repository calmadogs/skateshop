from rest_framework import serializers
from .models import SkateParts


class SkatePartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkateParts
        fields = '__all__'
