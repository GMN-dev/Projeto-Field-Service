from rest_framework import viewsets
from cadastroEquipamento.models import TblSolicitacao, TblOperacao
from .serializers import TblSolicitacaoSerializer, DashboardSerializer

class DashboardView(viewsets.ModelViewSet):
    queryset = TblOperacao.objects.all()
    serializer_class = DashboardSerializer
    

class TblSolicitacaoView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TblSolicitacao.objects.all()
    serializer_class = TblSolicitacaoSerializer




