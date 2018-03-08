# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Route(models.Model):
     route       = models.CharField(max_length=15)
     cluster     = models.CharField(max_length=15)
     isAssigned  = models.BooleanField(default=False)
     tbaCount    = models.CharField(max_length=15, blank=True)
     DP          = models.CharField(max_length=15, blank=True, null=True)

     class Meta:
         ordering = ('cluster', 'route',)

class Block(models.Model):
    date        = models.DateTimeField(max_length=20, blank=True, null=True)
    startTime   = models.CharField(max_length=10)
    endTime     = models.CharField(max_length=10)
    shiftLength = models.CharField(max_length=20)
    create_at   = models.DateTimeField(auto_now_add=True)


class Tba(models.Model):
    driver      = models.CharField(max_length=15, blank=True)
    route       = models.ForeignKey(Route, on_delete=models.CASCADE, null=True)
    tba         = models.CharField(max_length=15)
    status      = models.CharField(max_length=15)
    link        = models.CharField(max_length=60)
    address     = models.CharField(max_length=30)
