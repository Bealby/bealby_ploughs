from django.shortcuts import render
from .models import HomeAbout
from .models import HomeArticles


def index(request):
    ''' A view to return index page'''

    home_about = HomeAbout.objects.all()
    home_articles = HomeArticles.objects.all()

    context = {
        'home_about': home_about,
        'home_articles': home_articles,
    }

    return render(request, 'home/index.html', context)
