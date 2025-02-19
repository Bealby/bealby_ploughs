from django.shortcuts import render
from .models import BealbyFamily
from .models import Gallery_2
from .models import Gallery_3


# Create your views here.

def bealby_family(request):
    '''A view to return the Bealby Family page'''

    bealby_families = BealbyFamily.objects.all()

    context = {
        'bealby_families': bealby_families,
    }

    return render(request, 'gallery/bealby_family.html', context)


def gallery_2(request):
    '''A view to return the Gallery 2 page'''

    galleries_2 = Gallery_2.objects.all()

    context = {
        'galleries_2': galleries_2,
    }

    return render(request, 'gallery/gallery_2.html', context)


def gallery_3(request):
    '''A view to return the Gallery 3 page'''

    galleries_3 = Gallery_3.objects.all()

    context = {
        'galleries_3': galleries_3,
    }

    return render(request, 'gallery/gallery_3.html', context)
