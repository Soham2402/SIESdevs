from django.db import models
import uuid
from users.models import Profile
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class DiscussionPost(models.Model):
    owner = models.ForeignKey(
        Profile,  null=True, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    discription = models.TextField(null = True, blank = True)
    body = RichTextUploadingField(null = True)
    tags = models.ManyToManyField('Type', blank=True)
    total_vote = models.IntegerField(default = 0,null = True, blank = True)
    vote_ratio = models.IntegerField(default = 0,null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, 
                            primary_key = True, editable = False)   

    @property
    def CountReview(self):
        reviews = self.discreview_set.all()
        upvotes = reviews.filter(value = 'up').count()
        totalvotes = reviews.count()
        if totalvotes == 0:
            self.vote_ratio = 100
            self.total_vote = 0
        
        else:
            self.vote_ratio = (upvotes/totalvotes)*100
            self.total_vote = totalvotes
        self.save()

    
    def __str__(self):
        return self.title


class Discreview(models.Model):
    VOTE_CHOICE = [

        ('up','Up Vote'),
        ('down','Down Vote'),

    ]
    owner = models.ForeignKey(
        Profile,  null=True, on_delete = models.CASCADE)
    discussion_post = models.ForeignKey(DiscussionPost, on_delete=models.CASCADE)
    body = models.TextField(blank=True,null=True)
    value = models.CharField(max_length = 200, choices=VOTE_CHOICE)
    date_created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, 
                            primary_key = True, editable = False)

    def __str__(self):
        return self.value


class Type(models.Model):
    name = models.CharField(max_length = 200)
    date_created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, 
                            primary_key = True, editable = False)

    def __str__(self):
        return self.name
