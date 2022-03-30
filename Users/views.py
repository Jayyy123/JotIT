from django.shortcuts import redirect, render


def loginPage(request):
    return render(request,'Users/login.html')

def logoutPage(request):

    return redirect('login')

def signup(request):
    return render(request,'Users/signup.html')

def profile(request):
    return render(request,'Users/profile.html')

def edit_profile(request):
    return render(request,'Users/edit_profile.html')