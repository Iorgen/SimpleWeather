from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.schemas import get_schema_view

weather_router = routers.DefaultRouter()
weather_router.register('weather', views.WeatherView)


urlpatterns = [
    # Html pages urls
    path('', views.home, name='ApiWeather-home'),
    path('city_weather/<str:city_name>/', views.city_weather, name='ApiWeather-city'),
    path('docs/', views.docs, name='ApiWeather-docs'),
    # Api urls
    path('api/v1/', include(weather_router.urls)),
    path('api/v1/parse/', views.weather_parser),
    # Api Documentation urls
    path('docs/openapi', get_schema_view(
        title="Your Project",
        description="API for all things …"
    ), name='openapi-schema'),
]
