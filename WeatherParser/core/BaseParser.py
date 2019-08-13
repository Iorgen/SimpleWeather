from abc import ABCMeta, abstractmethod
import requests
from requests.exceptions import HTTPError
from ApiWeather.models import City, Weather
from ApiWeather.exceptions import DatabaseUploadException
import datetime
import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'SimpleWeather.settings'
django.setup()
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class BaseParser(metaclass=ABCMeta):
    """ Base abstract class for all kind of parsers
    Using template method
    """
    _url = ''
    _params = {}

    def __init__(self):
        """
        :param url: source address information
        :param params: query execution parameters
        """
        super(BaseParser, self).__init__()

    def prepare_url(self, city):
        pass

    def send_request(self):
        response = requests.get(self._url, params=self._params)
        print(response.url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        return response

    def parse_response(self, response):
        pass

    def upload_to_database(self, weather_info):
        try:
            for weather in weather_info:
                weather = Weather(temperature=weather['temperature'],
                                  measurement_date=datetime.datetime.fromtimestamp(weather['date']),
                                  source=weather['source'],
                                  city=City.objects.all().filter(name=weather['city_name']).first())

                weather.save()
        except Exception as e:
            raise DatabaseUploadException('Database upload problem')

    def parse(self, city):
        self.prepare_url(city)
        response = self.send_request()
        weather_info = self.parse_response(response)
        self.upload_to_database(weather_info)


class BaseApiKeyParser(BaseParser):
    """Base class for all API kind of parsers
    """
    _city_param = 'None'
    _api_key_param = 'None'
    _api_key = 'None'

    def __init__(self, **kwargs):
        super(BaseApiKeyParser, self).__init__()


class BaseHtmlParser(BaseParser):
    """ Base class for all kind of html parsers
    """
    def __init__(self, **kwargs):
        super(BaseHtmlParser, self).__init__()
