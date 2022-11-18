# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse


class TblOperacao(models.Model):
    operacao = models.CharField(unique=True, max_length=15)
    celula = models.IntegerField(default=0)
    qtd_solicitacao = models.IntegerField(blank=True, default=0)
    observacao = models.TextField()

    class Meta:
        managed = True
        db_table = 'tbl_operacao'
    
    def __str__(self):
        return self.operacao

    def get_absolute_url(self):
            return reverse("operacao_details", kwargs={'pk':self.pk})



class TblSolicitacao(models.Model):
    MOTIVO_CHOICES = (
        ("extravio","Extravio - Retirada indevida"),
        ("adicao","Adição Novo"),
        ("quebra","Quebra - Por Desgaste"),
        ("quebra_mal_uso","Quebra - Mal Uso"),
        ("troca","Troca")
    )

    chamado = models.CharField(max_length=7, unique=True)
    sla = models.BooleanField(default=False)
    data_incidentes = models.DateField(auto_now_add=True)
    solicitante = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    operacao = models.ForeignKey("TblOperacao", on_delete=models.PROTECT , related_name="incidentes_ativos")
    andar = models.CharField(max_length=10)
    periferico = models.ForeignKey("TblPeriferico", on_delete=models.PROTECT, related_name="perifericos")
    motivo = models.CharField(max_length=50, choices=MOTIVO_CHOICES, blank=False, null=False)
    observacao = models.TextField(max_length=50)
    pas = models.TextField(max_length=30)

    class Meta:
        managed = True
        db_table = 'tbl_solicitacao'

    def __str__(self) :
        return self.chamado

    def get_absolute_url(self):
        return reverse("incidente_details", kwargs={'chamado': self.chamado})



class TblPeriferico(models.Model):
    tipo = models.CharField(max_length=50)
    qtd_periferico = models.IntegerField(blank=True, default=0)

    class Meta:
        managed = True
        db_table = "tbl_periferico"

    def __str__(self):
        return self.tipo
    