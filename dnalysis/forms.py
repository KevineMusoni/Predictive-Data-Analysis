from django import forms
from .models import Registration, NumberofBuses, NumberofMinibuses, NumberofMatatu


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        exclude = ['business', 'contact', 'date_today']

class NumberofMinibusesForm(forms.ModelForm):
   class Meta:
       model = NumberofMinibuses
       fields = ['rating']

class NumberofMatatuForm(forms.ModelForm):
   class Meta:
       model = NumberofMatatu
       fields = ['rating']

class NumberofBusesForm(forms.ModelForm):
   class Meta:
       model = NumberofBuses
       fields = ['rating']