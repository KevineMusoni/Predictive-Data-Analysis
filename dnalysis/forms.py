from django import forms
from .models import Register,Space,Dailys,Data

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ('business_name','contact', 'email','description')

class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        exclude =['register','posted_on']


class DailysForm(forms.ModelForm):
    class Meta:
        model = Dailys
        exclude =['register','posted_on']


class DataForm(forms.ModelForm):
    class Meta:
        model= Data
        fields= '__all__'

