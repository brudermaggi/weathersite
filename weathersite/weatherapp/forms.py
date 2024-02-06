from django import forms

class LocationForm(forms.Form):
    location = forms.CharField(label='Search for a city:', max_length=100)
