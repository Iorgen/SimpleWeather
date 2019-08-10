from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ApiWeather-home'),
    path('docs/', views.docs, name='ApiWeather-docs'),

]
