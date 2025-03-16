from django.contrib import admin
from .models import BealbyFamily
from .models import BrookHouse
from .models import BealbyWorkshop
from .models import BealbyPlough
from .models import BealbyForestCart
from .models import WorkshopTool


class BealbyFamilyAdmin(admin.ModelAdmin):

    list_display = (
        'image_title',
        'image',
        'image_description',
        'position',
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


class BealbyPloughAdmin(admin.ModelAdmin):

    list_display = (
        'image_title',
        'image',
        'image_description',
    )



class BealbyForestCartAdmin(admin.ModelAdmin):

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
admin.site.register(BealbyPlough, BealbyPloughAdmin)
admin.site.register(BealbyForestCart, BealbyForestCartAdmin)
admin.site.register(WorkshopTool, WorkshopToolAdmin)
