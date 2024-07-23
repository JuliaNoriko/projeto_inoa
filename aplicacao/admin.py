from django.contrib import admin

from .models import Ativo, ParametroAtivo, Cotacao

admin.site.register(Ativo)
admin.site.register(ParametroAtivo)
admin.site.register(Cotacao)