from django.http import HttpResponse
from django.shortcuts import render
import requests

APIkey = "c4bb3958e6d110d2e0036c0027da9ad0"

def index(request):
    location = get_location()
    weather = get_current_weather(location["latitude"], location["longitude"], APIkey)
    context = {
        'weather': weather['weather'],
        'main': weather['main']
    }
    return render(request, 'weatherapp/weather_content.html', context)

#hier wird der jetzige Standort ausfindig gemacht

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude")
    }
    print(response)
    return location_data

#hier wird das Wetter am gesuchten Standort ausfindig gemacht

def get_current_weather(lat, lon, Key):
    response  = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={Key}&units=metric").json()

    current_weather = {
        "weather": response.get("weather"),
        "main": response.get("main")
    }
    return current_weather