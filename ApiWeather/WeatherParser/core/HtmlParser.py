from .BaseParser import BaseParser
from bs4 import BeautifulSoup
import requests


class BaseHtmlParser(BaseParser):
    """ Base class for all kind of html parsers
    """
    def __init__(self, **kwargs):
        super(BaseHtmlParser, self).__init__(params={}, **kwargs)


class YandexHtmlWeatherParser(BaseHtmlParser):

    def __init__(self, **kwds):
        super(YandexHtmlWeatherParser, self).__init__(**kwds)

    def prepare_url(self, city):
        self.url += city

    def parse_response(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        current_time = soup.find(class_='time fact__time')
        current_weather = soup.find(class_='temp fact__temp')
        print(current_time)
        print(current_weather)
