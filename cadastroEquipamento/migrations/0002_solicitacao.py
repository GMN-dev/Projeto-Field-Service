# Generated by Django 4.0.6 on 2022-08-23 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastroEquipamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id_incidentes', models.AutoField(primary_key=True, serialize=False)),
                ('chamado', models.IntegerField(blank=True, null=True)),
                ('data_incidente', models.DateField(blank=True, null=True)),
                ('informante', models.CharField(blank=True, max_length=255, null=True)),
                ('operacao', models.CharField(blank=True, max_length=255, null=True)),
                ('andar', models.IntegerField(blank=True, null=True)),
                ('periferico', models.CharField(blank=True, max_length=255, null=True)),
                ('motivo_solicitacao', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'solicitacao',
            },
        ),
    ]