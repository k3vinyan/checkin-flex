# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-07 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0003_auto_20180307_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='date',
            field=models.DateTimeField(blank=True, max_length=20, null=True),
        ),
    ]
