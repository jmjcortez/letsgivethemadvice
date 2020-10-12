from django.db import models

from forum.managers.thread_manager import ThreadManager


class Thread(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now=False)
    date_created = models.DateTimeField(auto_now=True)
    aftermath = models.TextField(blank=True, null=False)
    valid_from = models.DateTimeField(blank=True, null=True)
    valid_until = models.DateTimeField(blank=True, null=True)

    objects = ThreadManager()