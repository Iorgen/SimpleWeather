from .BaseParser import BaseHtmlParser
from bs4 import BeautifulSoup
import logging
logger = logging.getLogger(__name__)


# TODO fix YANDEX parser
class YandexHtmlWeatherParser(BaseHtmlParser):

    _url = 'https://yandex.ru/pogoda/'

    def __init__(self, **kwds):
        super(YandexHtmlWeatherParser, self).__init__(**kwds)

    def prepare_url(self, city):
        self._url += city

    def parse_response(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        current_time = soup.find(class_='time fact__time')
        current_weather = soup.find(class_='temp fact__temp')
        print(current_time)
        print(current_weather)
        weather_info = []
        weather_info['temperature'] = '123'
        weather_info['source'] = '123'
        weather_info['date'] = 123456723
        weather_info['city_name'] = '123'
        return [weather_info]
