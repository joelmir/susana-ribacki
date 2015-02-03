# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=b'products/images/default.png', upload_to=b'products/images/'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='tumb',
            field=models.ImageField(default=b'products/tumb/default.png', upload_to=b'products/tumb/'),
            preserve_default=True,
        ),
    ]
