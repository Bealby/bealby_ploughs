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
        'article_title_1',
        'article_image_1',
        'article_image_1_description',
        'article_image_2',
        'article_image_2_description',
        'article_title_2',
        'article_image_3',
        'article_image_3_description',
        'article_title_3',
    )


admin.site.register(HomeAbout, HomeAboutAdmin)
admin.site.register(HomeArticles, HomeArticlesAdmin)