from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        return ['home', 'articles', 'research', 'gallery', 'contact']

    def location(self, item):
        return reverse(item)
