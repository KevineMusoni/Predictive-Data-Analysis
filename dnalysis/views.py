from django.shortcuts import render

# Create your views here.
def about(request):
    title ='Dnalysis-About us'
    return render(request,'about.html',{'title':title})

def contacts(request):
    title='Dnalysis-Reach to us'
    return render(request,'contacts.html',{'title':title})