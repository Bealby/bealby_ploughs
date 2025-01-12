from django.shortcuts import render

# Create your views here.

def research_1(request):
    '''A view to return the index page'''
    
    return render(request, 'research/research_1.html')


def research_2(request):
    '''A view to return the index page'''
    
    return render(request, 'research/research_2.html')


def research_3(request):
    '''A view to return the index page'''
    
    return render(request, 'research/research_3.html')