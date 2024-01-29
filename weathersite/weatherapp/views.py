from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'weatherapp/weather_content.html')

# Hier müssen wir den Zugriff auf die API realisieren, evtl durch eine Methode
# Hier wird unter anderem in einzelnen Methoden eine HTTP-Anfrage angenommen und bearbeitet
# Das bedeutet wir verwalten hier welche Informationen im Browser angezeigt werden und verarbeiten Benutzer-Eingaben
