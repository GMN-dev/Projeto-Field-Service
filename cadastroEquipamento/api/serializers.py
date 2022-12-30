from rest_framework import serializers


class MonthDashboardSerializer(serializers.Serializer):
    operacao = serializers.CharField(max_length = 15)
    qtd_chamados = serializers.IntegerField()


