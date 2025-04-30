from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.conf import settings

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return [
            'home', 'the_thoroton_society', 'workshop_anecdote', 'family_recollection',
            'invoice_journal', 'brook_house_A', 'bealby_family_A', 'bealby_family',
            'brook_house', 'bealby_workshop', 'bealby_plough', 'bealby_forest_cart', 
            'workshop_tool'
        ]  # These are your URL names

    def location(self, item):
        return reverse(item)



