from rest_framework import viewsets
from cadastroEquipamento.models import TblSolicitacao, TblOperacao
from .serializers import TblSolicitacaoSerializer, MonthDashboardSerializer
from rest_framework.response import Response
from datetime import date


class TblSolicitacaoView(viewsets.ModelViewSet):
    queryset = TblSolicitacao.objects.all()
    serializer_class = TblSolicitacaoSerializer


class DashboardViewMonth(viewsets.ViewSet):
    
    def list(self, request):
        class DataObjectList():
            def __init__(self, op, qtd):
                self.operacao = op
                self.qtd_chamados = qtd

        data_to_dashboard = []

        for i in TblOperacao.objects.all():
            data_object = DataObjectList(i.operacao, len(i.incidentes_ativos.filter(data_incidentes__month = date.today().month) ))
            data_to_dashboard.append(data_object)
        
        serializer = MonthDashboardSerializer(data_to_dashboard, many = True)
        return Response(serializer.data)


        