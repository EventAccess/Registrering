from django.contrib import admin
from django.urls import path, include
from frontend import views





urlpatterns = [
    path('__reload__/', include('django_browser_reload.urls')), #This is the URL for the browser reload app.    
    path('admin/', admin.site.urls), # This is the admin page for the project.
    path('', views.home, name='home'), #This is the home page for the project. for DJANGO which we will replace with nextjs, or i will in next PR.il just write a API up. 
]
