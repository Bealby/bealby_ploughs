from django.shortcuts import render

# Create your views here.

def articles_1(request):
    '''A view to return the index page'''
    
    return render(request, 'articles/articles_1.html')


def articles_2(request):
    '''A view to return the index page'''
    
    return render(request, 'articles/articles_2.html')



def articles_3(request):
    '''A view to return the index page'''
    
    return render(request, 'articles/articles_3.html')
