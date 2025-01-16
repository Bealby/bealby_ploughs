from django.contrib import admin
from .models import Article_2


class Article_2Admin(admin.ModelAdmin):
    
    list_display = (
        'title',
        'article_image',
        'article_image',
        'author',
        'text',
    )

admin.site.register(Article_2, Article_2Admin)