from .ApiParser import OpenWeatherApiParser
from .HtmlParser import YandexHtmlWeatherParser


# Parsers list
parsers = [
    OpenWeatherApiParser,
    YandexHtmlWeatherParser
]