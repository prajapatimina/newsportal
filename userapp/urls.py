from django.urls import path
from django.contrib import admin

from .views import loginview

urlpatterns = [
    path('login/', loginview, name='login'),
#path('logout/', logoutview, name='logout')
]
