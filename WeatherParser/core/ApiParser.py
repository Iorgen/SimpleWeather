from .BaseParser import BaseApiKeyParser
from ApiWeather.exceptions import ResponseParsingException
import logging
logger = logging.getLogger(__name__)


class OpenWeatherApiParser(BaseApiKeyParser):

    _city_param = 'q'
    _api_key_param = 'appid'

    _url = 'http://api.openweathermap.org/data/2.5/weather'
    _api_key = 'ec96dbe80eea8425e6712cdff8ec9ee2'

    _params = {
        "units" : "metric"
    }

    def __init__(self, **kwds):
        """ Class for parsing weather via API from OpenWeather.org resource
        """
        super(OpenWeatherApiParser, self).__init__(**kwds)
        self._params[self._api_key_param] = self._api_key

    def prepare_url(self, city):
        self._params[self._city_param] = city
        return self._url

    def parse_response(self, response):
        try:
            open_weather = response.json()
            weather_info = dict()
            weather_info['source'] = 'OpenWeather.org'
            weather_info['temperature'] = open_weather['main']['temp']
            weather_info['date'] = int(open_weather['dt'])
            weather_info['city_name'] = open_weather['name']
            return [weather_info]
        except Exception as e:
            logger.error(e)
            raise ResponseParsingException('Parsing Exception')