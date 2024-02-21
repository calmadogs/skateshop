from django.db import models


class SkateParts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    shape_size = models.FloatField()
    truck_size = models.IntegerField()
    wheels_size = models.IntegerField()
    bearing_brand = models.CharField(max_length=100)

    class Meta:
        db_table = "skate_parts"
        ordering = ["id"]
