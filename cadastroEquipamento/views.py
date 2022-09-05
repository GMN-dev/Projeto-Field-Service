from django.contrib.messages import constants
from django.shortcuts import render, redirect, get_object_or_404
from .models import TblSolicitacao
from django.contrib import messages

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastroEquipamento/html/dashboard.html')
    if request.method == "POST":
        chamado = request.POST.get('chamado')
        data_incidente = request.POST.get('data')
        informante = request.POST.get('gestor')
        operacao = request.POST.get('operacao')
        andar = request.POST.get('andar')
        periferico = request.POST.get("periferico")
        motivo = request.POST.get("motivo")
        observacao = request.POST.get("obs")
        
        # try:
        migracao = TblSolicitacao.objects.create(
        chamado = chamado, 
        data_incidentes = data_incidente, 
        informante = informante,
        operacao = operacao,
        andar = andar,
        periferico = periferico,
        motivo_solicitacao = motivo,
        observacao = observacao)

        migracao.save()

        messages.add_message(request, messages.constants.SUCCESS, "Solicitação cadastrada!")
        
        return redirect('/cadastro/dashboard')

        # except:



def excluirSolicitacao(request, id_solicitacao):
    try:
        incidente = get_object_or_404(TblSolicitacao, id_incidentes = id_solicitacao)
        incidente.delete()
        messages.add_message(request, constants.SUCCESS, "Incidente deletado")
        return redirect("/cadastro/dashboard")
    except:
        messages.add_message(request, constants.ERROR ,"Erro ao excluir, contate o administrador")
        return redirect("/cadastro/dashboard")
