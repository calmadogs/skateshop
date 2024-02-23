from django.db import models


class Wheels(models.Model):
    id_wheels = models.AutoField(primary_key=True)
    wheels_size = models.IntegerField()
    wheels_brand = models.CharField(max_length=50)
    wheels_color = models.CharField(max_length=50)

    class Meta:
        db_table = "wheels"
        ordering = ["id"]
