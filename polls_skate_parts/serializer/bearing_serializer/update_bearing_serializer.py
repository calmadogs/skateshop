from rest_framework import serializers


class UpdateBearingSerializer(serializers.ModelSerializer):
    bearing_brand: str
