from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('research_1', views.research_1, name='research_1'),
    path('research_2', views.research_2, name='research_2'),
    path('research_3', views.research_2, name='research_3'),
]