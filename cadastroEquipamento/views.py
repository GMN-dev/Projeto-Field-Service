from importlib.metadata import requires
from django.contrib.messages import constants
from django.shortcuts import render, redirect, get_object_or_404
from .models import TblOperacao, TblSolicitacao
from django.contrib import messages
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def cadastro(request):
    if request.method == "GET":
        # Dados para alimentar o input de nova Soliticação (operações) \ Dados para alimentar a tabela
        operacoesAtivas = TblOperacao.objects.values()
        solicitacoes = TblSolicitacao.objects.all()

        # =-=-=-=- Paginação =-=-=-=-=
        parametro_page = request.GET.get("page", '1')
        parametro_limite = request.GET.get('limit', '5')

        if not ((parametro_limite.isdigit()) and (int(parametro_limite) > 0)):
            parametro_limite = 5

        solicitacoes_paginator = Paginator(solicitacoes, parametro_limite)
        
        try:
            page = solicitacoes_paginator.page(parametro_page)
        except (EmptyPage, PageNotAnInteger): 
            page = solicitacoes_paginator.page(1)

        return render(request, 'cadastroEquipamento/html/dashboard.html', {'operacoes': operacoesAtivas, 'solicitacoes':page,})
    
    if request.method == "POST":
        chamado = request.POST.get('chamado')
        data_incidente = request.POST.get('data')
        informante = request.POST.get('gestor')
        operacao = request.POST.get("operacao")
        andar = request.POST.get('andar')
        periferico = request.POST.get("periferico")
        motivo = request.POST.get("motivo")
        observacao = request.POST.get("obs")
        
        try:     
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
                incremento = TblOperacao.objects.get(operacao = operacao)
                incremento.qtd_solicitacao += 1
                incremento.save()

                migracao.save()
                messages.add_message(request, messages.constants.SUCCESS, "Solicitação cadastrada!")
            except:
                messages.add_message(request, messages.constants.ERROR, "Algo deu errado, contate o administrador!")

        except:
            messages.add_message(request, messages.constants.ERROR, "Verifique as informações cadastradas")
                    
        
        return redirect('/cadastro/dashboard')



def incidente_details(request, chamado):
    incidente = get_object_or_404(TblSolicitacao, chamado = chamado)
    return render(request, "cadastroEquipamento/html/incidenteDetails.html", {'incidente':incidente}) 



def excluirSolicitacao(request, id_solicitacao):
    try:
        # pegando objeto do banco a ser excluido
        incidente = get_object_or_404(TblSolicitacao, id = id_solicitacao)
        # =-=-=-=-= excluir registro na quantidade de operações =-=-=-=-=-
        excluir_qtd_solicitacao = TblOperacao.objects.get(operacao = incidente.operacao)
        excluir_qtd_solicitacao.qtd_solicitacao -= 1
        excluir_qtd_solicitacao.save()
        # =-=-=-=-=-==-==--=-=-=-=-=-=
        
        # apagando incidente das solicitacoes
        incidente.delete()
        # mensagem de sucesso
        messages.add_message(request, constants.SUCCESS, "Incidente deletado")
        return redirect("/cadastro/dashboard")

        # Caso erro:    
    except:

        #mensagem de erro
        messages.add_message(request, constants.ERROR ,"Erro ao excluir, contate o administrador")
        return redirect("/cadastro/dashboard")



def configurarDashboard(request):
    if request.method == 'GET':
        return render(request, 'cadastroEquipamento/html/settings_dashboard.html')


def operacoesAtivas(request):
    if request.method == 'GET':
        operacoes = TblOperacao.objects.all()
        return render(request, 'cadastroEquipamento/html/operacoes.html', {'operacoes':operacoes})