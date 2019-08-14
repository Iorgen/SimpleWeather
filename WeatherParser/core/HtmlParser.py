from .BaseParser import BaseHtmlParser
from bs4 import BeautifulSoup
from ApiWeather.exceptions import ResponseParsingException
import logging
logger = logging.getLogger(__name__)


# TODO fix YANDEX parser
class YandexHtmlWeatherParser(BaseHtmlParser):

    _url = 'https://yandex.ru/pogoda/'

    def __init__(self, **kwds):
        super(YandexHtmlWeatherParser, self).__init__(**kwds)

    def prepare_url(self, city):
        return self._url + city

    def parse_response(self, response):
        try:
            soup = BeautifulSoup(response.text, 'html.parser')
            current_time = soup.find(class_='time fact__time')
            current_weather = soup.find(class_='temp fact__temp')
            weather_info = []
            weather_info['temperature'] = '123'
            weather_info['source'] = '123'
            weather_info['date'] = 123456723
            weather_info['city_name'] = '123'
            return [weather_info]
        except Exception as e:
            logger.error(e)
            raise ResponseParsingException('Parsing Exception')

