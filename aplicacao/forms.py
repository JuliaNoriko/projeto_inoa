from django import forms
from .models import Ativo, ParametroAtivo

class AtivoForm(forms.ModelForm):
    class Meta:
        model = Ativo
        fields = ['simbolo', 'descricao']

class ParametroAtivoForm(forms.ModelForm):
    class Meta:
        model = ParametroAtivo
        fields = ['ativo', 'limite_inferior', 'limite_superior', 'periodicidade']
