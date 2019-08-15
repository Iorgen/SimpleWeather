from ApiWeather.models import City
from .core import parsers
from requests.exceptions import HTTPError
from ApiWeather.exceptions import ResponseParsingException, DatabaseUploadException
import logging
logger = logging.getLogger(__name__)


def parse_weather(cities):
    """
    method parsing weather for each parser in __init__.py - parsers in all cities
    :param cities: list
    :return: parse results list for each parser+city combination with error type
    """
    parse_results = {}
    for parser in parsers:
        parser = parser()
        for city in cities:
            try:
                city = City.objects.filter(name=city).first()
                parser.parse(city.name)
            except DatabaseUploadException as Dbe:
                logger.error(Dbe)
                parse_results[parser.__class__.__name__ + ' for ' + city.name] = 'Database loading error'
                pass
            except HTTPError as http_err:
                logger.error(http_err)
                parse_results[parser.__class__.__name__ + ' for ' + city.name] = 'Data request error'
                pass
            except ResponseParsingException as res_pars_err:
                logger.error(res_pars_err)
                parse_results[parser.__class__.__name__ + ' for ' + city.name] = 'Error parsing received response'
                pass
            except Exception as e:
                logger.error(e)
                parse_results[parser.__class__.__name__ + ' for ' + city.name] = 'Runtime error'
                pass
    return parse_results


