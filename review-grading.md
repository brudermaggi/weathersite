<!-- https://github.com/skills/communicate-using-markdown -->


# Grading Criteria Programmieren T3INF1004
In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.
Alle Kriterien betreffen nur die Projektarbeit. Beweismaterial kommt aus dem Gruppenprojekt.

# FACHKOMPETENZ (40 Punkte)

## Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)
<!-- Siehe Kenntnisse in prozeduraler Programmierung: zutreffendes wählen und beweisen-->

Siehe unten.

## Sie können die Syntax und Semantik von Python (10)
<!-- Eine Stelle aus ihrem Programmieren wählen auf die sie besonders stolz sind und begründen -->

Im folgenden Beispie wurde darauf geachtet, dass die Token nicht öffentlich im Git-Repository sichtbar sind, sondern in einer lokalen Datei abgespeichert sind. Das zeugt davon, dass sie sich gut mit dem Thema Discord-API auseinandergesetzt haben und die Risiken eines öffentlichen Tokens erkannt haben.

```python
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
JOKE = os.getenv('JOKE_TOKEN')
CHANNEL_GENERAL = int(os.getenv('CHANNEL_GENERAL'))
SERVER_ID = int(os.getenv('SERVER_ID'))
```

## Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)
<!-- Anhand von commits zeigen, wie jeder im Projekt einen Beitrag geleistet hat -->

![image](https://github.com/brudermaggi/weathersite/assets/151533450/49dc814a-c28d-4192-b2db-a654b0078867)


## Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)
<!-- Eine Stelle aus dem Projekt wählen auf die sie besonders stolz sind und begründen -->

Im folgenden Beispiel haben wir ein Dictionary ausgewählt, das eine Datenstruktur darstellt:

```python
database = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "discordbot"
)
```

# METHODENKOMPETENZ (10 Punkte)

## Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)
<!-- Beweise anbringen für Nutzen folgender Tools (können links, screenshots und screnncasts sein) -->

Die Studierenden haben beide Visual Studio Code als Entwicklungsumgebung genutzt und haben ihre Stände auf GitHub verwaltet.

https://github.com/D4C4N/Discord-Reminder-Bot/tree/main

<!-- zB -->
<!-- GIT -->
<!-- VSC -->
<!-- Copilot -->
<!-- other -->



# PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

## Die Studierenden können ihre Software erläutern und begründen. (5)
<!-- Jeder in der Gruppe: You have helped someone else and taught something to a fellow student (get a support message from one person) -->

Bei der Präsentation habe ich gemerkt, dass beide Studierenden sich super über ihr Projekt auskennen und sie konnten ihr erlentes Wissen gut vermitteln. 

## Sie können existierenden Code analysieren und beurteilen. (5)
<!-- Pro Gruppe:You have critiqued another group project. Link to your critique here (another wiki page on your git) and link the project in the critique, use these evaluation criteria to critique the other project. Make sure they get a top grade after making the suggested changes -->

https://github.com/SvenSrc/Programming-Habit/wiki/Critique-for-the-group:-Weathersite

https://github.com/D4C4N/Discord-Reminder-Bot/blob/main/Review-GradingCriteria.md

## Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)
<!-- Which technology did you learn outside of the teacher given input -->
<!-- Did you or your group get help from someone in the classroom (get a support message here from the person who helped you) -->

Die Studierenden haben sich in verscheidene Technologien eingearbeitet wie:

- Discord API
- Dadjoke API
- MySQL
- VSCode
- GIT

# ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

## Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)
<!-- Which parts of your project are you proud of and why (describe, analyse, link) -->
<!-- Where were the problems with your implementation, timeline, functionality, team management (describe, analyse, reflect from past to future, link if relevant) -->

Die Problemstellung des Projektes war, dass man sich ToDo's nicht selber merken will in der Freizeit, weil man keinen Kopf dafür hat. Somit kamen die Studierenden auf die Idee dem mit einer ToDo-Liste entgegenzuwirken. Durch die Integration in Discord anhand eines Bots, kann man diese einfach in einer Datenbank abspeichern. Somit hatte die Gruppe ein Problem und hat durch eine kreative Idee dieses Problem eliminiert. Ein weiterer Vorteil davon ist, dass man seine ToDo's auf jeder Plattform abrufen kann, da man Discord nicht nur auf dem PC sondern auch einem Smartphone nutzen kann.

# Kenntnisse in prozeduraler Programmierung:

## - Algorithmenbeschreibung

Im Projekt fanden wir keine Algorithmenbeschreibung, deswegen haben wir in den privaten discussions gesucht und wurden im folgenden Link fündig:

https://github.com/SvenSrc/Programming-Habit/discussions/12

## - Datentypen

```python
headers = {
    "X-RapidAPI-Key": JOKE,
    "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
  }
```

## - E/A-Operationen und Dateiverarbeitung

```python
@client.slash_command(guild_ids=[SERVER_ID], description="Our bot will greet you because he's nice :)")
async def hello(interaction: Interaction):
  member = interaction.user.mention
  await interaction.response.send_message(f"Hello, {member}! I am a bot.")
```

```python
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
JOKE = os.getenv('JOKE_TOKEN')
CHANNEL_GENERAL = int(os.getenv('CHANNEL_GENERAL'))
SERVER_ID = int(os.getenv('SERVER_ID'))
```

## - Operatoren

```python
if value_due_to != "":
        todos_message += f'* "{value_todo}" is due to "{value_due_to}"\n'
      else:
        todos_message += f'* {value_todo}\n'
```

## - Kontrollstrukturen

```python
if existing_item:
    await ctx.send("This item is already in the list.")
  else:
    # Insert the todo item into the database
    sql_insert = "INSERT INTO todolist (todo, user_id) VALUES (%s, %s)"
    value_insert = (messageSplit, ctx.user.id)
    cursor.execute(sql_insert, value_insert)
    database.commit()

    await ctx.send(f"Added {messageSplit} to your ToDo-List!")
```

## - Funktionen

```python
@client.event
async def on_member_remove(member):
  channel = client.get_channel(CHANNEL_GENERAL)
  await channel.send(f"{member.mention} has left us, we are sad to see them go.")
```

## - Stringverarbeitung

```python
await channel.send(f"Hello, {member.mention} here is a joke for you:\n{setup} - {punchline}")
```

## - Strukturierte Datentypen

```python
headers = {
    "X-RapidAPI-Key": JOKE,
    "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
  }
```
