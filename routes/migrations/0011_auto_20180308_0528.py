# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-08 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0010_auto_20180308_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tba',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]
