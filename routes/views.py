# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from flex import sessionHelper
from routes.models import Tba, Route
from flex import sessionHelper
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
# def index(request):
#
#     if request.method == 'GET':
#         if sessionHelper.isAuthSession():
#             return render(request, 'routes/index.html')
#         else:
#             return redirect('../')

def index(request):
    #get request
    routeDict = {}
    if request.method == 'GET':
        if sessionHelper.isAuthSession():
            allTbas = Tba.objects.all()
            allRoutes = Route.objects.all()

            for tba in allTbas:
                cluster = tba.route.cluster
                route = tba.route.route
                if routeDict.get(cluster) == None:
                    routeDict[cluster] = {'count': 0, 'routes': {} }
                if routeDict[cluster]['routes'].get(route) == None:
                    routeDict[cluster]['routes'][route] = {'count': 0, 'tbas': []}
                    routeDict[cluster]['count'] += 1
                routeDict[cluster]['routes'][route]['tbas'].append(tba)
                routeDict[cluster]['routes'][route]['count'] += 1



            for cluster in routeDict:
                routes = routeDict[cluster]['routes']
                for route in routes:
                    count = routes[route]['count']
                    r = Route.objects.get(route=route)
                    r.tbaCount = count
                    r.save(update_fields=['tbaCount'])
            return render(request, 'routes/index.html', {'routeDict': routeDict })
        else:
            return redirect('../')
    #post requeest
    if request.method == 'POST':
        cj = request.COOKIES
        tbas =  request.POST.get('tbas')

        searchForm = sessionHelper.searchForm
        searchForm['shipmentSearchIds'] = tbas
        data = sessionHelper.getTbasFromComp(cj, searchForm)

        tbaCount = 0
        routeCount = 0
        tbaTotal = 0

        existArray = []
        noRouteArray = []
        for item in data:
            tba = item['tba']
            route = item['route']
            try:
                r = Route.objects.get(route=route)
            except ObjectDoesNotExist:
                if route != "":
                    cluster = filter(lambda x: x.isalpha(), route)
                    routeCount += 1
                    r = Route(route=route, cluster=cluster)
                    r.save()
            try:
                tba = Tba.objects.get(tba=tba)
            except ObjectDoesNotExist:
                tbaCount += 1
                tbaTotal += 1

                route = item['route']
                r = Route.objects.get(route=route)
                status = item['status']
                link = item['link']
                address = item['address']
                tba = Tba(route=r, tba=tba, status=status, link=link, address=address)
                tba.save()


            else:
                tbaTotal += 1
                existArray.append(tba.tba)
        existArrayLength = len(existArray)
        allRoutes = Route.objects.all()

        message = {'tbaCount': tbaCount, 'tbaTotal': tbaTotal, 'existArray': existArray, 'existArrayLength': existArrayLength, 'routeCount': routeCount}
        return render(request, 'routes/index.html', {'message': message, 'allRoutes': allRoutes})

def deleteRoute(request):

    if request.method == "POST":
        route = request.POST.get('route')
        Route.objects.filter(route=route).delete()
        return redirect('/routes')
