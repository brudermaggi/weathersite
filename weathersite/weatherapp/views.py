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
            context = {
                'weather': weatheractual.get('weather', {}),
                'main': weatheractual.get('main', {}),
                'city': location,
                'forecast': context_forecast,
                'form': form
            }
            return render(request, 'weatherapp/weather_content.html', context)
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
    context = {
        'weather': weatheractual.get('weather', {}),
        'main': weatheractual.get('main', {}),
        'city': location[2],
        'forecast': context_forecast,
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
    # Das hier ist sozusagen ein Prozess, wobei ich den Code so angepasst habe, sodass wir das gewünschte Ergebnis haben
'''
    temp_list = []
    rain_list = []
    date_list = []
    weather_list = []

    # Unsorted Forecast Dict
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

    # Sorted forecast list
    sorted_forecast = []

    for i in range(0, 40):
        sorted_forecast.append(response["list"][i]["dt_txt"])
        sorted_forecast.append(response["list"][i]["main"]["temp"])
        sorted_forecast.append(response["list"][i]["weather"][0]["main"])

        if response["list"][i]["weather"][0]["main"] == "Rain":
            sorted_forecast.append(response["list"][i]["rain"]["3h"])
        else:
            sorted_forecast.append(0)
        sorted_forecast.append(i)
        sorted_forecast.append("Iteration")
        print("Soerted iteration", i)

    # Sorted forecast dict
    sorted_list = []
    sorted_forecast2 = {}

    for i in range(0, 40):
        sorted_list.clear()
        sorted_list.append(response["list"][i]["dt_txt"])
        sorted_list.append(response["list"][i]["main"]["temp"])
        sorted_list.append(response["list"][i]["weather"][0]["main"])

        if response["list"][i]["weather"][0]["main"] == "Rain":
            sorted_list.append(response["list"][i]["rain"]["3h"])
        else:
            sorted_list.append(0)

        sorted_forecast2[i] = sorted_list
'''
    # Sorted forecast list in list
    sorted_forecast_main_list = []

    for i in range(0, 40):
        sorted_forecast_list_in_list = []
        sorted_forecast_list_in_list.append(response["list"][i]["dt_txt"])
        sorted_forecast_list_in_list.append(response["list"][i]["main"]["temp"])
        sorted_forecast_list_in_list.append(response["list"][i]["weather"][0]["main"])

        if response["list"][i]["weather"][0]["main"] == "Rain":
            sorted_forecast_list_in_list.append(response["list"][i]["rain"]["3h"])
        else:
            sorted_forecast_list_in_list.append(0)

        sorted_forecast_main_list.append(sorted_forecast_list_in_list)

    # sorted_forecast follows this Syntax:
    # [Date and Time, temperatur, weather Type, precipitation]

    return sorted_forecast_main_list
