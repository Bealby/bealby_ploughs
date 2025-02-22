from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('bealby_family', views.bealby_family, name='bealby_family'),
    path('brook_house', views.brook_house, name='brook_house'),
    path('bealby_workshop', views.bealby_workshop, name='bealby_workshop'),
    path('workshop_tool', views.workshop_tool, name='workshop_tool'),
]
