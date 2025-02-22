from django.contrib import admin
from .models import BealbyFamily
from .models import BrookHouse
from .models import BealbyWorkshop
from .models import WorkshopTool


class BealbyFamilyAdmin(admin.ModelAdmin):

    list_display = (
        'image_title',
        'image',
        'image_description',
    )


class BrookHouseAdmin(admin.ModelAdmin):

    list_display = (
        'image_title',
        'image',
        'image_description',
    )


class BealbyWorkshopAdmin(admin.ModelAdmin):

    list_display = (
        'image_title',
        'image',
        'image_description',
    )


class WorkshopToolAdmin(admin.ModelAdmin):

    list_display = (
        'image_title',
        'image',
        'image_description',
    )


admin.site.register(BealbyFamily, BealbyFamilyAdmin)
admin.site.register(BrookHouse, BrookHouseAdmin)
admin.site.register(BealbyWorkshop, BealbyWorkshopAdmin)
admin.site.register(WorkshopTool, WorkshopToolAdmin)
