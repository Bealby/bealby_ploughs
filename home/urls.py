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

# Function for serving robots.txt
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow:",
        "Sitemap: https://www.bealbyploughs.com/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

# Adding the robots.txt path
urlpatterns += [
    path("robots.txt", robots_txt),
]
