# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videojuego',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('psinopsis', models.TextField()),
                ('fecha_distribucion', models.DateTimeField()),
                ('precio', models.TextField()),
            ],
        ),
    ]
