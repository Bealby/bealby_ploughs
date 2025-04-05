from django.shortcuts import render
from .models import InvoiceJournal
from .models import BrookHouse
from .models import BealbyFamily


# Create your views here.

def invoice_journal(request):
    '''A view to return Invoice Journals'''

    invoice_journals = InvoiceJournal.objects.all()

    context = {
        'invoice_journals': invoice_journals,
    }

    return render(request, 'research/invoice_journals.html', context)


def brook_house(request):
    '''A view to return Brook House'''

    brook_houses = BrookHouse.objects.all()

    context = {
        'brook_houses': brook_houses,
    }

    return render(request, 'research/brook_house.html', context)


def bealby_family_A(request):
    '''A view to return the Bealby Family page'''

    bealby_families = BealbyFamily.objects.all()

    context = {
        'bealby_families': bealby_families,
    }

    return render(request, 'research/bealby_family_A.html', context)
