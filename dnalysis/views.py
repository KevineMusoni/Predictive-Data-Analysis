# pylab inline
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import RegisterForm,SpaceForm,DailysForm
from django.core import serializers
from .models import Register, Dailys
from datetime import datetime
import pandas as pd
import json, time

MONTHS_TO_NUMBER = dict((
        ('January', 1),
        ('February', 2),
        ('March', 3),
        ('April', 4),
        ('May', 5),
        ('June', 6),
        ('July', 7),
        ('August', 8),
        ('September', 9),
        ('October', 10),
        ('November', 11),
        ('December', 12),
    ))

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
        print("Above")
        if request.method == 'POST':
                
                print("Below")
                form = RegisterForm(request.POST)

                if form.is_valid():
                        # form.save()
                        user=User(username=form.cleaned_data["username"])
                        if form.cleaned_data["password"] != form.cleaned_data["confirm_password"]:
                                #dosomething since password is not same
                                pass
                        user.set_password(form.cleaned_data["password"])
                        user.save()
                        r=Register(business_name=form.cleaned_data["business_name"]\
                                ,contact=form.cleaned_data["contact"],user=user)
                        r.save()
                        return redirect("spacing")
        else:
                form = RegisterForm()
        return render(request, 'register/registration.html', {'form': form})

def space(request):
        print("Above")
        if request.method == 'POST':
                
                print("Below")
                form = SpaceForm(request.POST)

                if form.is_valid():
                        # form.save()
                        
                        return HttpResponseRedirect('Welcome to Dnalysis') 
        else:
                form = SpaceForm()
        return render(request, 'register/spacing.html', {'form':form})

def prediction(request):
        title='prediction'
        data = serializers.serialize("json", Dailys.objects.all(), fields = ('income', 'month', 'no_of_passengers', 'no_of_trips'))
        data = json.loads(data)
        no_of_passengers = []
        no_of_trips = []
        income = []
        print(data)
        for da in data:
                a = da["fields"]
                a['month'] = MONTHS_TO_NUMBER[a['month']]
                time_ha = time.mktime(datetime(year=2018, month=a['month'], day=1).timetuple())
                income.append((time_ha, a['income']))
                no_of_passengers.append((time_ha, a['no_of_passengers']))
                no_of_trips.append((time_ha, a['no_of_trips']))
        # data = pd.DataFrame(clean_data)
        # data.hist(data, width=.8, range=(1,12))
        
        return render(request, 'register/predict.html', locals())
        
def future(request):
        title= 'future'
        return render(request, 'register/future.html', locals())
def daily(request):
        print("Above")
        if request.method == 'POST':
                
                print("Below")
                form = DailysForm(request.POST)

                if form.is_valid():
 
                        form.save()
                        
                        # print("Bottom")
                        return HttpResponseRedirect('Welcome to Dnalysis') 
        else:
                form = DailysForm()
        return render(request, 'register/dailys.html', {'form':form })
        