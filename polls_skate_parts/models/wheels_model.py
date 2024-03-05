from django.db import models

from polls_user.user_models import User


class Wheels(models.Model):
    wheels_size = models.IntegerField()
    wheels_brand = models.CharField(max_length=50)
    wheels_color = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "wheels"
        ordering = ["id"]
