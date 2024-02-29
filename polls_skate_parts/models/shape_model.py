from django.db import models


class Shape(models.Model):
    shape_size = models.FloatField()
    shape_brand = models.CharField(max_length=50)
    maple_or_marfin = models.CharField(max_length=6)

    class Meta:
        db_table = "shape"
        ordering = ["id"]
