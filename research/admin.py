from django.contrib import admin
from .models import InvoiceJournal
from .models import BrookHouse
from .models import BealbyFamily

class InvoiceJournalAdmin(admin.ModelAdmin):

    list_display = (
        'text',
        'image_1',
        'image_title_1',
        'image_description_1',
        'image_2',
        'image_title_2',
        'image_description_2',
    )


class BrookHouseAdmin(admin.ModelAdmin):

    list_display = (
        'text',
        'image_1',
        'image_title_1',
        'image_description_1',
        'image_2',
        'image_title_2',
        'image_description_2',
    )


class BealbyFamilyAdmin(admin.ModelAdmin):

    list_display = (
        'main_header',
        'authur',
        'sub_header_1',
        'paragraph_1',
        'sub_header_2',
        'paragraph_2',
        'sub_header_3',
        'paragraph_3',
    )


admin.site.register(InvoiceJournal, InvoiceJournalAdmin)
admin.site.register(BrookHouse, BrookHouseAdmin)
admin.site.register(BealbyFamily, BealbyFamilyAdmin)