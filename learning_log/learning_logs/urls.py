""" Define padrões de URL para learning_logs. """

from django.urls import path
from . import views

# nome do aplicativo
app_name = "learning_logs"

# padrões de URL
urlpatterns = [
    # página inicial 
    path('', views.index, name='index'),
    # mostra todos os assuntos
    path('topics/', views.topics, name='topics'),
]