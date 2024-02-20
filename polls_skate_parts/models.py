from django.db import models


class SkateParts(models.Model):
    shape_size = models.FloatField()
    truck_size = models.FloatField()
    wheels_size = models.IntegerField()
    bearing_brand = models.CharField(max_length=100)
