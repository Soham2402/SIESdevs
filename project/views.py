from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project, Tags
from .forms import ProjectForm,ReviewForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib import messages
from .utils import searchProject, paginateProject

def project(request):
    
    search_query, projects = searchProject(request)
    custom_range,projects = paginateProject(request,projects,8)

    context = {'projectdetails':projects,'search_query':search_query,"custom_range":custom_range}
    return render(request,'project/projects.html',context)



def projects(request,pk):
    projectObj = Project.objects.get(id = pk)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.owner = request.user.profile
        review.project = projectObj
        review.save()
        projectObj.CountReview
        messages.success(request,"Your review has been added!")
        return redirect('projects' , pk = projectObj.id)

    context = {'projectObj':projectObj,'form':form}
    return render(request,'project/single_project.html',context)

@login_required(login_url="login")
def createPost(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        newtags = request.POST.get("newtags").replace(","," ").split()
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save()
            project.owner = profile
            for tag in newtags:
                tag, created = Tags.objects.get_or_create(name = tag)
                project.tags.add(tag)
            project.save()
        return redirect('project')
    context = {'form':form}
    return render(request,'project/form_template.html',context)


@login_required(login_url="login")
def editPost(request,pk):
    projectObj = Project.objects.get(id = pk)
    form = ProjectForm(instance=projectObj)
    if request.method == 'POST':
        newtags = request.POST.get("newtags").replace(","," ").split()

        form = ProjectForm(request.POST, request.FILES, instance=projectObj)

        if form.is_valid():
            project = form.save()
            for tags in newtags:
                tags, created = Tags.objects.get_or_create(name = tags)
                project.tags.add(tags)
                project.save()
        return redirect('project')
    context = {'form':form}
    return render(request,'project/form_template.html',context)
    
@login_required(login_url="login")
def deletePost(request,pk):
    projectObj = Project.objects.get(id = pk)
    form = ProjectForm(instance=projectObj)
    if request.method == 'POST':
        projectObj.delete()
        return redirect('project')
    context = {'form':form}
    return render(request,'delete_template.html',context)

    
    