"""siteToWork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from task_app.views import index, AddProfession, DelProfession, ModifyProfession

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('add_prof/', AddProfession.as_view(), name='add_prof'),
    path('del_prof/<str:prof_pk>/', DelProfession.as_view(), name='del_prof'),
    path('modify_prof/<str:prof_data>/', ModifyProfession.as_view(), name='modify_prof'),
]
