from django.shortcuts import render 
from .forms import RegisterForm,SpaceForm,DailysForm


def registration(request):
    form = RegisterForm()
    form1 = SpaceForm()
    form2 = DailysForm()
    return render(request, 'register/registration.html', {'form': form,'form1':form1,'form2':form2 })