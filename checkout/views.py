# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)
    return render(request, 'checkout/index.html')
