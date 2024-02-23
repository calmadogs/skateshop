from rest_framework import serializers


class DetailedTruckSerializer(serializers.ModelSerializer):
    id_truck: int
    truck_size: int
    truck_brand: str
    truck_color: str
