import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'SimpleWeather.settings'
django.setup()
from ApiWeather.models import City
from WeatherParser import parse_weather


if __name__ == "__main__":
    cities = City.get_cities_names()
    cities = cities[::1]
    parse_weather(cities)
