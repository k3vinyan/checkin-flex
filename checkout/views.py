# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'GET':
        if sessionHelper.isAuthSession():
            return render(request, 'checkout/index.html')
        else:
            return render(request, 'home/login.html')
