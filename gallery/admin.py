from django.contrib import admin
from .models import Gallery_1
from .models import Gallery_2
from .models import Gallery_3


class Gallery_1Admin(admin.ModelAdmin):

    list_display = (
        'image_title',
        'image',
        'image_description',
    )


class Gallery_2Admin(admin.ModelAdmin):

    list_display = (
        'image_title',
        'image',
        'image_description',
    )


class Gallery_3Admin(admin.ModelAdmin):

    list_display = (
        'image_title',
        'image',
        'image_description',
    )


admin.site.register(Gallery_1, Gallery_1Admin)
admin.site.register(Gallery_2, Gallery_2Admin)
admin.site.register(Gallery_3, Gallery_3Admin)
