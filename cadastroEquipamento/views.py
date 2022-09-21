from django.contrib.messages import constants
from django.shortcuts import render, redirect, get_object_or_404
from .models import TblOperacao, TblSolicitacao
from django.contrib import messages
from django.http import HttpResponse
from django.core.paginator import Paginator



# Create your views here.
def cadastro(request):
    if request.method == "GET":
        # Dados para alimentar o input de nova Soliticação (operações) \ Dados para alimentar a tabela
        operacoesAtivas = TblOperacao.objects.values()
        solicitacoes = TblSolicitacao.objects.all()
        
        # =-=-=-=- Paginação =-=-=-=-=
        parametro_page = request.GET.get("page", '1')
        parametro_limite = request.GET.get('limit', '25')
        
        solicitacoes_paginator = Paginator(solicitacoes, parametro_limite)
        page = solicitacoes_paginator.page(parametro_page)

        return render(request, 'cadastroEquipamento/html/dashboard.html', {'operacoes': operacoesAtivas, 'solicitacoes':page})
    
    if request.method == "POST":
        chamado = request.POST.get('chamado')
        data_incidente = request.POST.get('data')
        informante = request.POST.get('gestor')
        operacao = request.POST.get("operacao")
        andar = request.POST.get('andar')
        periferico = request.POST.get("periferico")
        motivo = request.POST.get("motivo")
        observacao = request.POST.get("obs")
        
        migracao = TblSolicitacao.objects.create(
        chamado = chamado, 
        data_incidentes = data_incidente, 
        solicitante = informante,
        operacao = operacao,
        andar = andar,
        periferico = periferico,
        motivo = motivo,
        observacao = observacao)

        try:
            migracao.save()
            messages.add_message(request, messages.constants.SUCCESS, "Solicitação cadastrada!")
            return redirect('/cadastro/dashboard')
        except:
            messages.add_message(request, messages.constants.ERROR, "Algo deu errado, contate o administrador!")
            return redirect('/cadastro/dashboard')




def excluirSolicitacao(request, id_solicitacao):
    try:
        incidente = get_object_or_404(TblSolicitacao, id_incidentes = id_solicitacao)
        incidente.delete()
        messages.add_message(request, constants.SUCCESS, "Incidente deletado")
        return redirect("/cadastro/dashboard")
    
    except:
        messages.add_message(request, constants.ERROR ,"Erro ao excluir, contate o administrador")
        return redirect("/cadastro/dashboard")
