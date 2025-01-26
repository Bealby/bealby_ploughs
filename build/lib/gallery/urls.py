from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('gallery_1', views.gallery_1, name='gallery_1'),
    path('gallery_2', views.gallery_2, name='gallery_2'),
    path('gallery_3', views.gallery_3, name='gallery_3'),
]
