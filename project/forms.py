from django.forms import ModelForm
from .models import Project,Review

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','discription','demo_link','source_link','tags','featured_image']

    def __init__(self,*args,**kwargs):
        super(ProjectForm, self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value','body']

        label = {
            'value':"Place your vote",
            'body': "Place your feedback here"
        }
    def __init__(self,*args,**kwargs):
        super(ReviewForm, self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})