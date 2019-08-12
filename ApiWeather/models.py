from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=40)

    def __str__(self):
        return str(self.id) + self.name + "," + self.region


class Weather(models.Model):
    temperature = models.CharField(max_length=40)
    measurement_date = models.DateTimeField(default=timezone.now)
    date_added = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

# Create your models here.
