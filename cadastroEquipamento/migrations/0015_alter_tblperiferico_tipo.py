# Generated by Django 4.0.6 on 2022-12-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastroEquipamento', '0014_alter_tblperiferico_observacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblperiferico',
            name='tipo',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]