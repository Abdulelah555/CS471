"""
URL configuration for bookwebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('tasks/', views.tasks, name='tasks'),
    path('task/<int:tId>/', views.task, name='task'),
    path('create/', views.create, name='create'),
    path('edit/<int:tId>/', views.edit, name='edit'),
    path('delete/<int:tId>/', views.delete, name='delete'),
    path('createchecklist/<int:tId>/', views.createchecklist, name='createchecklist'),
    path('editchecklist/<int:tId>/<int:cId>/', views.editchecklist, name='editchecklist'),
    path('deletechecklist/<int:tId>/<int:cId>/', views.delete_checklist, name='delete_checklist'),
]
