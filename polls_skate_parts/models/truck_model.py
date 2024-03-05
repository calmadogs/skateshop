from django.db import models

from polls_user.user_models import User


class Truck(models.Model):
    truck_size = models.IntegerField()
    truck_brand = models.CharField(max_length=50)
    truck_color = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "truck"
        ordering = ["id"]
