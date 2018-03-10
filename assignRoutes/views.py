# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from flex import sessionHelper
from drivers.models import Driver
from routes.models import Route, Tba
# Create your views here.
def index(request):
    drivers = Driver.objects.filter(checkin=True, checkout=False)
    routes = Route.objects.filter(isAssigned=False)
    DP = {'drivers': drivers, 'routes': routes }
    if request.method == "GET":
        if sessionHelper.isAuthSession():
            drivers = Driver.objects.filter(checkin=True, checkout=False)
            routes = Route.objects.filter(isAssigned=False)
            DP = {'drivers': drivers, 'routes': routes }
            return render(request, 'assignRoutes/index.html', {'DP': DP})
        else:
            return redirect('../')
    if request.method == "POST":

        route = request.POST.get('route')
        driverId = request.POST.get('driverId')

        driver = Driver.objects.get(id=driverId)
        if route == "None":
            print "route is none"
        else:
            route = Route.objects.get(id=route)

        #remove Driver from Route Model
        if driver.route != None:
            try:
                oldRoute = driver.route
                newRoute = Route.objects.get(id=oldRoute.id)
                newRoute.isAssigned = False
                newRoute.driver = None
                newRoute.save(update_fields=['isAssigned'])
                newRoute.save(update_fields=['DP'])
            except ObjectDoesNotExist:
                print "does not exist"

        #if route is None sit driver route to None
        if route == "None":
            driver.route = None
            driver.isAssigned = False
            driver.save(update_fields=['route'])
            driver.save(update_fields=['isAssigned'])
        else:
            driver.route = route
            r = Route.objects.get(id=route.id)
            first = driver.first_name
            second = driver.last_name
            r.DP = first + " " + second
            r.isAssigned = True
            r.save(update_fields=['isAssigned'])
            r.save(update_fields=['DP'])
            tbas = Tba.objects.filter(route=r)
            for tba in tbas:
                tba.driver = driver
                tba.save(update_fields=['driver'])
            driver.isAssigned = True
            driver.save(update_fields=['route'])
            driver.save(update_fields=['isAssigned'])



        drivers = Driver.objects.filter(checkin=True, checkout=False)

        routes = Route.objects.filter(isAssigned=False)

        return render(request, 'assignRoutes/index.html', {'DP': DP})
