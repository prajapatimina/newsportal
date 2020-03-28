from django.urls import path
from django.contrib import admin

from .views import loginview,registerview, logoutview

urlpatterns = [
    path('login/', loginview, name='login'),
    path('register/', registerview, name='register'),
    path('logout/', logoutview, name='logout')
]
