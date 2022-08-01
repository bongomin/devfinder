from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('projects/', views.projects, name='projects'),
     path('project/', views.project, name='project'),
    path('admin/', admin.site.urls),
]
