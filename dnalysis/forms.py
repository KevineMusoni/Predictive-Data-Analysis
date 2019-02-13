from django import forms
from django.contrib.auth.models import User

from .models import Register,Space,Dailys

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    business_name= forms.CharField(label="business name")
    contact= forms.CharField(label="contact")

    class Meta:
        model = User
        fields = ('username', 'email','password')
class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        fields =('business_name','no_of_small_buses','no_of_big_buses')

class DailysForm(forms.ModelForm):
    class Meta:
        model = Dailys
        fields =('income','month','no_of_passengers','no_of_trips')
