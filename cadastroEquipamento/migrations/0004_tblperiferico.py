# Generated by Django 4.0.6 on 2022-10-19 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastroEquipamento', '0003_tblsolicitacao_site_tblsolicitacao_sla'),
    ]

    operations = [
        migrations.CreateModel(
            name='TblPeriferico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tbl_periferico',
                'managed': True,
            },
        ),
    ]
