from django.contrib import admin
from .models import HomeAbout
from .models import HomeArticles


class HomeAboutAdmin(admin.ModelAdmin):
    list_display = (
        'paragraph_1',
        'image_1',
        'image_1_description',
        'image_2',
        'image_2_description',
        'paragraph_2',
    )


class HomeArticlesAdmin(admin.ModelAdmin):
    list_display = (
        'image_1',
        'image_1_description',
        'image_2',
        'image_2_description',
        'image_3',
        'image_3_description',
    )


admin.site.register(HomeAbout, HomeAboutAdmin)
admin.site.register(HomeArticles, HomeArticlesAdmin)