from django.forms import ModelForm
from .models import Profile,Skills

class editProfile(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','location','short_intro','bio','profile_image','social_github',
        'social_twitter','social_linkedin','social_youtube','social_website']
      
class skillForm(ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'
        exclude = ('owner',)
