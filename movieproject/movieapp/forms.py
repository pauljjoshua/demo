from django import forms
from . models import Movie
# from . forms import MovieForm

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','desc','year','img']