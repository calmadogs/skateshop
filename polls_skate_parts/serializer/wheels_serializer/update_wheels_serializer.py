from rest_framework import serializers


class UpdateWheelsSerializer(serializers.ModelSerializer):
    wheels_size: int
    wheels_brand: str
    wheels_color: str
