from django.core.management.base import BaseCommand
from subprocess import Popen
from sys import stdout, stdin, stderr
import time, os, signal
from ApiWeather.models import City
from WeatherParser import parse_weather
import time


class Command(BaseCommand):
    help = 'Run parser loop '

    def handle(self, *args, **options):
        while 1:
            try:
                cities = City.get_cities_names()
                cities = cities[::1]
                parse_weather(cities)
                time.sleep(1000)
            except:
                continue
