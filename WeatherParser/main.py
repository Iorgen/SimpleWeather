# this app should working inside cron app
import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'SimpleWeather.settings'
django.setup()
from ApiWeather.models import City
from WeatherParser.core import parsers
from WeatherParser import parse_weather


if __name__ == "__main__":
    print("working")
    # cities = City.get_cities_names()
    # parse_weather(cities)