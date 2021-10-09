from django.urls import path
from . import views


urlpatterns = [

    path("login/", views.loginUser,name = 'login'),
    path("logout/", views.logoutUser,name = 'logout'),


    path("", views.profiles,name = 'profiles'),
    path('profile/<str:pk>/', views.userProfile, name = 'user-profile'),
    # path('userprof/<str:pk>/', views.userProf, name = 'user'), TESTING

    path("user-account/", views.userAccount,name = 'user-account'),
    path("edit-account/", views.editAccount,name = 'edit-account'),

    path("create-skill/", views.createSkill,name = 'create-skill'),
    path("edit-skill/<str:pk>/", views.editSkill,name = 'edit-skill'),
    path("delete-skill/<str:pk>/", views.deleteSkill,name = 'delete-skill'),

    path("inbox/", views.inbox,name = 'inbox'),
    path("view-message/<str:pk>/", views.viewMessage,name = 'view-message'),
    path("send-message/<str:pk>/", views.sendMessage,name = 'send-message'),


]