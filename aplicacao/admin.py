from django.contrib import admin

from .models import Ativo, Cotacao

admin.site.register(Ativo)
admin.site.register(Cotacao)