from .BaseParser import BaseHtmlParser
import dateutil.parser
from bs4 import BeautifulSoup
from ApiWeather.exceptions import ResponseParsingException
import logging
logger = logging.getLogger(__name__)


class YandexHtmlWeatherParser(BaseHtmlParser):
    """ Class for parsing weather from html from yandex.ru/pogoda/ resource
        """
    _url = 'http://yandex.ru/pogoda/'

    def __init__(self, **kwds):
        super(YandexHtmlWeatherParser, self).__init__(**kwds)

    def prepare_url(self, city):
        return self._url + city

    def parse_response(self, response, city):
        try:
            soup = BeautifulSoup(response.text, 'html.parser')
            current_time = soup.find(class_='time fact__time')
            current_weather = soup.find(class_='temp fact__temp fact__temp_size_s').find(class_="temp__value")
            weather_info = {}
            weather_info['temperature'] = current_weather.text[1:]
            print(weather_info['temperature'])
            weather_info['source'] = 'YandexPogoda'
            weather_info['date'] = dateutil.parser.parse(current_time['datetime']).timestamp()
            weather_info['city_name'] = city
            return [weather_info]
        except Exception as e:
            logger.error(e)
            raise ResponseParsingException('Parsing Exception')
