from django.shortcuts import render, redirect
from .forms import AtivoForm, ParametroAtivoForm
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



#Pagina para colocar os parametros dos ativos, como limite superior, limite inferior e periodicidade de cada ativo 
def adicionar_parametro(request):

    if request.method == 'POST':
        form = ParametroAtivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ParametroAtivoForm
    return render(request, 'parametros_preco.html', {'form': form})



#Pagina para acompanhar as cotações de cada ação e avisar quando houver chance de compra/venda de ações
def listar_cotacoes(request):
    
    cotacoes = Cotacao.objects.all()

    return render(request, 'cotacoes.html', {'cotacoes': cotacoes})
