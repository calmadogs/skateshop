from rest_framework import serializers

from ..models.truck_model import Truck


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = "__all__"
