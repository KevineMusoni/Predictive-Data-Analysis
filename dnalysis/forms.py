from .models import Data
from django import forms
class DataForm(forms.ModelForm):
    class Meta:
        model= Data
        fields= '__all__'