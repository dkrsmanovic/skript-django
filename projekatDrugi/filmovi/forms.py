from django import forms
from . import models

class KreirajFilm(forms.ModelForm):
    class Meta:
        model = models.Film
        fields =['naziv', 'ocena', 'godina']