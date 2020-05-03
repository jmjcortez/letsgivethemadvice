from django.contrib import admin

from forum.models.thread import Thread
from forum.models.poll import Poll, Choice

# Register your models here.
admin.site.register(Thread)
admin.site.register(Poll)
admin.site.register(Choice)