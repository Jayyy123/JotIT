from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import Jotter,Addjotter
from django.contrib.auth.models import User
from Users.models import UserProfile



def jotters(request):
    if request.user.is_authenticated:
        jotters = Jotter.objects.all()
    else:
        return redirect('login')

    return render(request,'Jotters/jotters.html',{'a':jotters})

def add_jotters(request):
    if request.user.is_authenticated:
        newJotter = Addjotter()
        if request.method == 'POST':
            newJotter = Addjotter(request.POST)
            if newJotter.is_valid():
                newJotter.save()
                messages.success(request,"{} has been successfully saved".format(request.POST['title']))
                return redirect('jotters')
            else:
                messages.error(request,"An error occured and {} could not be saved!".format(request.POST['title']))
    else:
        return redirect('login')
    
    return render(request,'Jotters/add_jotter.html',{'a':newJotter})

def edit_jotters(request,pk):
    if request.user.is_authenticated:
        selectedJotter = Jotter.objects.get(id=pk)
        newJotter = Addjotter(instance = selectedJotter)
        if request.method == 'POST':
            newJotter = Addjotter(request.POST, instance = selectedJotter)
            if newJotter.is_valid():
                newJotter.save()
                messages.success(request,"{} has been updated successfully!".format(request.POST['title']))
                return redirect('jotters')
            else:
                messages.error(request,"There was an error  and {} could not be updated!")
    else:
        return redirect('login')

    return render(request,'Jotters/edit_jotters.html', {'a':newJotter})

def jotter(request,pk):
    if request.user.is_authenticated:
        selectedJotter = Jotter.objects.get(id=pk)
        
    else:
        return redirect('login')
    
    return render(request, 'Jotters/jotter.html', {'a':selectedJotter})

