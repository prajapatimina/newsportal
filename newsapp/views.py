from django.shortcuts import render,redirect
import datetime
from django.contrib.auth.decorators import login_required

from .models import PostModel, CategoryModel

from django.contrib.auth.decorators import login_required

def index(request):
    posts = PostModel.objects.all()[:10]
    categories = CategoryModel.objects.all()[:5]
    context = {
        'posts' : posts,
        'categories': categories,
        'featured_post': posts[0] if len(posts) > 0 else None
    }
    return render(request, 'newsapp/index.html', context)

def detail(request, id):
    post = PostModel.objects.filter(id=id).first()
    categories = CategoryModel.objects.all()[:5]
    context = {
        'post': post,
        'categories': categories
    }
    return render(request, 'newsapp/detail.html', context)

def categorynews(request, id):
    category = CategoryModel.objects.filter(id=id).first()
    if category:
        posts = PostModel.objects.filter(category=category)
        categories = CategoryModel.objects.all()[:5]
        context = {
            'posts': posts,
            'categories': categories,
            'featured_post' :posts[0] if len(posts) > 0 else None
        }
        return render(request, 'newsapp/index.html', context)
    else:
        return render(request, 'newsapp/error404.html')

@login_required
    
def add_post_view(request):
    categories = CategoryModel.objects.all()[:5]
    context={
        'categories':categories
    }

    return render(request, 'newsapp/add_post.html', context)

@login_required
def delete_post_view(request, id):
    post = PostModel.objects.filter(id=id).first()
    if post:
        logged_in_user_id = request.user.id
        post_user_id = post.posted_by.auth.id
        if logged_in_user_id == post_user_id:
            post.delete()
            #send user to index
            return redirect('index')
        else:
            return render(request, 'newsapp/error404.html')
    else:
        #there is no post with that id
        return render(request, 'newsapp/error404.html')