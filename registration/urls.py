"""
URL configuration for registration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from frontend import views




urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")), #This is the URL for the browser reload app.    
    path('admin/', admin.site.urls), # This is the admin page for the project.
    path('', views.base_view, name='home'), #Root URL -> base.html
    path('test/', views.test_view, name='test'), #Test/placeholder URL
]