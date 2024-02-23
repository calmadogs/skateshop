from rest_framework import serializers


class CreateTruckSerializer(serializers.ModelSerializer):
    truck_size: int
    truck_brand: str
    truck_color: str
