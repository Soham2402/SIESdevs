from django.contrib import admin
from .models import Project,Review,Tags

admin.site.register(Project)
admin.site.register(Tags)
admin.site.register(Review)

# Register your models here.
