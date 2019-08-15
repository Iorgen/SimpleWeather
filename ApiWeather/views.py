import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Weather, City
from .serializers import WeatherSerializer
from WeatherParser import parse_weather
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
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
        city_name = self.request.query_params.get('city_name', None)
        queryset = Weather.current_weather()
        if city_name is not None:
            queryset = Weather.weather_by_city(city_name)
            if queryset:
                return queryset
            else:
                raise NotFound()
        else:
            return queryset




