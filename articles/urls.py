from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('articles_1', views.articles_1, name='articles_1'),
    path('articles_2', views.articles_2, name='articles_2'),
    path('articles_3', views.articles_3, name='articles_3'),
]
