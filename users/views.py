from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from .forms import customUserCreationForm
from .models import Profile

from django.contrib import messages


def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)

        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('profiles')

        else:
            messages.error(request, 'User name or password is Incorrect')

    return render(request, 'users/login_register.html', {'page': page})


def logoutUser(request):
    logout(request)
    messages.error(request, 'User logged out !!!')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = customUserCreationForm()

    if request.method == 'POST':
        form = customUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User created successfully')
            login(request, user)
            return redirect('profiles')

        else:
            messages.error(request, 'Error occured , user not created !')
    context ={
        'page': page,
        'form': form
    }
    return render(request, 'users/login_register.html', context)


def Profiles(request):
    profiles = Profile.objects.all()
    constext = {
        'profiles': profiles
    }
    return render(request, 'users/profiles.html', constext)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    top_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description=(""))
    context = {
        'profile': profile,
        "top_skills": top_skills,
        "other_skills": other_skills
    }
    return render(request, 'users/user-profile.html', context)


