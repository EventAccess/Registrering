from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def base_view(request): # This is the view function
    content = {
        'title': 'base view title',
        'content': 'This is the base view content',
        'registration': 'registration content',
    }
    return render(request, 'base.html', content)

def test_view(request): #this is the test view function
    return render (request, 'test.html', {'title': 'test view title', 'content': 'This is the test view content'})

# Create your views here. Class based views, we scrap the idea for now and go for function based views.


