# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from email.policy import default
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
    
    def get_absolute_url(self):
            return reverse("operacao_details", kwargs={'operacao': self.operacao, 'pk':self.pk})

class TblSolicitacao(models.Model):
    chamado = models.CharField(max_length=7, unique=True)
    data_incidentes = models.DateField()
    solicitante = models.CharField(max_length=30)
    operacao = models.CharField(max_length=15)
    andar = models.IntegerField()
    periferico = models.CharField(max_length=10)
    motivo = models.CharField(max_length=15)
    observacao = models.TextField()

    class Meta:
        managed = True
        db_table = 'tbl_solicitacao'

    def __str__(self) :
        return self.chamado

    def get_absolute_url(self):
        return reverse("incidente_details", kwargs={'chamado': self.chamado})
    