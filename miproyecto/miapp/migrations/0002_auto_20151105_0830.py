# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('apellidos', models.TextField()),
                ('seccion', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='videojuego',
            old_name='psinopsis',
            new_name='sinopsis',
        ),
        migrations.AddField(
            model_name='videojuego',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
        ),
        migrations.AddField(
            model_name='videojuego',
            name='proveedor',
            field=models.ManyToManyField(to='miapp.Proveedor'),
        ),
    ]
