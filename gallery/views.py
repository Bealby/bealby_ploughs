from django.shortcuts import render
from .models import Gallery_1

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
    
    return render(request, 'gallery/gallery_2.html')



def gallery_3(request):
    '''A view to return the index page'''
    
    return render(request, 'gallery/gallery_3.html')
