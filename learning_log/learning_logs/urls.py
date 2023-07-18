""" Define padrões de URL para learning_logs. """

from django.urls import path
from . import views

urlpatterns = [
    # página inicial 
    path('', views.index, name='index'),
]