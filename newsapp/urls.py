from django.urls import path
from django.contrib import admin

from .views import index, detail, categorynews,  add_post_view, delete_post_view, edit_post_view,search_view,add_comments_view

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:id>/', detail, name='detail'),
    path('topic/<int:id>/', categorynews, name='topic'),
    path('add_post/', add_post_view, name='add_post'),
    path('delete_post/<int:id>', delete_post_view, name='delete_post'),
    path('edit_post/<int:id>', edit_post_view, name='edit_post'),
    path('search/',search_view, name='search'),
    path('add_comments/<int:id>',add_comments_view, name='addcomment')
   
]
