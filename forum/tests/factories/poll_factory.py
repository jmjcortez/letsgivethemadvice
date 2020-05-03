import factory

from forum.models.poll import Poll, Choice


class ChoiceFactory(factory.django.DjangoModelFactory):

  class Meta:
    model = Choice

  text = factory.Faker('text')
  num_of_votes = 0


class PollFactory(factory.django.DjangoModelFactory):

  class Meta:
    model = Poll

  question = factory.Faker('text')
