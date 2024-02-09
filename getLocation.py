import requests
import geocoder

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location(ip):
    loc = geocoder.ip(ip)
    print(type(loc.latlng))
    return loc.latlng, loc.city
    

ip = get_ip()
print(get_location(ip))