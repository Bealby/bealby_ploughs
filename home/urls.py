from django.contrib import admin
from django.urls import path
from . import views  # Assuming the views are in the current app (home)

# URL patterns
urlpatterns = [
    path('', views.index, name='home'),  # Comma added
]

