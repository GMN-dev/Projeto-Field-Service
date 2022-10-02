from importlib.metadata import requires
from django.contrib.messages import constants
from django.shortcuts import render, redirect, get_object_or_404
from .models import TblOperacao, TblSolicitacao
from django.contrib import messages
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def dashboard_incidentes(request):
    if request.method == "GET":
        # Dados para alimentar o input de nova Soliticação (operações) \ Dados para alimentar a tabela
        operacoesAtivas = TblOperacao.objects.values()
        solicitacoes = TblSolicitacao.objects.all()

        # =-=-=-=- Paginação =-=-=-=-=
        # Parâmetro minimo
        parametro_page = request.GET.get("page", '1')
        
        #Parâmetro maximo
        parametro_limite = request.GET.get('limit', '5')

        # Evitar páginas inexistentes
        if not ((parametro_limite.isdigit()) and (int(parametro_limite) > 0)):
            parametro_limite = 5

        # Definindo Paginação
        solicitacoes_paginator = Paginator(solicitacoes, parametro_limite)
        
        # Evitar paginas vazias ou que nao sejam numero inteiros
        try:
            page = solicitacoes_paginator.page(parametro_page)
        except (EmptyPage, PageNotAnInteger): 
            page = solicitacoes_paginator.page(1)

        # Renderizar página
        return render(request, 'cadastroEquipamento/html/dashboard.html', {'operacoes': operacoesAtivas, 'solicitacoes':page,})

    # Registrando variaveis    
    if request.method == "POST":
        chamado = request.POST.get('chamado')
        data_incidente = request.POST.get('data')
        informante = request.POST.get('gestor')
        operacao = request.POST.get("operacao")
        andar = request.POST.get('andar')
        periferico = request.POST.get("periferico")
        motivo = request.POST.get("motivo")
        observacao = request.POST.get("obs")
        
        # Criando objeto com variaveis criadas
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

            # Aumentando a quantidade de incidentes
            try:
                incremento = TblOperacao.objects.get(operacao = operacao)
                incremento.qtd_solicitacao += 1
                incremento.save()

                migracao.save()
                messages.add_message(request, messages.constants.SUCCESS, "Solicitação cadastrada!")
            except:
                messages.add_message(request, messages.constants.ERROR, "Algo deu errado, contate o administrador!")

        # Caso o chamado já exista
        except:
            messages.add_message(request, messages.constants.ERROR, "Verifique as informações cadastradas")
                    
        # renderizar página
        return redirect('/home/dashboard')



def incidente_details(request, chamado):
    # Pegando incidente especificado
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
        
        messages.add_message(request, constants.SUCCESS, "Incidente deletado")
        return redirect("/home/dashboard")

        # Caso erro:    
    except:
        messages.add_message(request, constants.ERROR ,"Erro ao excluir, contate o administrador")
        return redirect("/home/dashboard")



def operacoesAtivas(request):
    if request.method == 'GET':
        # Pegando todas as operações
        operacoes = TblOperacao.objects.all()
        return render(request, 'cadastroEquipamento/html/operacoes.html', {'operacoes':operacoes})

    if request.method == 'POST':
        #verificando a existencia do objeto no
        # Criando objeto
        try:
            operacaoObjeto = TblOperacao.objects.create(
                operacao = request.POST.get('operacao'),
                celula = request.POST.get('celula'),
                observacao = request.POST.get('obs')
            )
            # salvando objeto no banco
            operacaoObjeto.save()

            messages.add_message(request, constants.SUCCESS, 'Operação registrada!')

        except:
            # Caso erro
            messages.add_message(request, constants.ERROR, 'Essa operação ja existe!')
        
    
    return redirect('/home/operacoes/')    




def operacao_details(request, operacao):
    if request.method == 'GET':
        try:
            # pegando operação em específico    
            operacaoBanco = get_object_or_404(TblOperacao, operacao = operacao)
            # pegando incidentes desta operacao
            incidentes_operacao = TblSolicitacao.objects.filter(operacao = operacaoBanco.operacao)

            return render(request, "cadastroEquipamento/html/operacaoDetails.html" , {"operacao" : operacaoBanco, 'incidentes_operacao' : incidentes_operacao}) 
        
        # Caso Error
        except:
            messages.add_message(request, constants.ERROR,"Operação nao encontrada")
            return redirect("/home/operacoes/")



def excluirOperacao(request, operacao):
    try:
        # Pegando operacao do banco
        operacaoBanco = get_object_or_404(TblOperacao, operacao = operacao)
        # Deletando operacao
        operacaoBanco.delete()
        
        # mensagem de Sucesso
        messages.add_message(request, constants.SUCCESS, "Operação deletada!")

    except:
        # caso error
        messages.add_message(request, constants.ERROR, "Erro no sistema, contate o administrador!")

    return redirect('/home/operacoes/')