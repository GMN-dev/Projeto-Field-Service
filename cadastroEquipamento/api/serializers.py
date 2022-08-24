from ..models import Solicitacao
from rest_framework import serializers


class SolicitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitacao
        fields = ('id_incidentes', 'chamado', 'data_incidente', 'operacao', 'andar', 'informante', 'periferico', 'motivo_solicitacao')