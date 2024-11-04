from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def home(request):
    return render(request, "base.html")
