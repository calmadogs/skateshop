from django.db import models


class Truck(models.Model):
    id_truck = models.AutoField(primary_key=True)
    truck_size = models.IntegerField()
    truck_brand = models.CharField(max_length=50)
    truck_color = models.CharField(max_length=50)

    class Meta:
        db_table = "truck"
        ordering = ["id"]
