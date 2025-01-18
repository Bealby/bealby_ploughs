from django.contrib import admin
from .models import Research_1
from .models import Research_2


class Research_1Admin(admin.ModelAdmin):
    
    list_display = (
        'text',
        'image_1',
        'image_title_1',
        'image_description_1',
        'image_2',
        'image_title_2',
        'image_description_2',
    )


class Research_2Admin(admin.ModelAdmin):
    
    list_display = (
        'text',
        'image_1',
        'image_title_1',
        'image_description_1',
        'image_2',
        'image_title_2',
        'image_description_2',
    )


admin.site.register(Research_1, Research_1Admin)
admin.site.register(Research_2, Research_2Admin)