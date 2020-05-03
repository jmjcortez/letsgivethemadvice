from django.db import models

from forum.models.thread import Thread


class Poll(models.Model):
    thread = models.OneToOneField(
        Thread,
        on_delete=models.PROTECT
    )
    question = models.TextField()


class Choice(models.Model):
    poll = models.ForeignKey(
        Poll,
        on_delete=models.PROTECT,
        related_name='poll_choices'
    )
    text = models.TextField()
    num_of_votes = models.IntegerField(default=0)