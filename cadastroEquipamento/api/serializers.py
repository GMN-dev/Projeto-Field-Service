from ..models import TblSolicitacao, TblOperacao
from rest_framework import serializers


class TblSolicitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblSolicitacao
        fields = ('id', 'chamado', 'data_incidentes', 'operacao', 'andar', 'solicitante', 'periferico', 'motivo', "observacao")


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model: TblOperacao
        fields = ('operacao', 'qtd_Solicitacao')
