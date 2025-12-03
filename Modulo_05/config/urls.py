from django.contrib import admin 
from django.urls import path, include 

urlpatterns = [ 
# Admin do Django 
    path('admin/', admin.site.urls), 
# URLs do app core (prefixo: /api/) 
    path('api/', include('core.urls')), 
]