from rest_framework import serializers
from .models import Weather


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        depth = 1
        fields = ('id', 'temperature', 'date_added', 'measurement_date', 'source', 'city')

