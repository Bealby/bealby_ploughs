from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        # List all your named URLs here
        return [
            # Home app
            'home',

            # Articles app
            'the_thoroton_society',
            'workshop_anecdote',
            'family_recollection',

            # Contact app
            'contact',

            # Home app additional pages
            'bealby_family',
            'brook_house',
            'bealby_workshop',
            'bealby_plough',
            'bealby_forest_cart',
            'workshop_tool',

            # Other app URLs (looks like invoice or research related)
            'invoice_journal',
            'brook_house_A',
            'bealby_family_A',
            
            # Add other named URLs here as needed
        ]

    def location(self, item):
        return reverse(item)