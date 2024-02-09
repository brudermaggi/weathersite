from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from geopy.geocoders import Nominatim
from .forms import LocationForm
import requests, os, geocoder
from dotenv import load_dotenv

load_dotenv()
APIkey = os.getenv("API_KEY")

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
            location = location.split(", ")[0]
            weatheractual = get_current_weather(latitude, longitude, APIkey)
            context_forecast = get_weather_forecast(latitude, longitude, APIkey)
            context_actual = {
                'weather': weatheractual.get('weather', {}),
                'main': weatheractual.get('main', {}),
                'city': location,
                'form': form
            }
            combined_context = {**context_actual, **context_forecast}
            return render(request, 'weatherapp/weather_content.html', combined_context)
        else:
            location = get_location()
            messages.error(request, "The searched city was not found, please try again.")
            latitude, longitude = location[:2]

        weatheractual = get_current_weather(latitude, longitude, APIkey)
        context_forecast = get_weather_forecast(latitude, longitude, APIkey)
    else:
        location = get_location()
        weatheractual = get_current_weather(location[0], location[1], APIkey)
        context_forecast = get_weather_forecast(location[0], location[1], APIkey)
    context_actual = {
        'weather': weatheractual.get('weather', {}),
        'main': weatheractual.get('main', {}),
        'city': location[2],
        'form': form
    }
    combined_context = {**context_actual, **context_forecast}
    return render(request, 'weatherapp/weather_content.html', combined_context)

#hier wird der jetzige Standort ausfindig gemacht

def get_location():
    response = requests.get('https://api64.ipify.org?format=json').json()   
    ip = response["ip"]
    loc = geocoder.ip(ip)
    location_data = loc.latlng
    location_data.append(loc.city)
    return location_data

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

#hier wird das Wetter am gesuchten Standort ausfindig gemacht

def get_current_weather(lat, lon, Key):
    response  = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={Key}&units=metric").json()

    current_weather = {
        "weather": response.get("weather"),
        "main": response.get("main")
    }
    return current_weather

def get_weather_forecast(lat, lon, Key):
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={Key}&units=metric").json()

    temp_list = []
    rain_list = []
    date_list = []
    weather_list = []

    for i in range(0, 40):
        date_list.append(response["list"][i]["dt_txt"])
        temp_list.append(response["list"][i]["main"]["temp"])
        weather_list.append(response["list"][i]["weather"][0]["main"])

        if response["list"][i]["weather"][0]["main"] == "Rain":
            rain_list.append(response["list"][i]["rain"]["3h"])
        else:
            rain_list.append(0)
        print(i)

    forecast = {
        "date_list": date_list,
        "temp_list": temp_list,
        "weather_list": weather_list,
        "rain_list": rain_list
    }
    return forecast
