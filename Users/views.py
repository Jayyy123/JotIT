from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import UserForm,UserProfile,User, UserProfileform
from django.contrib.auth import login,logout,authenticate


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['username']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Incorrect Username\nPlease type in the correct username to continue')
        
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"You have been successfully logged in")
            return redirect('home')
        
        else:
            messages.error(request, 'Password or Username is incorrect')


    return render(request,'Users/login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')

    userform = UserForm()
    
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            user = userform.save(commit=False)
            user.save()
            login(request,user)
            messages.success(request,'Your account has been successfully created')
            messages.success(request,"You're being logged into your account now.\n Welcome {}".format(request.POST['username']))
            return redirect('home')

        else:
            messages.error(request, "There was an error signing up {}".format(request.POST['username']))


    return render(request,'Users/signup.html')

def profile(request):
    if request.user.is_authenticated:
        user = request.user
        profile = UserProfile.objects.get(username = user)
    else:
        return redirect('login')
    return render(request,'Users/profile.html',{'a':profile})

def edit_profile(request,pk):
    profile = UserProfile.objects.get(id=pk)
    profile_form = UserProfileform(instance=profile)

    if request.method == 'POST':
        profile_form = UserProfileform(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,"Changes have been successfully saved")
            return redirect(profile)
        else:
            messages.error(request,"There was an error updatimng your account.\nPlease Try again.")
    

    return render(request,'Users/edit_profile.html')