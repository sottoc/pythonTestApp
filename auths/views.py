from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
# Create your views here.

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            print("successfully login!")
            return redirect('/')
        else:
            print("Not authroized!")
    return render(request, "auths/login.html")


def signup_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = ""
        users = User.objects.filter(email__iexact=email).first()
        if users:
            return render(request, "auths/signup.html", {'error' : "This email is already existed!"})
        user = User()
        user.email = email
        user.set_password(password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        print(email)
        login(request, user)
        print("successfully login!")
        return redirect('/')
    return render(request, "auths/signup.html", {'error' : ""})

def logout_view(request):
    logout(request)
    return redirect('/')