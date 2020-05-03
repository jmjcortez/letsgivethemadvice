from django.db import models

from forum.models.user import Voter
from forum.models.thread import Thread


class Comment(models.Model):
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    voter = models.ForeignKey(
        Voter,
        on_delete=models.PROTECT,
        related_name='voter_comments'
    )
    thread = models.ForeignKey(
        Thread,
        on_delete=models.PROTECT,
        related_name='thread_comments'
    )
