from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('the_thoroton_society', views.the_thoroton_society, name='the_thoroton_society'),
    path('workshop_anecdote', views.workshop_anecdote, name='workshop_anecdote'),
    path('family_recollection', views.family_recollection, name='family_recollection'),
]
