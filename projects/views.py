from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import Project
from .forms import ProjectForm

from django.contrib.auth.decorators import login_required

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectobj = Project.objects.get(id=pk)
    tags = projectobj.tags.all()
    return render(request, 'projects/singlepage.html', {'project': projectobj, 'tags': tags})
@login_required(login_url='login')
def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        data = request.POST
        postFiles = request.FILES
        form = ProjectForm(data, postFiles)

        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request,'projects/project_form.html', context)

@login_required(login_url='login')
def updateProject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        data = request.POST
        postFiles = request.FILES
        form = ProjectForm(data, postFiles, instance=project)

        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request,'projects/project_form.html', context)

@login_required(login_url='login')
def deleteProject(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context= {'object' : project}
    return render(request, 'projects/delete_template.html',context)
