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
    
    # página de detalhes para um único assunto
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # página para adicionar um novo assunto
    path('new_topic/', views.new_topic, name='new_topic'),

    # página para adicionar uma nova entrada url
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]