from django.shortcuts import render



def jotters(request):
    return render(request,'Jotters/home.html')

def add_jotters(request):
    return render(request,'Jotters/add_jotters.html')

def edit_jotters(request):
    return render(request,'Jotters/edit_jotters.html')

