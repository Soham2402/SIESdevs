from django.db import models
import uuid
from users.models import Profile
# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(
        Profile,  null=True, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    discription = models.TextField(null = True, blank = True)
    featured_image = models.ImageField(null=True, blank = True, default = 'default.jpg')
    demo_link = models.CharField(max_length = 2000, null = True, blank = True)
    source_link = models.CharField(max_length = 2000, null = True, blank = True)
    tags = models.ManyToManyField('Tags', blank=True)
    total_vote = models.IntegerField(default = 0,null = True, blank = True)
    vote_ratio = models.IntegerField(default = 0,null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, 
                            primary_key = True, editable = False)

  
    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = '/default.jpg'
        return url


    @property
    def UserId(self):
        queryset = self.review_set.all().values_list('owner__id', flat = True)
        return queryset
        
    @property
    def CountReview(self):
        reviews = self.review_set.all()
        upvotes = reviews.filter(value = 'up').count()
        totalvotes = reviews.count()

        self.vote_ratio = (upvotes/totalvotes)*100
        self.total_vote = totalvotes
        self.save()

    class Meta:
        ordering = ['-vote_ratio','-total_vote','title']

    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_CHOICE = [

        ('up','Up Vote'),
        ('down','Down Vote'),

    ]
    owner = models.ForeignKey(
        Profile,  null=True, on_delete = models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(blank=True,null=True)
    value = models.CharField(max_length = 200, choices=VOTE_CHOICE)
    date_created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, 
                            primary_key = True, editable = False)

    class Meta:
        unique_together = [['owner','project']]            

    def __str__(self):
        return self.value


class Tags(models.Model):
    name = models.CharField(max_length = 200)
    date_created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, 
                            primary_key = True, editable = False)

    def __str__(self):
        return self.name
