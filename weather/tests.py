from django.test import TestCase
from .models import WeatherData
from django.core.management import call_command

class WeatherDataTests(TestCase):

    def test_weather_data_creation(self):
        weather = WeatherData.objects.create(
            city='Delhi',
            date='2024-10-19',
            avg_temp=25.5,
            max_temp=30.0,
            min_temp=20.0,
            dominant_condition='Clear'
        )
        self.assertEqual(weather.city, 'Delhi')
        self.assertEqual(weather.avg_temp, 25.5)
    
