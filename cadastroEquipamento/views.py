from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Solicitacao
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
        migracao = Solicitacao.objects.create(
        chamado = chamado, 
        data_incidente = data_incidente, 
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
            
        

# def entrada(request):
#     return render(request, 'entrada.html')
        