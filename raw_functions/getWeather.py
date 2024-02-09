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

    # Unsorted Forecast Dict
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

    # Sorted forecast list
    sorted_forecast = []

    for i in range(0,40):
        sorted_forecast.append(response["list"][i]["dt_txt"])
        sorted_forecast.append(response["list"][i]["main"]["temp"])
        sorted_forecast.append(response["list"][i]["weather"][0]["main"])

        if response["list"][i]["weather"][0]["main"] == "Rain":
            sorted_forecast.append(response["list"][i]["rain"]["3h"])
        else:
            sorted_forecast.append(0)
        sorted_forecast.append(i)
        sorted_forecast.append("Iteration")
        print ("Soerted iteration",i)


    # Sorted forecast dict
    sorted_list = []
    sorted_forecast2 = {}
    
    for i in range(0,40):
        sorted_list.clear()
        sorted_list.append(response["list"][i]["dt_txt"])
        sorted_list.append(response["list"][i]["main"]["temp"])
        sorted_list.append(response["list"][i]["weather"][0]["main"])

        if response["list"][i]["weather"][0]["main"] == "Rain":
            sorted_list.append(response["list"][i]["rain"]["3h"])
        else:
            sorted_list.append(0)

        sorted_forecast2[i] = sorted_list


        

    # Sorted forecast list in list
    sorted_forecast_list_in_list = []
    sorted_forecast_main_list = []
    
    for i in range(0,40):
        sorted_forecast_list_in_list.clear()
        sorted_forecast_list_in_list.append(response["list"][i]["dt_txt"])
        sorted_forecast_list_in_list.append(response["list"][i]["main"]["temp"])
        sorted_forecast_list_in_list.append(response["list"][i]["weather"][0]["main"])

        if response["list"][i]["weather"][0]["main"] == "Rain":
            sorted_forecast_list_in_list.append(response["list"][i]["rain"]["3h"])
        else:
            sorted_forecast_list_in_list.append(0)

        sorted_forecast_main_list.append(sorted_forecast_list_in_list)

    



    # sorted_forecast follows this Syntax:
        # [Date and Time, temperatur, weather Type, precipitation, iteration, Brakeword]

    return forecast, sorted_forecast, sorted_forecast2, sorted_forecast_main_list
forecast, sorted_forecast, sorted_forecast2, sorted_forecast_main_list = get_weather_forecast(49.4925, 9.7736, APIkey)
print(sorted_forecast_main_list)
#print(get_current_weather(49.4925, 9.7736, APIkey))