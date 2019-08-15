from abc import ABCMeta
import requests
from ApiWeather.models import City, Weather
from ApiWeather.exceptions import DatabaseUploadException
import datetime
import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'SimpleWeather.settings'
django.setup()
import logging
logger = logging.getLogger(__name__)


class BaseParser(metaclass=ABCMeta):
    """ Base abstract class for all kind of parsers
    Using template method
    1) prepare_url
    2) send_request
    3) parse_response
    4) upload_to_database
    """
    _url = ''
    _params = {}

    def __init__(self):
        super(BaseParser, self).__init__()

    def prepare_url(self, city):
        """ Base url preparation method """
        pass

    def send_request(self, url):
        """ Base request sending method """
        response = requests.get(url, params=self._params)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        return response

    def parse_response(self, response, city):
        """ Base request response parsing method """
        pass

    def upload_to_database(self, weather_info):
        """ Base database uploading method using Django ORM model"""
        try:
            for weather in weather_info:
                weather = Weather(temperature=weather['temperature'],
                                  measurement_date=datetime.datetime.fromtimestamp(weather['date']),
                                  source=weather['source'],
                                  city=City.objects.all().filter(name=weather['city_name']).first())

                weather.save()
        except Exception as e:
            logger.error(e)
            print(e)
            raise DatabaseUploadException('Database upload problem')

    def parse(self, city):
        url = self.prepare_url(city)
        response = self.send_request(url)
        weather_info = self.parse_response(response, city)
        self.upload_to_database(weather_info)


class BaseApiKeyParser(BaseParser):
    """Base class for all API kind of parsers
    """
    _city_param = ''
    _api_key_param = ''
    _api_key = ''

    def __init__(self, **kwargs):
        super(BaseApiKeyParser, self).__init__()


class BaseHtmlParser(BaseParser):
    """ Base class for all kind of html parsers
    """
    def __init__(self, **kwargs):
        super(BaseHtmlParser, self).__init__()
