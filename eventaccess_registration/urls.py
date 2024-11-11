from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path(
        "", views.home, name="home"
    ),  # This is the home page for the project. for DJANGO which we will replace with nextjs, or i will in next PR.il just write a API up.
]