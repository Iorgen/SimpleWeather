# Generated by Django 2.2.4 on 2019-08-12 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ApiWeather', '0002_weather_source'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weather',
            name='author',
        ),
    ]