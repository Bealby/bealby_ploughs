"""bealby_ploughs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from bealby_ploughs.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('allauth.urls')),
    path('articles/', include('articles.urls')),
    path('research/', include('research.urls')),
    path('gallery/', include('gallery.urls')),
    path('contact/', include('contact.urls')),  
    path('tinymce/', include('tinymce.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# default: "Django Administration"
admin.site.site_header = 'Bealby Ploughs Website'
# default: "Site administration"
admin.site.index_title = 'Website Admin'
# default: "Django Bealby Plough Site Admin"
admin.site.site_title = 'HTML title from adminsitration'
