from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='query'),
    path('signup', views.signupHandle, name='signupHandle'),
    path('login', views.loginHandle, name='loginHandle'),
    path('logout', views.logoutHandle, name='logoutHandle')
    
]
