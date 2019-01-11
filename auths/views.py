from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

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
        cpassword = request.POST['cpassword']
        print(email)
    return render(request, "auths/signup.html")

def logout_view(request):
    logout(request)
    return redirect('/')