from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Profile,Skills

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']

        try:
            user = User.objects.get(username = username)
        except:
            print("Username or password does not exist")

        user = authenticate(request, username = username,password = password)

        if user is not None:
            login(request,user)
            return redirect("profiles")

        else:
            print("Username or password does not exist")

    return render(request, "users/login.html")

def profiles(request):
    profiles = Profile.objects.all()
    skills = Skills.objects.all()

    context = {'profiles':profiles,'skills':skills}
    return render(request, 'users/profiles.html',context)



def userProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skills_set.exclude(discription__exact = "")
    otherSkills = profile.skills_set.filter(discription = "")
    context = {'profile':profile,'topSkills':topSkills,'otherSkills':otherSkills}
    return render(request,'users/user-profile.html',context)

# def userProf(request,pk):
#     profile = Profile.objects.get(id=pk)
#     context = {'profile':profile}
#     return render(request,'users/user-profile.html',context)