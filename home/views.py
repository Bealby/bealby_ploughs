from django.shortcuts import render
from .models import HomeAbout
from .models import HomeArticle
from .models import HomeResearch
from .models import HomeGallery


def index(request):
    ''' A view to return index page'''

    home_abouts = HomeAbout.objects.all()
    home_articles = HomeArticle.objects.all()
    home_research = HomeResearch.objects.all()
    home_gallery = HomeGallery.objects.all()

    context = {
        'home_abouts': home_abouts,
        'home_articles': home_articles,
        'home_research': home_research,
        'home_gallery': home_gallery,
    }

    return render(request, 'home/index.html', context)
