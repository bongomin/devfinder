from django.shortcuts import render
from .models import Profile

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


