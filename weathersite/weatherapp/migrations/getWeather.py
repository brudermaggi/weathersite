import requests

APIkey = "c4bb3958e6d110d2e0036c0027da9ad0"

def get_current_weather(lat, lon, Key):
    response  = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={Key}&units=metric").json()

    current_weather = {
        "weather": response.get("weather"),
        "main": response.get("main")
    }
    return current_weather

print(get_current_weather(48.8302 , 10.0709, APIkey))