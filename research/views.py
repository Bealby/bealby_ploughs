from django.shortcuts import render
from .models import Research_1
from .models import Research_2

# Create your views here.

def research_1(request):
    ''' A view to return index page'''

    researches_1 = Research_1.objects.all()

    context = {
        'researches_1': researches_1,
    }
    
    return render(request, 'research/research_1.html', context)


def research_2(request):
    ''' A view to return index page'''

    researches_2 = Research_2.objects.all()

    context = {
        'researches_2': researches_2,
    }
    
    return render(request, 'research/research_2.html', context)


def research_3(request):
    ''' A view to return index page'''
    
    return render(request, 'research/research_3.html')