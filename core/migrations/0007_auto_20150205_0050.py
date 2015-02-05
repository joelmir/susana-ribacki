# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150204_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(default=b'banner/default.png', upload_to=b'banner/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=b'products/images/default.png', upload_to=b'products/images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tumb',
            field=models.ImageField(default=b'products/tumb/default.png', upload_to=b'products/tumb/'),
        ),
    ]
