from django.contrib import admin
from .models import Gallery_1


class Gallery_1Admin(admin.ModelAdmin):
    
    list_display = (
        'image',
        'image_title',
        'image_description',
    )


admin.site.register(Gallery_1, Gallery_1Admin)