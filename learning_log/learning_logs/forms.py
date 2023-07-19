from django import forms
from .models import Topic, Entry   

class TopicForm(forms.ModelForm):
    
    class Meta:
        """ Modelo de formulário que o usuário irá preencher. """

        # herdando as características de Topic
        model = Topic

        # selecionando apenas o texto de Topic
        fields = ['text']

        # espeficando um rótulo vazio de texto
        labels = {'text': ''}

class EntryForm(forms.ModelForm):

    class Meta:
    
        # herda as características de Entry
        model = Entry

        # selecioando apenas o texto de Entry
        fields = ['text']

        # espeficando um rótulo vazio de texto
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}