# Generated by Django 3.2.7 on 2021-09-10 21:32

from django.db import migrations
import localflavor.br.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='postal_code',
            field=localflavor.br.models.BRPostalCodeField(default='', max_length=9, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='user',
            name='cnpj',
            field=localflavor.br.models.BRCNPJField(blank=True, default='', max_length=18, null=True, verbose_name='CNPJ'),
        ),
    ]