# Generated by Django 4.0.6 on 2022-08-30 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastroEquipamento', '0002_solicitacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacao',
            name='observacao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
