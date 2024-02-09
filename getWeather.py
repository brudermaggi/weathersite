import requests
import os
from dotenv import load_dotenv

load_dotenv()
APIkey = os.getenv("API_KEY")


def get_current_weather(lat, lon, Key):
    response  = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={Key}&units=metric").json()

    current_weather = {
        "weather": response.get("weather"),
        "main": response.get("main")
    }
    return current_weather


def get_weather_forecast(lat, lon, Key):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={Key}&units=metric").json()
    
    temp_list = []
    rain_list = []
    date_list=[]
    weather_list =[]


    for i in range(0,40):
        date_list.append(response["list"][i]["dt_txt"])
        temp_list.append(response["list"][i]["main"]["temp"])
        weather_list.append(response["list"][i]["weather"][0]["main"])

        if response["list"][i]["weather"][0]["main"] == "Rain":
            rain_list.append(response["list"][i]["rain"]["3h"])
        else:
            rain_list.append(0)
        print (i)


    forecast={
        "date_list": date_list,
        "temp_list": temp_list,
        "weather_list" : weather_list,
        "rain_list": rain_list
    }
    return forecast

forecast = get_weather_forecast(49.4925, 9.7736, APIkey)
print(forecast)
#print(get_current_weather(49.4925, 9.7736, APIkey))