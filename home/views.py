# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from bs4 import BeautifulSoup
from flex import sessionHelper

# Create your views here.
def index(request):

    #need session prior to homepage
    if request.method == 'GET':
        if sessionHelper.isAuthSession():
            return render(request, 'home/index.html')
        else:
            return render(request, 'home/login.html')

    #create session and redirect to homepage
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        s = sessionHelper.getAmazonSession(email, password)
        response = render(request, 'home/index.html')

        for cookie in s.cookies:
            print cookie
            response.set_cookie(cookie.name, cookie.value)

        if sessionHelper.isAuthSession():
            return response
        else:
            return render(request, 'home/login.html', {'error': 'email or password is incorrect'})
