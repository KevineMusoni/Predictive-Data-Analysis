from django import forms

from .models import Register,Space,Dailys

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ('business_name','contact', 'email','route')

class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        exclude =['register','posted_on']


class DailysForm(forms.ModelForm):
    class Meta:
        model = Dailys
        exclude =['register','posted_on']