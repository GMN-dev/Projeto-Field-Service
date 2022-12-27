from ..models import TblSolicitacao, TblOperacao
from rest_framework import serializers


class TblSolicitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblSolicitacao
        fields = ('id', 'chamado', 'data_incidentes', 'operacao', 'andar', 'solicitante', 'periferico', 'motivo', "observacao")
        

class MonthDashboardSerializer(serializers.Serializer):
    operacao = serializers.CharField(max_length = 15)
    qtd_chamados = serializers.IntegerField()


