from django.forms import ModelForm
from .models import Jotter

class Addjotter(ModelForm):
    class Meta:
        model = Jotter
        fields = ['title','snippet','detail','important']