# Generated by Django 4.0.6 on 2022-11-08 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastroEquipamento', '0009_alter_tblsolicitacao_operacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblsolicitacao',
            name='motivo',
            field=models.CharField(choices=[('extravio', 'Extravio - Retirada indevida'), ('adicao', 'Adição Novo'), ('quebra', 'Quebra - Por Desgaste'), ('quebra_mal_uso', 'Quebra - Mal Uso'), ('troca', 'Troca')], max_length=15),
        ),
    ]
