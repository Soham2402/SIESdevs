from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_discussion, name='view-discussion'),
    path('create-discussion/', views.create_discussion, name='create-discussion'),
    path('single-discussion/<str:pk>/', views.single_discussion, name='single-discussion'),

]
