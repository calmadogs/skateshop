from rest_framework import serializers


class UpdateTruckSerializer(serializers.ModelSerializer):
    truck_size: int
    truck_brand: str
    truck_color: str
