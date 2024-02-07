from django import forms

# Hier wird das Formular in einer Klasse definiert, dieses wird dann in views.py in das HTML-Template gerendert.

class LocationForm(forms.Form):
    location = forms.CharField(label='Search for a city:', max_length=100)
