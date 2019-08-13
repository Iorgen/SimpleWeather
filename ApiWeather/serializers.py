from rest_framework import serializers
from .models import Weather
from .models import City


class WeatherSerializer(serializers.ModelSerializer):
    # city = serializers.RelatedField(many=True)

    class Meta:
        model = Weather
        depth = 1
        fields = ('id', 'temperature', 'measurement_date', 'source', 'city')

