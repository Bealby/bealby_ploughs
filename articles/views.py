from django.shortcuts import render
from .models import Article_2

# Create your views here.

def articles_1(request):
    '''A view to return the index page'''
    
    return render(request, 'articles/articles_1.html')


def articles_2(request):
    ''' A view to return index page'''

    articles_2 = Article_2.objects.all()

    context = {
        'articles_2': articles_2,
    }
    
    return render(request, 'articles/articles_2.html', context)



def articles_3(request):
    '''A view to return the index page'''
    
    return render(request, 'articles/articles_3.html')
