# Generated by Django 2.0.7 on 2018-08-23 17:37

from django.db import migrations


def criar_parametro_inicial(apps, schema_editor):
    ParameterForBase = apps.get_model('core', 'ParameterForBase')
    parametro = ParameterForBase.objects.first()

    if not parametro:
        parametro = ParameterForBase()
        parametro.nomeProjeto = "Core"
        parametro.tituloProjeto = "Prefeitura de Palmas"
        parametro.descricaoProjeto = "Aqui faz uma descrição do sistema."
    parametro.iconeProjeto = '<img src="/static/img/icons/Mais.svg" width="50px"/>'
    parametro.save()



class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180823_1434'),
    ]

    operations = [
        migrations.RunPython(criar_parametro_inicial)
    ]