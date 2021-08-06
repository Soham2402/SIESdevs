from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','discription','demo_link','source_link','tags','featured_image']