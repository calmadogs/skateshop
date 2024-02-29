from django.db import models


class Bearing(models.Model):
    bearing_brand = models.CharField(max_length=50)

    class Meta:
        db_table = "bearing"
        ordering = ["id"]
