# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 23:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('sockets', '0004_auto_20170630_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='socket',
            name='session',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='sessions.Session'),
            preserve_default=False,
        ),
    ]
