from django.db import models
from django.contrib.auth.models import User


class Voter(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        primary_key=True,
    )
    times_voted = models.IntegerField(default=0)