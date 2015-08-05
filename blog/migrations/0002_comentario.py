# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
                ('entrada', models.ForeignKey(to='blog.Entrada')),
            ],
            options={
                'ordering': ['-fecha'],
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
            },
        ),
    ]
