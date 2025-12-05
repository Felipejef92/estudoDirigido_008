from django.contrib import admin
from .models import Unidade, Sala, Status, Bem

# Registrar os modelos no admin
admin.site.register(Unidade)
admin.site.register(Sala)
admin.site.register(Status)
admin.site.register(Bem)

