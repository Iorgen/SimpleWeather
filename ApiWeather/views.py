from django.shortcuts import render
import subprocess
from .models import City, Weather
from .serializers import WeatherSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .WeatherParser.core import ApiParser, HtmlParser


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
        # serializer = SnippetSerializer(data=request.data)
        params = {
        }
        try:
            OWP = ApiParser.OpenWeatherApiParser(api_key='ec96dbe80eea8425e6712cdff8ec9ee2', params=params,
                                                 url='http://api.openweathermap.org/data/2.5/weather')

            OWP.parse('Tomsk')
            return Response([], status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def home(request):
    # print('inside home')
    # print('Start parser process')
    # cmd = ['python', 'WeatherParser/test_script.py']
    # subprocess.Popen(cmd).wait()
    # print('ended')
    context = {
    }
    return render(request, 'ApiWeather/home.html', context=context)


def docs(request):
    return render(request, 'ApiWeather/docs.html', {'title': 'Docs'})


class WeatherView(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, ) - #TODO auth can be here
    # TODO condition, get current weather and take get params from query
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    def get_queryset(self):
        """ allow rest api to filter by submissions """
        city_name = self.request.query_params.get('city_name', None)
        queryset = Weather.objects.all()
        # TODO exception handler
        if city_name is not None:
            queryset = Weather.objects.all().filter(city__name=city_name)
        return queryset