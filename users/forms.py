from django.forms import ModelForm
from .models import Profile,Skills,Message

class editProfile(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','location','short_intro','bio','profile_image','social_github',
        'social_twitter','social_linkedin','social_youtube','social_website']
        
    def __init__(self,*args,**kwargs):
        super(editProfile, self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
      
class skillForm(ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'
        exclude = ('owner',)
    def __init__(self,*args,**kwargs):
        super(skillForm, self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class messageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name','email','subject','body']

    def __init__(self,*args,**kwargs):
        super(messageForm, self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

