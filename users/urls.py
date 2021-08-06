from django.urls import path
from . import views


urlpatterns = [

    path("", views.profiles,name = 'profiles'),
    path('profile/<str:pk>/', views.userProfile, name = 'user-profile'),
    # path('userprof/<str:pk>/', views.userProf, name = 'user'), TESTING


]