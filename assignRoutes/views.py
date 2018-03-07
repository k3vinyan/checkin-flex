# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from flex import sessionHelper
# Create your views here.
def index(request):
    if request.method == 'GET':
        if sessionHelper.isAuthSession():
            return render(request, 'assignRoutes/index.html')
        else:
            return redirect('../')
