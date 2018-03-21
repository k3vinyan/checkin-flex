# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Route(models.Model):
     route       = models.CharField(max_length=50)
     cluster     = models.CharField(max_length=50)
     isAssigned  = models.BooleanField(default=False)
     tbaCount    = models.CharField(max_length=50, blank=True)
     DP          = models.CharField(max_length=50, blank=True, null=True)

     def __str__(self):
         return self.route

     class Meta:
         ordering = ('cluster', 'route',)



class Block(models.Model):
    date        = models.DateTimeField(max_length=50, blank=True, null=True)
    startTime   = models.CharField(max_length=50)
    endTime     = models.CharField(max_length=50)
    shiftLength = models.CharField(max_length=50)
    create_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.startTime + " - " + self.endTime

class Tba(models.Model):
    driver      = models.ForeignKey('drivers.Driver', blank=True, null=True)
    route       = models.ForeignKey(Route, on_delete=models.CASCADE, null=True)
    tba         = models.CharField(max_length=50)
    status      = models.CharField(max_length=50)
    link        = models.CharField(max_length=100)
    address     = models.CharField(max_length=100)

    def __str__(self):
        return self.tba
