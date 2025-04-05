from django.shortcuts import render
from .models import WorkshopAnecdote
from .models import FamilyRecollection

# Create your views here.


def the_thoroton_society(request):
    '''A view to return The Thoroton Society page'''

    return render(request, 'articles/the_thoroton_society.html')


def workshop_anecdote(request):
    '''A view to return Workshop Anecdote page'''

    workshop_anecdotes = WorkshopAnecdote.objects.all()

    context = {
        'workshop_anecdotes': workshop_anecdotes,
    }

    return render(request, 'articles/workshop_anecdotes.html', context)


def family_recollection(request):
    '''A view to return Family recollection page'''

    family_recollections = FamilyRecollection.objects.all()

    context = {
        'family_recollections': family_recollections,
    }

    return render(request, 'articles/family_recollections.html', context)
