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
        'article_description_1',
        'article_image_alt_text_1',
        'article_title_2',
        'article_image_2',
        'article_description_2',
        'article_image_alt_text_2',
        'article_title_3',
        'article_image_3',
        'article_description_3',
        'article_image_alt_text_3',
    )


class HomeResearchAdmin(admin.ModelAdmin):
    
    list_display = (
        'research_title_1',
        'research_image_1',
        'research_description_1',
        'research_image_alt_text_1',
        'research_image_2',
        'research_description_2',
        'research_title_2',
        'research_image_alt_text_2',
        'research_image_3',
        'research_description_3',
        'research_title_3',
        'research_image_alt_text_3',
    )


class HomeGalleryAdmin(admin.ModelAdmin):
    
    list_display = (
        'gallery_title_1',
        'gallery_image_1',
        'gallery_description_1',
        'gallery_image_alt_text_1',
        'gallery_image_2',
        'gallery_title_2',
        'gallery_description_2',
        'gallery_image_alt_text_2',
        'gallery_image_3',
        'gallery_title_3',
        'gallery_description_3',
        'gallery_image_alt_text_3',
    )


admin.site.register(HomeAbout, HomeAboutAdmin)
admin.site.register(HomeArticles, HomeArticlesAdmin)
admin.site.register(HomeResearch, HomeResearchAdmin)
admin.site.register(HomeGallery, HomeGalleryAdmin)