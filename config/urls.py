"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django_music import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.album_list, name='album_list'),
    path ('albums/<int:pk>/', views.album_detail, name= 'album_detail'),
    path('album/new', views.album_new, name='album_new'),
    path('albums/<int:pk>/edit/', views.album_edit, name='album_edit'),
    path('album/<pk>/remove/', views.album_remove, name='album_remove'),
]
