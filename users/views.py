from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from .models import Profile,Skills

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request,"Username or pasword incorrect")
            return redirect('login')

        user = authenticate(request, username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect("profiles")
        else:
            messages.error(request,"Username or pasword incorrect")
            return redirect('login')
    return render(request, "users/login.html")
    

def logoutUser(request):
    logout(request)
    messages.success(request, "Log out successfull")
    return redirect("profiles")

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