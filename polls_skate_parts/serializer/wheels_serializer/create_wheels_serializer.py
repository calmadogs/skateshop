from rest_framework import serializers


class CreateWheelsSerializer(serializers.ModelSerializer):
    wheels_size: int
    wheels_brand: str
    wheels_color: str
