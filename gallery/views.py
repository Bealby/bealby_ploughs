from django.shortcuts import render
from .models import Gallery_1
from .models import Gallery_2
from .models import Gallery_3

# Create your views here.

def gallery_1(request):
    ''' A view to return index page'''

    galleries_1 = Gallery_1.objects.all()

    context = {
        'galleries_1': galleries_1,
    }
    
    return render(request, 'gallery/gallery_1.html', context)


def gallery_2(request):
    '''A view to return the index page'''
    
    galleries_2 = Gallery_2.objects.all()

    context = {
        'galleries_2': galleries_2,
    }
    
    return render(request, 'gallery/gallery_2.html', context)



def gallery_3(request):
    '''A view to return the index page'''
    
    galleries_3 = Gallery_3.objects.all()

    context = {
        'galleries_3': galleries_3,
    }
    
    return render(request, 'gallery/gallery_3.html', context)
