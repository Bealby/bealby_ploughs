from django.contrib import admin
from .models import HomeAbout
from .models import HomeArticles
from .models import HomeResearch
from .models import HomeGallery


class HomeAboutAdmin(admin.ModelAdmin):
    
    list_display = (
        'about_paragraph_1',
        'about_image_1',
        'about_image_1_title',
        'about_image_2',
        'about_image_2_title',
        'about_paragraph_2',
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

class HomeResearchAdmin(admin.ModelAdmin):
    
    list_display = (
        'research_title_1',
        'research_image_1',
        'research_image_1_description',
        'research_image_2',
        'research_image_2_description',
        'research_title_2',
        'research_image_3',
        'research_image_3_description',
        'research_title_3',
    )


class HomeGalleryAdmin(admin.ModelAdmin):
    
    list_display = (
        'gallery_title_1',
        'gallery_image_1',
        'gallery_image_1_description',
        'gallery_image_2',
        'gallery_image_2_description',
        'gallery_title_2',
        'gallery_image_3',
        'gallery_image_3_description',
        'gallery_title_3',
    )


admin.site.register(HomeAbout, HomeAboutAdmin)
admin.site.register(HomeArticles, HomeArticlesAdmin)
admin.site.register(HomeResearch, HomeResearchAdmin)
admin.site.register(HomeGallery, HomeGalleryAdmin)