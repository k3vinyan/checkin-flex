# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from routes.models import Route, Block
# Create your models here.
class Driver(models.Model):
    DPID        = models.CharField(max_length=20, default=False)
    first_name  = models.CharField(max_length=20)
    last_name   = models.CharField(max_length=30)
    checkin     = models.BooleanField(default=False)
    isAssigned  = models.BooleanField(default=False)
    shiftLength = models.CharField(max_length=20, blank=True)
    startTime   = models.CharField(max_length=10, blank=True)
    endTime     = models.CharField(max_length=10, blank=True)
    isNoShow    = models.BooleanField(default=True)
    checkout    = models.BooleanField(default=False)
    packageScan = models.CharField(max_length=3, blank=True)
    routingTool = models.CharField(max_length=3, blank=True)
    route       = models.ForeignKey(Route, on_delete=models.CASCADE, null=True)
    block       = models.ForeignKey(Block, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
