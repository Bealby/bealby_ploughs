from django.shortcuts import render
from .models import HomeAbout
from .models import HomeArticles
from .models import HomeResearch
from .models import HomeGallery


def index(request):
    ''' A view to return index page'''

    home_about = HomeAbout.objects.all()
    home_articles = HomeArticles.objects.all()
    home_research = HomeResearch.objects.all()
    home_gallery = HomeGallery.objects.all()

    context = {
        'home_about': home_about,
        'home_articles': home_articles,
        'home_research': home_research,
        'home_gallery': home_gallery,
    }

    return render(request, 'home/index.html', context)
