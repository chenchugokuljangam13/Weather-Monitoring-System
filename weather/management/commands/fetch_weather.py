# weather/management/commands/fetch_weather.py
import requests
from django.core.management.base import BaseCommand
from weather.models import WeatherData
from django.core.mail import send_mail
from django.utils import timezone
import datetime

API_KEY = 'your_openweathermap_api_key'  # Replace with your actual API key
ALERT_THRESHOLD = 35  # Example threshold for alerts

class Command(BaseCommand):
    help = 'Fetch weather data from OpenWeatherMap API'

    def handle(self, *args, **options):
        cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
        for city in cities:
            weather_data = self.process_weather_data(city)
            if weather_data:
                avg_temp, max_temp, min_temp, dominant_condition = weather_data
                WeatherData.objects.update_or_create(
                    city=city,
                    date=datetime.date.today(),
                    defaults={
                        'avg_temp': avg_temp,
                        'max_temp': max_temp,
                        'min_temp': min_temp,
                        'dominant_condition': dominant_condition
                    }
                )
        self.stdout.write(self.style.SUCCESS('Successfully fetched weather data.'))

    def fetch_weather_data(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        return response.json()

    def process_weather_data(self, city):
        data = self.fetch_weather_data(city)
        if data and data.get('cod') == 200:  # Check for successful response
            main = data['main']
            weather = data['weather'][0]
            avg_temp = main['temp']
            max_temp = main['temp_max']
            min_temp = main['temp_min']
            dominant_condition = weather['main']

            if avg_temp > ALERT_THRESHOLD:
                self.send_alert(city, avg_temp)

            return avg_temp, max_temp, min_temp, dominant_condition
        return None

    def send_alert(self, city, temperature):
        subject = f'Weather Alert for {city}'
        message = f'Temperature has exceeded {ALERT_THRESHOLD}°C. Current temperature is {temperature}°C.'
        send_mail(subject, message, 'from@example.com', ['to@example.com'])  # Update with real email
