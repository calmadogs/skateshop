from rest_framework import serializers


class CreateBearingSerializer(serializers.ModelSerializer):
    bearing_brand: str
