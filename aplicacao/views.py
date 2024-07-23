from django.shortcuts import render, redirect, get_object_or_404
from .forms import AtivoForm
from .models import Cotacao, Ativo

#Pagina principal
def home(request):
    return render(request, 'index.html')


#Pagina com formulário para adicionar as informações dos ativos que devem ser verificados
def adicionar_ativo(request):

    if request.method == 'POST':
        form = AtivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AtivoForm()

    return render(request, 'ativos.html', {'form': form})

def listar_cotacoes(request):
    ativos = Ativo.objects.all()
    cotacao = None
    ativo_selecionado = None

    if request.method == 'POST':
        simb_ativo = request.POST.get('simb_ativo')
        try:
            ativo_selecionado = Ativo.objects.get(simbolo=simb_ativo)
        except Ativo.DoesNotExist:
            ativo_selecionado = None

        if ativo_selecionado:
            cotacao = Cotacao.objects.filter(ativo=ativo_selecionado).order_by('-data_hora').first()
        else:
            cotacao = None
    
    return render(request, 'cotacoes.html', {
        'ativos': ativos,
        'cotacao': cotacao,
        'ativo_selecionado': ativo_selecionado
    })


#Pagina para acompanhar as cotações de cada ação e avisar quando houver chance de compra/venda de ações
def informacoes_ativos(request):
    
    ativos = Ativo.objects.all()

    return render(request, 'informacoes_ativos.html', {'ativos': ativos})
