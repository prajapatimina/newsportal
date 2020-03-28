from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserModel


from django.contrib.auth import login, authenticate,logout

def loginview(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #do something after login
            next = request.GET.get('next')
            if next:
                return redirect('next')
            else:   
                return redirect('index')
        else:
            #there is not such user. send to login again. also give error
            return redirect('login')
    else:
        return render(request, 'userapp/login.html')

def registerview(request):
    if request.method == 'POST':
        errors ={}
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        status = request.POST.get('status')
        profile_pic = request.POST.get('profilepic')

        if password != password2:
            errors['password2'] ='Password and confirm passwod doesnot match'

     

        existinguser = User.objects.filter(username = username).first()
        if existinguser:
            errors['username'] = 'username already exists'
        if len(errors) > 0:
            return render(request, 'userapp/register.html', context=errors)
        else:


            user = User(username=username, password=password, email=email, first_name=fname, last_name=lname, is_active=True)
            user.save()
            usermodel = UserModel(auth=user, status=status, profile_picture=profile_pic)
            usermodel.save() 
            return redirect('index')
    else:

        return render(request, 'userapp/register.html')
    
def logoutview(request):
    logout(request)
    return redirect('index')