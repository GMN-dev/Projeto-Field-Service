from ..models import TblSolicitacao, TblOperacao
from rest_framework import serializers


class TblSolicitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblSolicitacao
        fields = ('id_incidentes', 'chamado', 'data_incidente', 'operacao', 'andar', 'informante', 'periferico', 'motivo_solicitacao', "observacao")


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model: TblOperacao
        fields = ('operacao', 'qtd_Solicitacao')
