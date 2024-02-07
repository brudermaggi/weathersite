<!-- https://github.com/skills/communicate-using-markdown -->

# Grading Criteria Programmieren T3INF1004

In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.

## FACHKOMPETENZ (40 Punkte)

# Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)

<!-- Siehe Kenntnisse in prozeduraler Programmierung: zutreffendes wählen und beweisen-->

# Sie können die Syntax und Semantik von Python (10)

<!-- Eine Stelle aus ihrem Programmieren wählen auf die sie besonders stolz sind und begründen -->

# Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)

<!-- Anhand von commits zeigen, wie sie im Projekt einen Beitrag geleistet haben-->

# Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)

<!-- Eine Stelle aus ihrem Programmieren wählen auf die sie besonders stolz sind und begründen -->

## METHODENKOMPETENZ (10 Punkte)

# Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)

<!-- Beweise anbringen für Nutzen folgender Tools (können links, screenshots und screnncasts sein)-->

<!-- GIT -->

<!-- VSC -->

<!-- Codepilot -->

<!-- other -->

## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

# Die Studierenden können ihre Software erläutern und begründen. (5)

<!-- You have helped someone else and taught something to a fellow student (get a support message from one person) -->

# Sie können existierenden Code analysieren und beurteilen. (5)

<!-- You have critiqued another group project. Link to your critique here (another wiki page on your git) and link the project -->

# Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)

<!-- Which technology did you learn outside of the teacher given input -->

<!-- Did you get help from someone in the classroom (get a support message here from the person who helped you) -->

## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

# Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)

<!-- Which parts of your project are you proud of and why (describe, analyse, link) -->

<!-- Where were the problems with your implementation, timeline, functionality, team management (describe, analyse, reflect from past to future, link if relevant) -->

## Kenntnisse in prozeduraler Programmierung:

# - Algorithmenbeschreibung

# - Datentypen

```python

STATIC_URL = 'static/'

```

# - E/A-Operationen und Dateiverarbeitung

```python

if request.method == 'POST':
    form = LocationForm(request.POST)
else:
    form = LocationForm()

```

# - Operatoren

```python

def get_location():
    response = requests.get('https://api64.ipify.org?format=json').json()   
    ip = response["ip"]
    loc = geocoder.ip(ip)
    location_data = loc.latlng
    location_data.append(loc.city)
    return location_data

```

# - Kontrollstrukturen

```python

if form.is_valid():
    location = form.cleaned_data['location']
    location_info = get_location_info(location)

```

# - Funktionen

```python

def get_current_weather(lat, lon, Key):
    response  = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={Key}&units=metric").json()

    current_weather = {
        "weather": response.get("weather"),
        "main": response.get("main")
    }
    return current_weather

```

# - Stringverarbeitung

```python

response  = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={Key}&units=metric").json()

```

# - Strukturierte Datentypen

```python

context = {
                'weather': weather.get('weather', {}),
                'main': weather.get('main', {}),
                'city': location,
                'form': form
            }
return render(request, 'weatherapp/weather_content.html', context)

```
