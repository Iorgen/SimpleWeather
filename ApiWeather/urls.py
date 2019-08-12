from django.urls import path, include
from . import views
from rest_framework import routers


weather_router = routers.DefaultRouter()
weather_router.register('weather', views.WeatherView)

urlpatterns = [
    path('', views.home, name='ApiWeather-home'),
    path('docs/', views.docs, name='ApiWeather-docs'),
    path('api/v1/parse/', views.weather_parser),
    path('api/v1/', include(weather_router.urls)),

]
