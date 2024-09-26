from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here. Class based views, we scrap the idea for now and go for function based views.
""" def base_view(request):
    return render(request, 'base.html')
def test_view(request):
    return render(request, 'test.html') """