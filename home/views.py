from django.shortcuts import render
from .models import HomeAbout


def index(request):
    ''' A view to return index page'''

    home_about = HomeAbout.objects.all()

    context = {
        'home_about': home_about,
    }

    return render(request, 'home/index.html', context)
