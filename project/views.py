from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project,Tags
from .forms import ProjectForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from .utils import searchProject, paginateProject
def project(request):
    
    search_query, projects = searchProject(request)
    custom_range,projects = paginateProject(request,projects,6)

    context = {'projectdetails':projects,'search_query':search_query,"custom_range":custom_range}
    return render(request,'project/projects.html',context)



def projects(request,pk):
    projectObj = Project.objects.get(id = pk)
    return render(request,'project/single_project.html',{'projectObj':projectObj})

@login_required(login_url="login")
def createPost(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('project')
    context = {'form':form}
    return render(request,'project/form_template.html',context)


@login_required(login_url="login")
def editPost(request,pk):
    projectObj = Project.objects.get(id = pk)
    form = ProjectForm(instance=projectObj)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=projectObj)
        if form.is_valid():
            form.save()
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