from django.shortcuts import render
from .models import BealbyFamily
from .models import BrookHouse
from .models import BealbyWorkshop
from .models import BealbyPlough
from .models import BealbyForestCart
from .models import WorkshopTool


# Create your views here.

def bealby_family(request):
    '''A view to return the Bealby Family gallery page'''

    bealby_families = BealbyFamily.objects.all()

    context = {
        'bealby_families': bealby_families,
    }

    return render(request, 'gallery/bealby_family.html', context)


def brook_house(request):
    '''A view to return the Brook House gallery page'''

    brook_houses = BrookHouse.objects.all()

    context = {
        'brook_houses': brook_houses,
    }

    return render(request, 'gallery/brook_house.html', context)


def bealby_workshop(request):
    '''A view to return the Bealby Workshop gallery page'''

    bealby_workshops = BealbyWorkshop.objects.all()

    context = {
        'bealby_workshops': bealby_workshops,
    }

    return render(request, 'gallery/bealby_workshop.html', context)


def bealby_plough(request):
    '''A view to return the Bealby Plough gallery page'''

    bealby_ploughs = BealbyPlough.objects.all()

    context = {
        'bealby_ploughs': bealby_ploughs,
    }

    return render(request, 'gallery/bealby_ploughs.html', context)


def bealby_forest_cart(request):
    '''A view to return the Brook House gallery page'''

    bealby_forest_carts = BealbyForestCart.objects.all()

    context = {
        'bealby_forest_carts': bealby_forest_carts,
    }

    return render(request, 'gallery/bealby_forest_cart.html', context)


def workshop_tool(request):
    '''A view to return the Workshop Tools gallery page'''

    workshop_tools = WorkshopTool.objects.all()

    context = {
        'workshop_tools': workshop_tools,
    }

    return render(request, 'gallery/workshop_tools.html', context)


