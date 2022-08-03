from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Project


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectobj = Project.objects.get(id=pk)
    tags = projectobj.tags.all()
    return render(request, 'projects/singlepage.html', {'project': projectobj, 'tags': tags})
