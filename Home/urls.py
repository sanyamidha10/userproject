from django.contrib import admin
from django.urls import path, include
from Home import views
urlpatterns = [
    path('',views.index,name="Home"),
    path('login',views.loginUser,name="login"),
    path('logout',views.logoutUser,name="logout")
    
]