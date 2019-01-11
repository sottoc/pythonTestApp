from django.urls import path, include
from .views import *
urlpatterns = [
    path('account/', account_view, name="account"),
]