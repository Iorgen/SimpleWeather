from ApiWeather.models import City
from .core import parsers
from requests.exceptions import HTTPError
from ApiWeather.exceptions import ResponseParsingException, DatabaseUploadException
import logging
logger = logging.getLogger(__name__)


def parse_weather(cities):
    parse_results = {}
    for parser in parsers:
        try:
            parser = parser()
            print(parser.__class__.__name__)
            for city in cities:
                city = City.objects.filter(name=city).first()
                parser.parse(city.name)
        except DatabaseUploadException as Dbe:
            logger.error(Dbe)
            parse_results[parser.__class__.__name__ + city.name] = 'Database loading error'
            pass
        except HTTPError as http_err:
            logger.error(http_err)
            parse_results[parser.__class__.__name__ + city.name] = 'Data request error'
            pass
        except ResponseParsingException as res_pars_err:
            logger.error(res_pars_err)
            parse_results[parser.__class__.__name__ + city.name] = 'Error parsing received response'
            pass
        except Exception as e:
            logger.error(e)
            parse_results[parser.__class__.__name__ + city.name] = 'Runtime error'
            pass
    return parse_results


