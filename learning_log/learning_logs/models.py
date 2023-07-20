from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """ Um assunto sobre o qual o usuário está aprendendo. """
    
    # texto armazenado no banco de dados
    text = models.CharField(max_length=200)
    
    # registrará a data e hora 
    date_added = models.DateTimeField(auto_now_add=True)

    # torando o atributo público
    public = models.fields.BooleanField(default=False)

    # relação entre user e cahve estrangeira 
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """ Devolve uma representação em string do modelo. """

        return self.text
    

class Entry(models.Model):
    """ Algo específico aprendido sobre um assunto. """
    
    # referência a outro registro do banco de dados
    # associa cada entrada a um assunto em específico
    # cada assunto recebe uma chave, um ID. Sendo este dado a conexão entre os BD's
    # precisei adicionar on_delete pois trata-se de uma versão nova do Django 2.0 
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    # não se quer restringir a quantiade de caracter
    text = models.TextField()

    # torando o atributo público
    public = models.fields.BooleanField(default=False)

    # apresenta em ordem que foram criadas e inserem um timestamp junto a cada entrada
    date_added = models.DateTimeField(auto_now_add=True)

    # precisa estar dentro de Entry
    class Meta:
        """ Armazena as informações extras para adminstrar um modelo. """

        # quando fro se referir a mais de uma entrada utilizar entries ao invés de Entrys
        verbose_name_plural = 'entries'

    def __str__(self):
        """ Devolve uma representação em string do modelo. """
        
        return self.text[:50] + "..."