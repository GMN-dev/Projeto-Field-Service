from rest_framework import viewsets
from cadastroEquipamento.models import Solicitacao
from .serializers import SolicitacaoSerializer


class SolicitacaoView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Solicitacao.objects.all()
    serializer_class = SolicitacaoSerializer
    

    
    

