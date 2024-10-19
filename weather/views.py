import requests
from django.shortcuts import render
from .models import WeatherData
from django.utils import timezone
import datetime

API_KEY = 'your_openweathermap_api_key'  # Replace with your API key

def index(request):
    weather_data = WeatherData.objects.filter(date=datetime.date.today())
    return render(request, 'weather/index.html', {'weather_data': weather_data})


def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def process_weather_data(city):
    data = fetch_weather_data(city)
    if data and data.get('main'):
        main = data['main']
        weather = data['weather'][0]
        avg_temp = main['temp']
        max_temp = main['temp_max']
        min_temp = main['temp_min']
        dominant_condition = weather['main']
        return avg_temp, max_temp, min_temp, dominant_condition
    return None

def update_weather(request):
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    for city in cities:
        weather_data = process_weather_data(city)
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
    return render_weather_data(request)

def render_weather_data(request):
    weather_data = WeatherData.objects.filter(date=datetime.date.today())
    return render(request, 'weather/index.html', {'weather_data': weather_data})

# def get_weather_by_date(request):
#     weather_data = []
#     if request.method == 'POST':
#         date_str = request.POST.get('date')
#         try:
#             input_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
#             weather_data = WeatherData.objects.filter(date=input_date)
#         except ValueError:
#             # Handle invalid date format
#             weather_data = []
#     return render(request, 'weather/index.html', {'weather_data': weather_data})

def get_weather_by_date(request):
    weather_data = []
    current_weather = []
    if request.method == 'POST':
        date_str = request.POST.get('date')
        try:
            input_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            weather_data = WeatherData.objects.filter(date=input_date)
            if not weather_data.exists():
                # If there is no historical data for the entered date, fetch current weather
                cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
                for city in cities:
                    current_weather_data = process_weather_data(city)
                    if current_weather_data:
                        avg_temp, max_temp, min_temp, dominant_condition = current_weather_data
                        current_weather.append({
                            'city': city,
                            'date': input_date,
                            'avg_temp': avg_temp,
                            'max_temp': max_temp,
                            'min_temp': min_temp,
                            'dominant_condition': dominant_condition
                        })
        except ValueError:
            # Handle invalid date format
            weather_data = []
    return render(request, 'weather/index.html', {'weather_data': weather_data, 'current_weather': current_weather})