from django.shortcuts import render
from .models import Profile,Skills
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