from django.contrib import admin
from django.urls import path
from . import views  # Assuming the views are in the current app (home)
from django.contrib.sitemaps.views import sitemap
from home.sitemaps import StaticViewSitemap  # Correct path to your sitemaps file
from django.http import HttpResponse

# Define sitemaps
sitemaps = {
    'static': StaticViewSitemap,
}

# URL patterns
urlpatterns = [
    path('', views.index, name='home'),  # Comma added
    path("sitemap.xml", sitemap, {'sitemaps': sitemaps}, name='sitemap'),  # This registers the sitemap route
]

