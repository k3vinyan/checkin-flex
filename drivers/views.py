# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from http.django import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render('drivers/index.html')
