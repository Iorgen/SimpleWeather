from rest_framework import serializers
from .models import Weather


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        depth = 1
        fields = ('id', 'temperature', 'measurement_date', 'source', 'city')

