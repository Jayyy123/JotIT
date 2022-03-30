from django.shortcuts import render



def home(request):
    return render(request,'Jotters/home.html')

def about(request):
    return render(request,'Jotters/about.html')

def contact(request):
    return render(request,'Jotters/contact.html')
