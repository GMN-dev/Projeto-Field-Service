# Generated by Django 4.0.6 on 2022-11-07 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastroEquipamento', '0007_tblsolicitacao_pas_alter_tblsolicitacao_observacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblsolicitacao',
            name='data_incidentes',
            field=models.DateField(auto_now_add=True),
        ),
    ]