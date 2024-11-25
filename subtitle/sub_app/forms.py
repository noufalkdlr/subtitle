from django import forms
from . import models

class MovieForm(forms.ModelForm):
    class Meta:
        model = models.MovieInfo
        fields = '__all__'