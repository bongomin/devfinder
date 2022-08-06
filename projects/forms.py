from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'featured_img', 'demo_link', 'source_link', 'tags']
