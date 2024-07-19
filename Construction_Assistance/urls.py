"""Construction_Assistance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Construction_App import admin_urls, worker_urls, contractor_urls
from Construction_App import views
from Construction_App.views import Index, Login, Contractor_Reg, Worker_Reg

urlpatterns = [
    path('admin/', admin_urls.urls()),
    path('worker/',worker_urls.urls()),
    path('contractor/',contractor_urls.urls()),
    path('',Index.as_view()),
    path('activate/<str:uidb64>/<str:token>/',views.activate_account, name='activate'),
    path('reset_password/', views.reset_password_view, name='reset_password'),

    path('reset-password-confirm/<str:uidb64>/<str:token>/', views.reset_password_confirm_view, name='reset_password_confirm'),


    path('login',Login.as_view(),name='login'),
    path('Contractor_Reg/',Contractor_Reg.as_view(),name='Contractor_Reg/'),
    path('Worker_Reg/',Worker_Reg.as_view(),name='Worker_Reg/')
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)