import factory

from forum.models.thread import Thread
from forum.tests.factories.poll_factory import PollFactory

class ThreadFactory(factory.django.DjangoModelFactory):

  class Meta:
    model = Thread

  title = factory.Faker('text')
  body = factory.Faker('text')
  date_posted = factory.Faker('date')
  date_created = factory.Faker('date')
  aftermath = factory.Faker('text')
  valid_from = factory.Faker('date')
  valid_until = factory.Faker('date')

  poll = factory.RelatedFactory(PollFactory, 'thread')