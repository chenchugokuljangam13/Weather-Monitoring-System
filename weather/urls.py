from django.urls import path
from .views import index, update_weather, get_weather_by_date  # Import the new view

urlpatterns = [
    path('', index, name='index'),
    path('update/', update_weather, name='update_weather'),
    path('get_weather_by_date/', get_weather_by_date, name='get_weather_by_date'), # New path
]
