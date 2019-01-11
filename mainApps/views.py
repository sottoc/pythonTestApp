from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.


def home_view(request):
    accounts = Account.objects.all()
    for obj in accounts:
        print(obj.amount)
    return render(request, "mainApps/home.html" , {
        'loggedin' : request.user.is_authenticated,
        'accounts' : accounts
    })


@login_required
def account_view(request):
    error = None
    if request.method == "POST":
        amount = float(request.POST['amount'])
        user = request.user
        account = Account.objects.all()
        if len(account) > 0:
            error = "Account is already existed."
        else:
            account.user = user
            account.amount = amount
            account.save()
    return render(request, "mainApps/profile.html" ,{'error' : error})

# @login_required
# def box_view(request):
#     if request.mothod == 'POST':
#

