from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.


def home_view(request):
    accounts = Account.objects.all()
    boxes = Box.objects.all()
    for obj in accounts:
        print(obj.amount)
    return render(request, "mainApps/home.html" , {
        'user' : request.user,
        'accounts' : accounts,
        'boxes' : boxes,
    })


@login_required
def account_view(request):
    error = None
    if request.method == "POST":
        amount = float(request.POST['amount'])
        user = request.user
        accounts = Account.objects.filter(user=user).first()
        if accounts:
            error = "Account is already existed."
        else:
            account = Account()
            account.user = user
            account.amount = amount
            account.save()
    return render(request, "mainApps/profile.html" ,{'error' : error, 'user' : request.user})

@login_required
def box_view(request):
    if request.method == 'POST':
        box_name = request.POST['box-name']
        box_price = float(request.POST['box-price'])
        user = request.user
        account = Account.objects.filter(user=user).first()
        box = Box()
        box.name = box_name
        box.price = box_price
        box.account = account
        box.save()
        print(box_name)
        print(box_price)
        return redirect('/')
    return render(request, "mainApps/box.html", {'user' : request.user})


