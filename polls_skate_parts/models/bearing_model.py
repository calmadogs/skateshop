from django.db import models

from polls_user.user_models import User


class Bearing(models.Model):
    bearing_brand = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "bearing"
        ordering = ["id"]
