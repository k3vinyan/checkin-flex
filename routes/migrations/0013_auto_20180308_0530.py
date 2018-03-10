# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-08 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0012_auto_20180308_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='date',
            field=models.DateTimeField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='endTime',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='block',
            name='shiftLength',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='block',
            name='startTime',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='route',
            name='DP',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='cluster',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='route',
            name='route',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='route',
            name='tbaCount',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='tba',
            name='driver',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='tba',
            name='status',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tba',
            name='tba',
            field=models.CharField(max_length=50),
        ),
    ]