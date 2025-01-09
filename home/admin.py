from django.contrib import admin
from .models import HomeAbout


class HomeAboutAdmin(admin.ModelAdmin):
    list_display = (
        'text_1',
        'image_1',
        'image_1_description',
        'image_2',
        'image_1_description',
        'text_2',
    )

admin.site.register(HomeAbout, HomeAboutAdmin)