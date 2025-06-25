from django.contrib import admin
from .models import WorkshopAnecdote
from .models import FamilyRecollection


class WorkshopAnecdoteAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'article_image',
        'article_image',
        'author',
        'text',
    )


class FamilyRecollectionAdmin(admin.ModelAdmin):

    list_display = (
        'text_intro',
        'title',
        'article_image',
        'article_image',
        'author',
        'text',
    )


admin.site.register(WorkshopAnecdote, WorkshopAnecdoteAdmin)
admin.site.register(FamilyRecollection, FamilyRecollectionAdmin)
