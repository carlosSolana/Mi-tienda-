# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_auto_20151105_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='videojuego',
            name='foto',
            field=models.ImageField(upload_to='miapp/static/media', default=1),
        ),
    ]
