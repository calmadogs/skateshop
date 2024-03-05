from rest_framework import serializers

from ..models.wheels_model import Wheels


class WheelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wheels
        fields = "__all__"
