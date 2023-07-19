from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """ Faz o cadastro de um novo usuário. """

    if request.method != 'POST':

        # exibe um formulário de cadastro em branco
        form = UserCreationForm()
    else:
        
        # processa o formulário preenchido
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()

            # faz login do usuário e o redicreciona para o página inicial
            login(request, new_user)
            return redirect('learning_logs:index')

    # exibe um formulário em branco ou inválido 
    context = {'form': form}
    return render(request, 'registration/register.html', context)