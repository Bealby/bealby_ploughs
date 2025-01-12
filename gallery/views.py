from django.shortcuts import render

# Create your views here.

def gallery_1(request):
    '''A view to return the index page'''
    
    return render(request, 'gallery/gallery_1.html')


def gallery_2(request):
    '''A view to return the index page'''
    
    return render(request, 'agallery/gallery_2.html')



def gallery_3(request):
    '''A view to return the index page'''
    
    return render(request, 'gallery/gallery_3.html')
