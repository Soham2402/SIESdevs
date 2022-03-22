from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile,Skills
from django.db.models import Q 
from .forms import editProfile, skillForm, messageForm
from django.core.paginator import Paginator
from .utils import searchProfiles,paginateDevs

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
            return redirect(request.GET['next'] if 'next' in request.GET else 'profiles')
        else:
            messages.error(request,"Username or pasword incorrect")
            return redirect('login')
    return render(request, "users/login.html")
    


def logoutUser(request):
    logout(request)
    messages.success(request, "Log out successfull")
    return redirect("profiles")


def profiles(request):

    search_query, profiles = searchProfiles(request)
    custom_range, profiles = paginateDevs(request,profiles,6) 

    context = {'profiles':profiles,'search_query':search_query,'custom_range':custom_range}
    return render(request, 'users/profiles.html',context)



def userProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skills_set.exclude(discription__exact = "")
    otherSkills = profile.skills_set.filter(discription = "")
    projects = profile.project_set.all()
    disc = profile.discussionpost_set.all()
    context = {'profile':profile,'topSkills':topSkills,'otherSkills':otherSkills,"project":projects,'discussion':disc}
    return render(request,'users/user-profile.html',context)


@login_required(login_url="login")
def userAccount(request):
    profile = request.user.profile
    Skills = profile.skills_set.all()
    project = profile.project_set.all()
    discussion = profile.discussionpost_set.all()
    context = {"profile":profile,"skills":Skills,"project":project,'discussion':discussion}
    return render(request,'users/user-account.html',context)


@login_required(login_url="login")
def editAccount(request):
    profile = request.user.profile
    form = editProfile(instance = profile)
    
    if request.method == "POST":
        form = editProfile(request.POST,request.FILES,instance = profile)
        if form.is_valid():
            form.save()
            return redirect('user-account')
    context = {"form":form}
    return render(request,"users/edit-account.html",context)


@login_required(login_url="login")
def createSkill(request):
    profile = request.user.profile
    form = skillForm()
    if request.method == 'POST':
        form = skillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            return redirect("user-account")
    context = {"form":form}
    return render(request,"users/skill-form.html",context)

@login_required(login_url="login")
def editSkill(request,pk):
    profile = request.user.profile
    skillobj = profile.skills_set.get(id = pk)
    form = skillForm(instance=skillobj)

    if request.method == 'POST':
        form = skillForm(request.POST,instance=skillobj)
        if form.is_valid():
            form.save()
            return redirect("user-account")
    context = {"form":form}
    return render(request,"users/skill-form.html",context)


@login_required(login_url="login")
def deleteSkill(request,pk):
    profile = request.user.profile
    skillobj = profile.skills_set.get(id = pk)
    form = skillForm(instance=skillobj)

    if request.method == 'POST':
            skillobj.delete()
            return redirect("user-account")
    context = {"form":form,"object":skillobj}
    return render(request,"delete_template.html",context)

@login_required(login_url="login")
def inbox(request):
    profile = request.user.profile
    messageRequest = profile.messages.all()
    unread = messageRequest.filter(is_read = False).count() 
    context = {"requests":messageRequest,"unread":unread}
    return render(request,'users/inbox.html',context)

@login_required(login_url="login")
def viewMessage(request,pk):
    profile = request.user.profile
    messageRequest = profile.messages.get(id = pk)
    if messageRequest.is_read == False:
        messageRequest.is_read = True
        messageRequest.save()
    context = {'message':messageRequest}
    return render(request,'users/view-message.html',context)

def sendMessage(request,pk):
    profile = Profile.objects.get(id = pk)
    form = messageForm()

    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == 'POST':
        form = messageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.recipient = profile
            message.sender = sender

            if sender:
                message.email = sender.email
                message.name = sender.name
            message.save()

            messages.success(request,"Your message has been successfully sent!")
            return redirect('user-profile',pk = profile.id)

    context = {'form':form}
    return render(request, 'users/message-form.html',context)
