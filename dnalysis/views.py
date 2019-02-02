from django.shortcuts import render
from .forms import DataForm
# Create your views here.
def about(request):
    
    title ='Dnalysis-About us'
    return render(request,'about.html',{'title':title})

def contacts(request):
    form =DataForm()
    title='Dnalysis-Reach to us'
    return render(request,'contacts.html',{'title':title,'form':form})