from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from geopy.geocoders import Nominatim
from .forms import LocationForm
import requests
import geocoder

APIkey = "c4bb3958e6d110d2e0036c0027da9ad0"

#Diese Funktion wird vom Routing der Website aufgerufen, wenn eine Anfrage eingeht. Das Formular wird geladen und das HTML-Template wird mit den Wetterdaten gerendert.

def indexview(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
    else:
        form = LocationForm()

    if form.is_valid():
        location = form.cleaned_data['location']
        location_info = get_location_info(location)
        if location_info:
            latitude = location_info['latitude']
            longitude = location_info['longitude']
            location = location_info['city']
            weather = get_current_weather(latitude, longitude, APIkey)
            context = {
                'weather': weather.get('weather', {}),
                'main': weather.get('main', {}),
                'city': location,
                'form': form
            }
            return render(request, 'weatherapp/weather_content.html', context)
        else:
            location = get_location()
            messages.error(request, "The searched city was not found, please try again.")
            latitude, longitude = location[:2]

        weather = get_current_weather(latitude, longitude, APIkey)
    else:
        location = get_location()
        weather = get_current_weather(location[0], location[1], APIkey)

    context = {
        'weather': weather.get('weather', {}),
        'main': weather.get('main', {}),
        'city': location[2],
        'form': form
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

def get_location_info(location):
    geolocator = Nominatim(user_agent="myapp")
    location_data = geolocator.geocode(location)
    if location_data:
        return {
            'latitude': location_data.latitude,
            'longitude': location_data.longitude,
            'city': location_data.address
        }
    else:
        return None
