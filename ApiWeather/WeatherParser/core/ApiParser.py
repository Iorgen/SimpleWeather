from .BaseParser import BaseParser
import requests
import pprint
# Get list of all classes from ApiParser
# dir(ApiParser)
# Then getattr(ApiParser, class_list[0]) - get realization of each parser classes, filter list by *Parser
# call Parsers


class BaseApiKeyParser(BaseParser):
    """Base class for all API kind of parsers
    """
    _city_param = None
    _api_key_param = None

    @property
    def city_param(self):
        return type(self)._city_param

    @property
    def api_key_param(self):
        return type(self)._api_key_param

    def __init__(self, api_key, **kwargs):
        super(BaseApiKeyParser, self).__init__(**kwargs)
        assert isinstance(api_key, str)
        self.api_key = api_key


class OpenWeatherApiParser(BaseApiKeyParser):
    """ Immutable Static variable settings for each API
    _city_param: get parameter name for city
    _api_key_param: auth access key to API
    """
    _city_param = 'q'
    _api_key_param = 'appid'

    def __init__(self, **kwds):
        """ Class for parsing weather via API from OpenWeather.org resource
        """
        super(OpenWeatherApiParser, self).__init__(**kwds)
        self.params[self._api_key_param] = self.api_key

    def prepare_url(self, city):
        self.params[self._city_param] = city

    def parse_response(self, response):
        open_weather = response.json()
        weather_info = dict()
        weather_info['source'] = 'OpenWeather.org'
        weather_info['temperature'] = open_weather['main']['temp']
        weather_info['date'] = int(open_weather['dt'])
        return weather_info
