from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=='POST':
        US=request.POST['us']
        PS=request.POST['fs']
        ls = request.POST['ls']
        email = request.POST['mail']
        password = request.POST['pas1']
        password1= request.POST['pas2']
        if password==password1:
            if User.objects.filter(username=US).exists():
                messages.info(request ,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email Taken")
            else:
                user=User.objects.create_user(username=US,password=password,first_name=PS,last_name=ls,email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return  redirect('register')
        return redirect('/')
    return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return  redirect('/')
        else:
            messages.info(request,"invalid")
            return redirect('login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return  redirect(request,'/')