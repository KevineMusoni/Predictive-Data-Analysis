from django.shortcuts import render
from .forms import RegisterForm,SpaceForm,DailysForm

# Create your views here.
def home_page(request):
    
    return render(request,'home.html',locals())

def about(request):
    title ='Dnalysis-About us'
    return render(request,'about.html',{'title':title})

def contacts(request):
    title='Dnalysis-Reach to us'
    return render(request,'contacts.html',{'title':title})

def registration(request):
    form = RegisterForm()
    form1 = SpaceForm()
    form2 = DailysForm()
    return render(request, 'register/registration.html', {'form': form,'form1':form1,'form2':form2 })
