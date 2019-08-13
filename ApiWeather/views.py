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


@api_view(['GET', 'POST'])
def weather_parser(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        weather = Weather.objects.all()
        serializer = WeatherSerializer(weather, many=True)
        return Response(serializer.data)

    elif request.method == 'GET':
        try:
            cities = City.get_cities_names()
            cities = cities[::1]
            parse_results = parse_weather(cities)
            if not parse_results:
                return Response([], status=status.HTTP_201_CREATED)
            return Response(parse_results, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
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

