from django.http import HttpResponse
from django.shortcuts import render
import requests
import geocoder

APIkey = "c4bb3958e6d110d2e0036c0027da9ad0"

def index(request):
    location = get_location()
    weather = get_current_weather(location[0], location[1], APIkey)
    context = {
        'weather': weather['weather'],
        'main': weather['main'],
        'city': location[2]
    }
    return render(request, 'weatherapp/weather_content.html', context)

#hier wird der jetzige Standort ausfindig gemacht

def get_location():
    response = requests.get('https://api64.ipify.org?format=json').json()   
    ip = response["ip"]
    loc = geocoder.ip(ip)
    location_data = loc.latlng
    location_data.append(loc.city)
    return location_data

#hier wird das Wetter am gesuchten Standort ausfindig gemacht

def get_current_weather(lat, lon, Key):
    response  = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={Key}&units=metric").json()

    current_weather = {
        "weather": response.get("weather"),
        "main": response.get("main")
    }
    return current_weather
