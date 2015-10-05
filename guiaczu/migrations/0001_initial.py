# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id_empresa', models.AutoField(primary_key=True, serialize=False)),
                ('logo', models.ImageField(blank=True, help_text='Imagen o Logo de la empresa', null=True, upload_to='documents/%Y/%m/%d')),
                ('razonsocial', models.CharField(max_length=140, help_text='Razon social de la empresa')),
                ('slug', models.SlugField(editable=False)),
                ('telefono', models.CharField(max_length=50, help_text='Numero de telefono de la empresa')),
                ('direccion', models.CharField(max_length=140, help_text='Direccion de la empresa')),
                ('latitud', models.CharField(max_length=50, blank=True, help_text='Latitud para la direccion en google maps', null=True)),
                ('longitud', models.CharField(max_length=50, blank=True, help_text='Longitud para la direccion en google maps', null=True)),
            ],
            options={
                'verbose_name': 'Empresa',
            },
        ),
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id_rubro', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, help_text='Nombre del rubro de la empresa')),
                ('slug', models.SlugField(editable=False)),
            ],
            options={
                'verbose_name': 'Categoria / Rubro',
            },
        ),
        migrations.AddField(
            model_name='empresa',
            name='rubro',
            field=models.ForeignKey(to='guiaczu.Rubro', db_column='id_rubro'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
