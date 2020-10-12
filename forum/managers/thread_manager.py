from datetime import datetime

from django.db import models

class ThreadManager(models.Manager):

  def get_current_thread(self):
    now = datetime.now()

    return self.filter(valid_from__lte=now, valid_until__gte=now).first()