from django.shortcuts import render, redirect
from .models import Weather, City
from .serializers import WeatherSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages
from WeatherParser import parse_weather
import logging
logger = logging.getLogger(__name__)


def home(request):
    cities = City.objects.all()
    context = {
        'last_weather': Weather.current_weather(),
        'cities': cities
    }
    return render(request, 'ApiWeather/home.html', context=context)


def city_weather(request, city_name):
    if city_name is None:
        messages.warning(request, "Choose city!")
        return redirect('ApiWeather-home')
    weather = Weather.weather_by_city(city_name)
    context = {
        'city_weather': weather,
        'cities': City.objects.all()
    }
    return render(request, 'ApiWeather/city.html',  context=context)


def docs(request):
    return render(request, 'ApiWeather/docs.html', {'title': 'Docs'})


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

        parse_results = parse_weather(validate_cities)
        response.update(parse_results)
        if not response:
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.error(e)
        return Response(["Api Error"], status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class WeatherView(viewsets.ModelViewSet):
    # TODO API authorization for key.
    # permission_classes = (IsAuthenticated, )
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    def get_queryset(self):
        """ allow rest api to filter by city_name and last  """
        city_name = self.request.query_params.get('city_name', None)
        queryset = Weather.current_weather()
        # TODO exception handler
        if city_name is not None:
            queryset = Weather.current_weather.filter(city__name=city_name)
        return queryset


class WeatherByCityView(viewsets.ModelViewSet):
    # TODO API authorization for key.
    # permission_classes = (IsAuthenticated, )
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    lookup_field = 'city__name'

    def retrieve(self, request, *args, **kwargs):
        city_name = kwargs.get('city__name', None)
        self.queryset = Weather.objects.all().filter(city__name=city_name)
        print(self.queryset)
        return super(WeatherByCityView, self).retrieve(request, *args, **kwargs)
        # return Response([], status=status.HTTP_201_CREATED)





