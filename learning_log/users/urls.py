""" Define padrões de URL para users. """

from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    # login quanto logout estão aqui 
    path('', include('django.contrib.auth.urls')),
]