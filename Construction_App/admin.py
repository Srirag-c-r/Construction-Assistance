from django.contrib import admin

# Register your models here.
from django.urls import path

from Construction_App.admin_views import IndexView

urlpatterns = [

    path('',IndexView.as_view()),



]

def urls():
    return urlpatterns, 'admin','admin'