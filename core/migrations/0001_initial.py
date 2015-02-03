# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'Nome da Categoria')),
                ('ranking', models.IntegerField(verbose_name=b'Ordena\xc3\xa7\xc3\xa3o da exibi\xc3\xa7\xc3\xa3o')),
                ('active', models.BooleanField(default=True, verbose_name=b'Categoria ativa/inativa')),
            ],
            options={
                'ordering': ['ranking', 'name'],
            },
            bases=(models.Model,),
        ),
    ]
