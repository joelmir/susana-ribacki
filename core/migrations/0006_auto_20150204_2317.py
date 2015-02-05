# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150202_2351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(null=True, verbose_name=b'Descri\xc3\xa7\xc3\xa3o do banner', blank=True)),
                ('ranking', models.IntegerField(default=0, verbose_name=b'Ordena\xc3\xa7\xc3\xa3o do banenr')),
                ('image', models.ImageField(default=b'media/banner/default.png', upload_to=b'media/banner/')),
                ('active', models.BooleanField(default=True, verbose_name=b'Banner ativo/inativo')),
            ],
            options={
                'ordering': ['ranking', 'description'],
                'verbose_name_plural': 'Banners',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=b'media/products/images/default.png', upload_to=b'media/products/images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tumb',
            field=models.ImageField(default=b'media/products/tumb/default.png', upload_to=b'media/products/tumb/'),
        ),
    ]
