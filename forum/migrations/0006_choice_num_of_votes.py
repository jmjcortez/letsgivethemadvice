# Generated by Django 2.2 on 2020-04-27 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_choice_poll'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='num_of_votes',
            field=models.IntegerField(default=0),
        ),
    ]
