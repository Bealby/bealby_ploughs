from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('invoice_journal', views.invoice_journal, name='invoice_journal'),
    path('brook_house', views.brook_house, name='brook_house'),
    path('bealby_family_A', views.bealby_family_A, name='bealby_family_A'),
]
