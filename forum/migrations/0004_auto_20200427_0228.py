# Generated by Django 2.2 on 2020-04-27 02:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_thread_valid_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thread',
            name='valid_until',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
