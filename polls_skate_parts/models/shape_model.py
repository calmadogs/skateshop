from django.db import models

from polls_user.user_models import User


class Shape(models.Model):
    shape_size = models.FloatField()
    shape_brand = models.CharField(max_length=50)
    maple_or_marfin = models.CharField(max_length=6)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "shape"
        ordering = ["id"]
