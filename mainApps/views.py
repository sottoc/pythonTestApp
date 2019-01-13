from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.


def home_view(request):
    account_list = []
    users = User.objects.all()
    for user in users:
        account = Account.objects.filter(user=user).first()
        name = user.first_name
        email = user.email
        account_list.append([account, name, email])
    accounts = Account.objects.all()
    boxes = Box.objects.all()
    for obj in accounts:
        print(obj.amount)
    return render(request, "mainApps/home.html" , {
        'user' : request.user,
        'accounts' : accounts,
        'account_list' : account_list,
        'boxes' : boxes,
    })


@login_required
def account_view(request):
    info = None
    amount = None
    user = request.user
    account = Account.objects.filter(user=user).first()
    boxes = Box.objects.filter(account=account)
    if account:
        amount = account.amount
    if request.method == "POST":
        if request.POST['amount'] == '':
            info = "Please enter amount"
        else:
            amount = float(request.POST['amount'])
            account = Account()
            account.user = user
            account.amount = amount
            account.save()
            amount = amount
    return render(request, "mainApps/profile.html" ,{'amount':amount, 'info' : info, 'boxes': boxes, 'user' : request.user})

@login_required
def box_view(request):
    info_name = None
    info_price = None
    if request.method == 'POST':
        if request.POST['box-name'] == "":
            info_name = "Please enter box name"
        else:
            if request.POST['box-price'] == "":
                info_price = "Please enter box price"
            else:
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
    return render(request, "mainApps/box.html", {'user' : request.user, 'info_name':info_name, 'info_price': info_price})


