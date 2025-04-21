from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        return ['articles', 'research', 'gallery', 'contact' ]  # use your actual view names here

    def location(self, item):
        return reverse(item)