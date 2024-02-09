<!-- https://github.com/skills/communicate-using-markdown -->

# Grading Criteria Programmieren T3INF1004

In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.

## FACHKOMPETENZ (40 Punkte)

### Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)

<!-- Siehe Kenntnisse in prozeduraler Programmierung: zutreffendes wählen und beweisen-->

### Sie können die Syntax und Semantik von Python (10)

<!-- Eine Stelle aus ihrem Programmieren wählen auf die sie besonders stolz sind und begründen -->

### Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)

<!-- Anhand von commits zeigen, wie sie im Projekt einen Beitrag geleistet haben-->

### Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)

<!-- Eine Stelle aus ihrem Programmieren wählen auf die sie besonders stolz sind und begründen -->

## METHODENKOMPETENZ (10 Punkte)

### Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)

<!-- Beweise anbringen für Nutzen folgender Tools (können links, screenshots und screnncasts sein)-->

<!-- GIT -->

<!-- VSC -->

<!-- Codepilot -->

<!-- other -->

## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

### Die Studierenden können ihre Software erläutern und begründen. (5)

<!-- You have helped someone else and taught something to a fellow student (get a support message from one person) -->

### Sie können existierenden Code analysieren und beurteilen. (5)

<!-- You have critiqued another group project. Link to your critique here (another wiki page on your git) and link the project -->

### Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)

<!-- Which technology did you learn outside of the teacher given input -->
Ich habe zu Beginn dieses Projekts angefangen, PyCharm zu verwenden. Vorher habe ich Visual Studio Code für alles verwendet und war zufrieden damit, aber dann erfuhr ich, dass die Produkte von JetBrains für Studenten kostenlos sind. Also bekam ich Zugang zu den Produkten und begann damit zu arbeiten. Die KI-Unterstützung ist sehr hilfreich beim Coden und erspart einem Zeit. Was ich allerdings nicht so gut finde, ist dass PyCharm in jeder Kleinigkeit einen Fehler und sich beschwert. Das verunsichert einen manchmal, jedoch gibt es für manche Fehler einfach keine Lösung, anscheinend muss man sich zufrieden stellen, dass ab und zu eine Line rot oder gelb unterstrichen ist. Was ich allerdings viel besser finde als bei VSC ist die Anbindung an Github, ich finde das verwalten eines repopsitorys auf dem lokalen PC viel einfacher, das wird bei PyCharm über einen extra Ordner mit Meta-Daten im Repository realisiert.
<!-- Did you get help from someone in the classroom (get a support message here from the person who helped you) -->
Ich habe mir zu PyCharm alles selber beigebracht, wenn ich mal Hilfe gebraucht habe, habe ich mir einen Stackoverflow-Beitrag oder ein Youtube-Video angeschaut.

## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

### Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)

<!-- Which parts of your project are you proud of and why (describe, analyse, link) -->

<!-- Where were the problems with your implementation, timeline, functionality, team management (describe, analyse, reflect from past to future, link if relevant) -->

## Kenntnisse in prozeduraler Programmierung:

### - Algorithmenbeschreibung

### - Datentypen

```python

STATIC_URL = 'static/'

```

### - E/A-Operationen und Dateiverarbeitung

```python

if request.method == 'POST':
    form = LocationForm(request.POST)
else:
    form = LocationForm()

```

### - Operatoren

```python

def get_location():
    response = requests.get('https://api64.ipify.org?format=json').json()   
    ip = response["ip"]
    loc = geocoder.ip(ip)
    location_data = loc.latlng
    location_data.append(loc.city)
    return location_data

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

response  = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={Key}&units=metric").json()

```

### - Strukturierte Datentypen

```python

context = {
                'weather': weather.get('weather', {}),
                'main': weather.get('main', {}),
                'city': location,
                'form': form
            }
return render(request, 'weatherapp/weather_content.html', context)

```
