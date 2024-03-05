from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_age = models.IntegerField()

    class Meta:
        db_table = "user"
        ordering = ["id"]
