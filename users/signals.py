from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save,post_delete
from django.core.mail import message, send_mail
from django.conf import settings
def onCreate(sender, instance,created,  **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            email = user.email,
            username = user.username,
            name = user.first_name,)

        subject = 'Welcome to SIESDevs!'
        message = 'This is an automated email'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False
        )

        

def updateUser(sender,instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()

        
def onDelete(sender,instance,**kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass
    
post_save.connect(onCreate, sender = User)
post_save.connect(updateUser,sender = Profile)
post_delete.connect(onDelete,sender = Profile)
