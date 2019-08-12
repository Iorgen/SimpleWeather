from abc import ABCMeta, abstractmethod
import requests
from requests.exceptions import HTTPError


class BaseParser(metaclass=ABCMeta):
    """ Base abstract class for all kind of parsers
    Using template method
    """
    def __init__(self, url, params):
        """
        :param url: source address information
        :param params: query execution parameters
        """
        assert isinstance(url, str)
        self.url = url
        self.params = params
        super(BaseParser, self).__init__()

    def prepare_url(self, city):
        pass

    def send_request(self):
        try:
            response = requests.get(self.url, params=self.params)
            print(response.url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print('HTTP error occurred:', http_err)  # Python 3.6
        except Exception as err:
            print('Other error occurred:', err)  # Python 3.6
        else:
            print('Success!')
        return response

    def parse_response(self, response):
        pass

    def upload_to_database(self, weather_info):
        print(weather_info)

    def parse(self, city):
        self.prepare_url(city)
        response = self.send_request()
        weather_info = self.parse_response(response)
        self.upload_to_database(weather_info)
