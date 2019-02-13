from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import RegisterForm,SpaceForm,DailysForm
from .models import Register

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
        return render(request, 'register/predict.html', {'title': title})


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
        