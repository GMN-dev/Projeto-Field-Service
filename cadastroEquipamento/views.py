from django.contrib.messages import constants
from django.shortcuts import render, redirect, get_object_or_404
from .models import TblOperacao, TblSolicitacao, TblPeriferico
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.shortcuts import HttpResponse


# Create your views herekmkm  joao  .
def dashboard_incidentes(request):
    if request.method == "GET":
        # Dados para alimentar o input de nova Soliticação (operações) \ Dados para alimentar a tabela
        operacoesAtivas = TblOperacao.objects.values()
        solicitacoes = TblSolicitacao.objects.all()
        perifericos = TblPeriferico.objects.all()

        # =-=-=-=- Paginação =-=-=-=-=
        # Parâmetro minimo
        parametro_page = request.GET.get("page", '1')
        
        #Parâmetro maximo
        parametro_limite = request.GET.get('limit', '12')

        # Evitar páginas inexistentes
        if not ((parametro_limite.isdigit()) and (int(parametro_limite) > 0)):
            parametro_limite = 12

        # Definindo Paginação
        solicitacoes_paginator = Paginator(solicitacoes, parametro_limite)
        
        # Evitar paginas vazias ou que nao sejam numero inteiros
        try:
            page = solicitacoes_paginator.page(parametro_page)
        except (EmptyPage, PageNotAnInteger): 
            page = solicitacoes_paginator.page(1)

        # Renderizar página
        return render(request, 'cadastroEquipamento/html/dashboard.html', {'operacoes': operacoesAtivas, 'solicitacoes':page, 'perifericos':perifericos})

    # Registrando variaveis    
    if request.method == "POST":
        # if request.POST.get("sla") == "on":
        #     sla = True
        # else:
        #     sla = False

        chamado = request.POST.get('chamado')
        data_incidente = request.POST.get('data')
        informante = request.POST.get('gestor')
        operacao = request.POST.get("operacao")
        andar = request.POST.get('andar')
        periferico = request.POST.get("periferico")
        motivo = request.POST.get("motivo")
        observacao = request.POST.get("obs")
        site = request.POST.get("site")
        pas = request.POST.get('PAS')
        if request.POST.get("sla") ==  "on":
            sla = True
        else:
            sla = False
        
        # Pegando dados de tabelas que nao sao a solicitacoes
        instanciaPeriferico = TblPeriferico.objects.get(tipo = periferico)
        instanciaOperacao = TblOperacao.objects.get(operacao = operacao)

        try:     
            migracao = TblSolicitacao.objects.create(
            chamado = chamado, 
            data_incidentes = data_incidente, 
            solicitante = informante,
            operacao = instanciaOperacao,
            andar = andar,
            periferico = instanciaPeriferico,
            motivo = motivo,
            observacao = observacao,
            pas = pas,
            site = site,
            sla = sla
            )

            # Aumentando a quantidade de incidentes
            try:
                instanciaOperacao.qtd_solicitacao += 1
                instanciaOperacao.save()

                try:
                    instanciaPeriferico.qtd_periferico += 1
                    instanciaPeriferico.save()
                except:
                    messages.add_message(request, messages.constants.SUCCESS, "Solicitação nao contabilizou periferico!")

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
    incidente_antigo = get_object_or_404(TblSolicitacao, chamado = chamado)
    perifericos = TblPeriferico.objects.all()
    operacoes = TblOperacao.objects.all()

    if request.method == "GET":
        return render(request, "cadastroEquipamento/html/incidenteDetails.html", {'incidente':incidente, "perifericos":perifericos, "operacoes":operacoes, "motivos":TblSolicitacao.MOTIVO_CHOICES})
    
    if request.method == "POST":
        try:
            chamado = request.POST.get('chamado')
            informante = request.POST.get('gestor')
            operacao = request.POST.get("operacao")
            andar = request.POST.get('andar')
            periferico = request.POST.get("periferico")
            motivo = request.POST.get("motivo")
            observacao = request.POST.get("obs")
            site = request.POST.get("site")
            pas = request.POST.get('PAS')
            if request.POST.get("sla") ==  "on":
                sla = True
            else:
                sla = False

            instanciaPerifericoInput = TblPeriferico.objects.get(tipo = periferico)
            instanciaOperacaoInput = TblOperacao.objects.get(operacao = operacao)

            
            if instanciaOperacaoInput.operacao != incidente.operacao.operacao:
                instanciaOperacaoVelha = TblOperacao.objects.get(operacao = incidente.operacao.operacao) 

                instanciaOperacaoInput.qtd_solicitacao += 1
                instanciaOperacaoVelha.qtd_solicitacao -= 1                                    

                instanciaOperacaoInput.save()
                instanciaOperacaoVelha.save()

            if instanciaPerifericoInput.tipo != incidente.periferico.tipo:
                instanciaPerifericoVelha = TblPeriferico.objects.get(tipo = incidente.periferico.tipo)

                instanciaPerifericoInput.qtd_periferico += 1
                instanciaPerifericoVelha.qtd_periferico -= 1

                instanciaPerifericoInput.save()
                instanciaPerifericoVelha.save()

            incidente.chamado = chamado
            incidente.sla = sla
            incidente.solicitante = informante
            incidente.site = site
            incidente.operacao = instanciaOperacaoInput
            incidente.andar = andar
            incidente.periferico = instanciaPerifericoInput
            incidente.motivo = motivo
            incidente.observacao = observacao
            incidente.pas = pas
            
            incidente.save()
            messages.add_message(request, messages.constants.SUCCESS, "Incidente atualizado!")
        
        except:
            messages.add_message(request, messages.constants.ERROR, "Algo deu errado, confira os dados!")
         
        return redirect(incidente)


def excluirSolicitacao(request, id_solicitacao):
    try:
        # pegando objeto do banco a ser excluido
        incidente = get_object_or_404(TblSolicitacao, id = id_solicitacao)
        # =-=-=-=-= excluir registro na quantidade de operações =-=-=-=-=-
        excluir_qtd_solicitacao = TblOperacao.objects.get(operacao = incidente.operacao)
        excluir_qtd_solicitacao.qtd_solicitacao -= 1
        excluir_qtd_solicitacao.save()
        # =-=-=-=-=-==-==--=-=-=-=-=-=-=-
        
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


def operacao_details(request, pk):
    if request.method == 'GET':
        try:
            # pegando operação em específico    
            operacaoBanco = get_object_or_404(TblOperacao, pk = pk)
            # pegando incidentes desta operacao
            incidentes_operacao = TblSolicitacao.objects.filter(operacao = TblOperacao.objects.get(operacao = operacaoBanco.operacao))

            # =-=-=-=- Paginação =-=-=-=-=
            # Parâmetro minimo
            parametro_page = request.GET.get("page", '1')
            
            #Parâmetro maximo
            parametro_limite = request.GET.get('limit', '12')

            # Evitar páginas inexistentes
            if not ((parametro_limite.isdigit()) and (int(parametro_limite) > 0)):
                parametro_limite = 12

            # Definindo Paginação
            solicitacoes_paginator = Paginator(incidentes_operacao, parametro_limite)
            
            # Evitar paginas vazias ou que nao sejam numero inteiros
            try:
                page = solicitacoes_paginator.page(parametro_page)
            except (EmptyPage, PageNotAnInteger): 
                page = solicitacoes_paginator.page(1)

            
            return render(request, "cadastroEquipamento/html/operacaoDetails.html" , {"operacao" : operacaoBanco, 'solicitacoes' : page}) 
         
        # Caso Erro
        except:
            messages.add_message(request, constants.ERROR,"Operação não encontrada.")
            return redirect("/home/operacoes/")
    

    if request.method == 'POST':
        try:
            # pegando instancia do banco
            instanciaBanco = get_object_or_404(TblOperacao, pk = pk)

            # pegando informações do POST
            requestOperacao = request.POST.get('operacao')
            requestCel = request.POST.get('celula')
            requestObservacao = request.POST.get('obs')

            # atualizando instancia
            instanciaBanco.operacao = requestOperacao
            instanciaBanco.celula = requestCel
            instanciaBanco.observacao = requestObservacao
            instanciaBanco.save()

            # Mensagem de sucesso
            messages.add_message(request, constants.SUCCESS, "Alteração realizada com sucesso!")

        except:
            messages.add_message(request, constants.ERROR, "Essa operação já existe!")
        
        return redirect(instanciaBanco)
        


def excluirOperacao(request, operacao):
    try:
        # Pegando operacao do banco
        operacaoBanco = TblOperacao.objects.get(operacao = operacao)
        
        # mensagem de Sucesso
        messages.add_message(request, constants.SUCCESS, "Operação deletada!")
        
        operacaoBanco.delete()
         
    except:
        # caso error
        messages.add_message(request, constants.ERROR, "Erro no sistema, contate o administrador!")

    return redirect('/home/operacoes/')

def perifericos(request):
    return render(request, 'cadastroEquipamento/html/perifericos.html')
