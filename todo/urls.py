from django.urls import path
from . import views

urlpatterns = [

    path('register', views.register, name="register"),

    path('my-login', views.my_login, name="my-login"),

    path('',views.home, name=""),

    path('dashboard', views.dashboard, name="dashboard"),

    path('profile-manage', views.profile_manage, name = "profile-manage"),

    path('create-task', views.createTask, name= "create-task"),

    path('view-tasks', views.viewTask, name="view-tasks"),

    path('update-task/<str:pk>/', views.updateTask, name= "update-task"),

    path('delete-task/<str:pk>/', views.deleteTask, name= "delete-task"),

    path('logout', views.user_Logout, name= "logout"),

    path('my-view/', views.my_view, name='my_view'),

    

]
