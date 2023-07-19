from django.shortcuts import render
from .models import Topic

def index(request):
    """ A página inicial de Learning Log. """

    return render(request, 'learning_logs/index.html')

def topics(request):
    """ Mostra todos os tópicos. """

    # consulta-se o  banco de dados pedindo os objetos de Topic, ordenados com o atributo date_added
    topics = Topic.objects.order_by('date_added')

    # contexto que será enviado ao template
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """ Mostra um único assunto e todas as suas entradas. """

    # topic armazena o assunto .get()
    topic = Topic.objects.get(id=topic_id)

    # os assuntos são recuperados e organizados
    entries = topic.entry_set.order_by('-date_added')

    # os assuntos são armazenados dentro do dicionário para o html
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)