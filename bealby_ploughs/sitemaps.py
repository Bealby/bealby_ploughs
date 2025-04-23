# from django.contrib.sitemaps import Sitemap
#from django.urls import reverse

#class StaticViewSitemap(Sitemap):
#    priority = 1.0
#    changefreq = 'monthly'

#    def items(self):
#        return ['the_thoroton_society', 'workshop_anecdote', 'family_recollection', 'bealby_family', 'brook_house', 'bealby_workshop', 'bealby_plough', 'bealby_forest_cart', 'workshop_tool', 'home', 'invoice_journal', 'brook_house_A', 'bealby_family_A']  # use your actual view names here
#
#    def location(self, item):
#        return reverse(item)