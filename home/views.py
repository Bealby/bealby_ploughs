from django.shortcuts import render
from .models import HomeAbout
from .models import HomeArticle
from .models import HomeResearch
from .models import HomeGallery


def index(request):
    ''' A view to return Home page'''

    home_abouts = HomeAbout.objects.all()
    home_articles = HomeArticle.objects.all()
    home_researches = HomeResearch.objects.all()
    home_galleries = HomeGallery.objects.all()

    context = {
        'home_abouts': home_abouts,
        'home_articles': home_articles,
        'home_researches': home_researches,
        'home_galleries': home_galleries,
    }

    return render(request, 'home/index.html', context)


def page_not_found(request, exception):
    # Log the URL that caused the 404 error (optional)
    print(f"Page not found: {request.path}")  # You can log this in your server logs too

    # Render the 404 page with the requested path passed to the template
    return render(request, '404.html', {'requested_url': request.path}, status=404)
