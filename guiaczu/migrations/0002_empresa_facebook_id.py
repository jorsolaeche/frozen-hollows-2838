# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guiaczu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='facebook_id',
            field=models.CharField(null=True, blank=True, help_text='id de pagina de facebook', max_length=30),
        ),
    ]
