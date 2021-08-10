from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm

# projectdetails = [
#     {'id':'1',
#     'title':'E-Commerce website',
#     'discription':"This is a fully functioning ecommerce website"
#     }, 
    
#     {'id':'2',
#     'title':'Social media website',
#     'discription':"This is a fully functioning social media website"
#     },

#     {'id':'3',
#     'title':'Portfolio website',
#     'discription':"This is a fully functioning portfolio website"
#     }

# ]


def project(request):
    Projects = Project.objects.all()
    context = {'projectdetails':Projects}
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
    return render(request,'project/delete_template.html',context)