from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers
from rest_framework.schemas import get_schema_view
# from background_task import background

weather_router = routers.DefaultRouter()
weather_router.register('weather', views.WeatherView)


urlpatterns = [
    path('', views.home, name='ApiWeather-home'),
    path('docs/', views.docs, name='ApiWeather-docs'),
    path('api/v1/parse/', views.weather_parser),
    path('api/v1/', include(weather_router.urls)),
    path('docs/openapi', get_schema_view(
        title="Your Project",
        description="API for all things …"
    ), name='openapi-schema'),
]
