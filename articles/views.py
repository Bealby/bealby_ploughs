from django.shortcuts import render
from .models import Article_2
from .models import Article_3

# Create your views here.


def articles_1(request):
    '''A view to return the Article 1 page'''

    return render(request, 'articles/article_1.html')


def articles_2(request):
    '''A view to return the Article 2 page'''

    articles_2 = Article_2.objects.all()

    context = {
        'articles_2': articles_2,
    }

    return render(request, 'articles/article_2.html', context)


def articles_3(request):
    '''A view to return the Article 3 page'''

    articles_3 = Article_3.objects.all()

    context = {
        'articles_3': articles_3,
    }

    return render(request, 'articles/article_3.html', context)
