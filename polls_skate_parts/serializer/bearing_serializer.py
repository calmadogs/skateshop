from rest_framework import serializers

from ..models.bearing_model import Bearing


class BearingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bearing
        fields = "__all__"
