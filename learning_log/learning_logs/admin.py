from django.contrib import admin
from learning_logs.models import Topic, Entry

# administra o modelo pelo um site de administração
admin.site.register(Topic)

#
admin.site.register(Entry)

