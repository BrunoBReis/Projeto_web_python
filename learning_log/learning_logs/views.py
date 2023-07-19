from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """ A página inicial de Learning Log. """

    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """ Mostra todos os tópicos. """

    # consulta-se o  banco de dados pedindo os objetos de Topic, ordenados com o atributo date_added
    topics = Topic.objects.order_by('date_added')

    # contexto que será enviado ao template
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """ Mostra um único assunto e todas as suas entradas. """

    # topic armazena o assunto .get()
    topic = Topic.objects.get(id=topic_id)

    # os assuntos são recuperados e organizados
    entries = topic.entry_set.order_by('-date_added')

    # os assuntos são armazenados dentro do dicionário para o html
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """ Adiciona um novo assunto. """

    if request.method != 'POST':

        # nenhum dado submetido; cria um formulário em branco
        form = TopicForm()
    else:
        
        # dados do POST submetidos; processa os dados
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            
            return redirect('learning_logs:topics')

    # exibir um formulário em branco ou inválido
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """ Acrescenta uma nova entrada para um assunto em particular. """
    
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        
        # nenhum dado submetido; cria um formulário em branco
        form = EntryForm()
    else:

        # dados do POST submetidos; processa os dados
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()

            return redirect('learning_logs:topic', topic_id=topic_id)

    # exibir um formulário em branco ou inválido 
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """ Edita uma entrada existente. """

    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':

        # requisição inicial; preenche previamente o formulário com a entrada atual
        form = EntryForm(instance=entry)
    else:
        
        # Dados de POST submetidos; processa os dados
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()

            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)