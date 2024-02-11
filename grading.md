<!-- https://github.com/skills/communicate-using-markdown -->

# Grading Criteria Programmieren T3INF1004

In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.

## FACHKOMPETENZ (40 Punkte)

### Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)

<!-- Siehe Kenntnisse in prozeduraler Programmierung: zutreffendes wählen und beweisen-->

### Sie können die Syntax und Semantik von Python (10)

<!-- Eine Stelle aus ihrem Programmieren wählen auf die sie besonders stolz sind und begründen -->

Im folgenden Code-Beispiel sieht man eine selbstgeschriebene Funktion, in der z.B. eine If-Anfrage angewendet wird und ein Python.Modul verwendet wird. Dieses Modul gibt einem anhand eines Ortnamens latitude, longitude und des Ortnamen zurück. Dies wird realisiert, indem ein ganzes Dictionary zurückgegeben wird aus der Funktion. Konnte die Funktion anhand des location-Parameters keinen Ort finden, so gibt die Funktion None zurück. In diesem Ausschnitt werden also die für die Python-Syntax relevanten Themen dargestellt:
- Funktionsdefinition
- if-else
- instanziierung eines Objekts
- Methodenaufruf
- Dictionary-Erstellung
- Rückgabewert einer Funktion

```python
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
```
### Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)

<!-- Anhand von commits zeigen, wie sie im Projekt einen Beitrag geleistet haben-->

### Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)

<!-- Eine Stelle aus ihrem Programmieren wählen auf die sie besonders stolz sind und begründen -->

## METHODENKOMPETENZ (10 Punkte)

### Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)

<!-- Beweise anbringen für Nutzen folgender Tools (können links, screenshots und screnncasts sein)-->

<!-- GIT -->https://github.com/brudermaggi/weathersite

<!-- VSC -->![grafik](https://github.com/brudermaggi/weathersite/assets/152855041/4640f287-8886-4bde-9fcb-6f2654502d00)

<!-- Codepilot -->

<!-- other -->https://poe.com/PythonAIChat

## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

### Die Studierenden können ihre Software erläutern und begründen. (5)

<!-- You have helped someone else and taught something to a fellow student (get a support message from one person) --> Die meisten hilfe lief über Discord Voicechat, da man dabei auch den Bildschirm übertragen kann und es somit einfacher ist zu verstehen was der andere will.

### Sie können existierenden Code analysieren und beurteilen. (5)

<!-- You have critiqued another group project. Link to your critique here (another wiki page on your git) and link the project -->https://github.com/brudermaggi/weathersite/wiki/Critique-for-group:-Discord%E2%80%90Reminder%E2%80%90Bot

### Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)

<!-- Which technology did you learn outside of the teacher given input -->
Ich habe zu Beginn dieses Projekts angefangen, PyCharm zu verwenden. Vorher habe ich Visual Studio Code für alles verwendet und war zufrieden damit, aber dann erfuhr ich, dass die Produkte von JetBrains für Studenten kostenlos sind. Also bekam ich Zugang zu den Produkten und begann damit zu arbeiten. Die KI-Unterstützung ist sehr hilfreich beim Coden und erspart einem Zeit. Was ich allerdings nicht so gut finde ist, dass PyCharm in jeder Kleinigkeit einen Fehler sieht und sich beschwert. Das verunsichert einen manchmal. Jedoch gibt es für manche Fehler einfach keine Lösung, anscheinend muss man sich zufrieden stellen, dass ab und zu eine Line rot oder gelb unterstrichen ist. Was ich allerdings viel besser finde als bei VSC ist die Anbindung an Github, ich finde das verwalten eines repopsitorys auf dem lokalen PC viel einfacher, das wird bei PyCharm über einen extra Ordner mit Meta-Daten im Repository realisiert.
<!-- Did you get help from someone in the classroom (get a support message here from the person who helped you) -->
Ich habe mir zu PyCharm alles selber beigebracht, wenn ich mal Hilfe gebraucht habe, habe ich mir einen Stackoverflow-Beitrag oder ein Youtube-Video angeschaut.
Was die API´s angeht habe ich mir auch viel über Tutorials und Blogbeiträge angeeignet.
## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

### Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)

<!-- Which parts of your project are you proud of and why (describe, analyse, link) -->
In diesem Code-snipped habe ich die JSON-Datei, die mir die API zurückgegeben hat ausgewertet und nur die nötigsten Variablen ausgelesen.
Außerdem habe ich die Variable in einer bestimmten Reihenfolge in eine Liste gespeichert, damit wir diese ohne Probleme auf der Website übergeben und anzeigen können.
Der Code ist nicht sehr Komplex, trotzdem hat der Code 3 Iterationen gebraucht, bis wir den Output hatten, den wir benötigen.
```python
    sorted_forecast_main_list = []
    
    for i in range(0,40):
        sorted_forecast_list_in_list = []
        sorted_forecast_list_in_list.append(response["list"][i]["dt_txt"])
        sorted_forecast_list_in_list.append(response["list"][i]["main"]["temp"])
        sorted_forecast_list_in_list.append(response["list"][i]["weather"][0]["main"])

        if response["list"][i]["weather"][0]["main"] == "Rain":
            sorted_forecast_list_in_list.append(response["list"][i]["rain"]["3h"])
        else:
            sorted_forecast_list_in_list.append(0)

        sorted_forecast_main_list.append(sorted_forecast_list_in_list)
```

<!-- Where were the problems with your implementation, timeline, functionality, team management (describe, analyse, reflect from past to future, link if relevant) -->
Das Schwerste war meiner Meinung nach die Themenfindung, es war schwer ein Projekt zu finden, welches nicht zu schwer ist und nicht zu leicht ist, damit wir weder zu lange brauchen noch zu schnell fertig sind. Als wir unsere Projektidee hatten setzten wir uns daran zu schauen welche Features wir brauchen, wollen und welche ein nettes extra sind.![grafik](https://github.com/brudermaggi/weathersite/assets/152855041/5d10704b-707e-4faf-8a90-4d0cf14e06c9)
Unser Projekt haben wir dann in verschedene Arbeitsschritte gegliedert und mithilfe eines KANBAN-Boards abgearbeitet.![grafik](https://github.com/brudermaggi/weathersite/assets/152855041/4f8b9ecf-a1f5-4a88-9eb8-8d64a640dd79)
Bei der BEarbeitung des Projetk sind wir selbstverständlich auch auf Probleme gestoßen, die wir ebenfalls festgehalten haben:![grafik](https://github.com/brudermaggi/weathersite/assets/152855041/287a4669-61ab-49e2-a1ff-4036d2912d81)
So haben wir gemerkt, dass es einfacher und sicherer ist den Standort ohne eine API zu ermitteln. Aber auch Probleme mit der Dartstellung von Browsern haben wir festgehalten.

Reflektiert kann man sagen, dass wir viel Fortschritt gemacht haben, sowohl durch das erlernen neuer Skills, als auch das anwenden neu gelernter Techniken.

## Kenntnisse in prozeduraler Programmierung:

### - Algorithmenbeschreibung

```python
from functools import lru_cache

@lru_cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Ruft die fibonacci-Funktion für n=10 auf
print(fibonacci(10))  # Verwendet das zwischengespeicherte Ergebnis für n=10
```

### - Datentypen

```python
context = {
        'weather': weatheractual.get('weather', {}),
        'main': weatheractual.get('main', {}),
        'city': location[2],
        'forecast': context_forecast,
        'form': form
        }
```

### - E/A-Operationen und Dateiverarbeitung

```python
if request.method == 'POST':
    form = LocationForm(request.POST)
else:
    form = LocationForm()
```

### - Operatoren
Auszug aus dem Code
```python
        if response["list"][i]["weather"][0]["main"] == "Rain":
            sorted_forecast_list_in_list.append(response["list"][i]["rain"]["3h"])
        else:
            sorted_forecast_list_in_list.append(0)
```

### - Kontrollstrukturen

```python
if form.is_valid():
    location = form.cleaned_data['location']
    location_info = get_location_info(location)
```

### - Funktionen

```python
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
```

### - Stringverarbeitung

```python
response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={Key}&units=metric").json()
```

### - Strukturierte Datentypen

```python
context = {
                'weather': weatheractual.get('weather', {}),
                'main': weatheractual.get('main', {}),
                'city': location,
                'forecast': context_forecast,
                'form': form
            }
return render(request, 'weatherapp/weather_content.html', context)
```
