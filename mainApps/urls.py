from django.urls import path, include
from .views import *
urlpatterns = [
    path('box/', box_view, name="box"),
    path('account/', account_view, name="account"),
    path('about/', about_view, name="about"),
]