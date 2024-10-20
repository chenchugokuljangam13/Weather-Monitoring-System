# Weather Monitoring System

The **Weather Monitoring System** is a Django-based application designed to retrieve, process, and display real-time and historical weather data. The application integrates with the OpenWeatherMap API to provide weather insights, daily summaries, and alerts.

## Features
- **Real-Time Data**: Retrieves real-time weather data from the OpenWeatherMap API.
- **Temperature Conversion**: Converts temperature units (Celsius, Fahrenheit, etc.).
- **Daily Summaries**: Aggregates weather data into daily summaries.
- **Weather Alerts**: Sends alerts when the weather conditions meet predefined thresholds.
- **Historical Data**: Retrieves and displays historical weather data for a specific date.
- **Forecasting**: (Bonus) Supports weather forecasting features.

## Project Structure
Here's a breakdown of the important files and folders in this project:

    ```graphql
    /WEATHER_MONITORING
    ├── /weather               # Django app for weather monitoring
    │   ├── /migrations        # Database migrations
    │   ├── /static            # Static files (CSS, JS, etc.)
    │   │   └── /weather
    │   │       └── styles.css # Stylesheet for the weather app
    │   ├── /templates         # HTML templates
    │   │   └── /weather
    │   │       ├── index.html          # Main page
    │   │       └── weather_data.html    # Page for displaying weather data
    │   ├── __init__.py       # Indicates this directory is a Python package
    │   ├── admin.py          # Admin panel configuration
    │   ├── apps.py           # App configuration
    │   ├── models.py         # Database models
    │   ├── tests.py          # Tests for the app
    │   ├── urls.py           # URL routing for the app
    │   └── views.py          # Views for handling requests
    ├── /weather_monitoring    # Main project directory
    │   ├── __init__.py       # Indicates this directory is a Python package
    │   ├── asgi.py           # ASGI configuration for async support
    │   ├── settings.py       # Project settings
    │   ├── urls.py           # URL routing for the project
    │   ├── wsgi.py           # WSGI configuration for deployment
    │   └── _pycache          # Compiled Python files (automatically generated)
    ├── .env                  # Environment variables
    ├── db.sqlite3            # SQLite database file
    ├── manage.py             # Django management script
    └── README.md             # Project documentation


## Installation
1. Clone the Repository
    ```bash
    git clone https://github.com/chenchugokuljangam13/Weather-Monitoring-System.git
    cd Weather-Monitoring-System


2. Install Dependencies
- Install the required Python packages from requirements.txt:

    ```bash
    pip install -r requirements.txt

3. Set Up Environment Variables
- Create a .env file in the project root:
    ```bash
    touch .env
- Add your OpenWeatherMap API Key to the .env file:
    ```bash
    OPENWEATHER_API_KEY=your_api_key_here
- Make sure settings.py in the WeatherMonitoring folder loads environment variables correctly using python-dotenv:
    ```bash
    import os
    from dotenv import load_dotenv

    load_dotenv()
    OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

4. Run Database Migrations
    ```bash
    python manage.py migrate

5. Start the Django Development Server
    ```bash
    python manage.py runserver
-Visit http://localhost:8000 in your browser to access the Weather Monitoring System.


## Usage
- Access the main dashboard to view the current weather for a specified location.
- Use the form on the page to search weather data by date.
- Daily weather summaries and historical data can be viewed by entering a specific date.
- Alert thresholds for weather conditions can be customized in the settings.


## Future Enhancements
- Add more weather parameters (e.g., wind speed, visibility).
- Implement user authentication for personalized settings.
- Integrate support for forecasts of multiple days.

## Testing
- Run the Tests
    ```bash
    python manage.py test weather
