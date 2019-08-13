from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class City(models.Model):
    name = models.CharField(max_length=50, unique=True)
    region = models.CharField(max_length=40)

    # def __str__(self):
    #     return self.name

    @staticmethod
    def get_cities_names():
        return City.objects.order_by('name').values_list('name', flat=True).distinct('name')


class Weather(models.Model):
    temperature = models.CharField(max_length=40)
    measurement_date = models.DateTimeField(default=timezone.now)
    date_added = models.DateTimeField(default=timezone.now)
    source = models.CharField(default='', max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    # TODO Beatifull weather showing case
    def __str__(self):
        return self.city.name + " " + str(self.temperature) + str(self.date_added.day)

    @staticmethod
    def current_weather():
        last_weather = []
        for city in City.objects.all():
            Weather.objects.filter(city=city).last()
            last_weather.append(city)

        return last_weather

# Create your models here.
