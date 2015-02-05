# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150202_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500, verbose_name=b'Nome do produto')),
                ('description', models.TextField(null=True, verbose_name=b'Descri\xc3\xa7\xc3\xa3o do produto', blank=True)),
                ('size', models.CharField(max_length=200, verbose_name=b'Tamanhos do produto')),
                ('price', models.CharField(max_length=200, verbose_name=b'Pre\xc3\xa7o do produto')),
                ('active', models.BooleanField(default=True, verbose_name=b'Produto ativo/inativo')),
                ('ranking', models.IntegerField(default=0, verbose_name=b'Ordena\xc3\xa7\xc3\xa3o da exibi\xc3\xa7\xc3\xa3o')),
                ('categories', models.ManyToManyField(to='core.Category', verbose_name=b'Categorias que o produto faz parte')),
            ],
            options={
                'ordering': ['ranking', 'name'],
                'verbose_name_plural': 'Produtos',
            },
            bases=(models.Model,),
        ),
    ]
