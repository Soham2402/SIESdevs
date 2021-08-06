from django.urls import path
from . import views


urlpatterns = [
    path("", views.project,name = 'project'),

    path("projects/<str:pk>/", views.projects,name = 'projects'),

    path("create-post", views.createPost,name = 'create-project'),

    path("edit-post/<str:pk>/", views.editPost,name = 'edit-project'),

    path("delete-post/<str:pk>/", views.deletePost,name = 'delete-project'),

]
