from django.shortcuts import render
from .models import Weather, City
from .serializers import WeatherSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from WeatherParser import parse_weather
import logging
logger = logging.getLogger(__name__)


@api_view(['GET'])
def weather_parser(request):
    """
    List all code snippets, or create a new snippet.
    """

    try:
        response = {}
        city_names = request.query_params.get('city_name', None)
        cities = City.get_cities_names()
        cities = cities[::1]
        if city_names is None:
            validate_cities = cities[::1]
        else:
            city_names = city_names.split('|')
            validate_cities = [c for c in city_names if c in cities]
            non_exist_cities = [c for c in city_names if c not in validate_cities]
            response = {c: 'not exist ' for c in non_exist_cities}

        # cities = City.get_cities_names()
        # cities = cities[::1]
        parse_results = parse_weather(cities)
        response.update(parse_results)
        if not response:
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.error(e)
        return Response(["Api Error"], status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class WeatherView(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, ) - #TODO auth can be here
    # TODO condition, get current weather and take get params from query
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    def get_queryset(self):
        """ allow rest api to filter by city_name and last  """
        city_name = self.request.query_params.get('city_name', None)
        queryset = Weather.objects.all()
        # TODO exception handler
        if city_name is not None:
            queryset = Weather.objects.all().filter(city__name=city_name)
        return queryset


def home(request):
    context = {}
    # Show last info about weather using buit-in function Weather
    return render(request, 'ApiWeather/home.html', context=context)


def docs(request):
    return render(request, 'ApiWeather/docs.html', {'title': 'Docs'})

