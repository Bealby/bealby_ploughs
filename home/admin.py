from django.contrib import admin
from .models import HomeAbout


class HomeAboutAdmin(admin.ModelAdmin):
    list_display = (
        'text_1',
        'image_1',
        'image_2',
        'text_2',
    )

admin.site.register(HomeAbout, HomeAboutAdmin)