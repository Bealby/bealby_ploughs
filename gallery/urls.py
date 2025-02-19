from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('bealby_family', views.bealby_family, name='bealby_family'),
    path('gallery_2', views.gallery_2, name='gallery_2'),
    path('gallery_3', views.gallery_3, name='gallery_3'),
]
