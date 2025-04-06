from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('invoice_journal', views.invoice_journal, name='invoice_journal'),
    path('brook_house_A', views.brook_house_A, name='brook_house_A'),
    path('bealby_family_A', views.bealby_family_A, name='bealby_family_A'),
]
