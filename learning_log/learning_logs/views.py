from django.shortcuts import render
from .models import Topic

def index(request):
    """ A página inicial de Learning Log. """

    return render(request, 'learning_logs/index.html')

def topics(request):
    """ Mostra todos os tópicos. """

    # consulta-se o  banco de dados pedindo os objetos de Topic, ordenados com o atributo date_added
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')

    # contexto que será enviado ao template
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)