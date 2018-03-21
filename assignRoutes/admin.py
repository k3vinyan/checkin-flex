# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from drivers.models import Driver
from routes.models import Route, Block, Tba

# Register your models here.
admin.site.register(Driver)
admin.site.register(Route)
admin.site.register(Block)
admin.site.register(Tba)
