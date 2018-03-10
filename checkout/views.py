# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
from flex import sessionHelper
from bs4 import BeautifulSoup
from django.template.defaulttags import register
from flex import sessionHelper
from collections import OrderedDict
from drivers.models import Driver
# Create your views here.
def index(request):
    # if request.method == 'GET':
    #     if sessionHelper.isAuthSession():
    #         return render(request, 'checkout/index.html')
    #     else:
    #         return redirect('/')

    #Cluster
    DSF3_EMERGENCY  = "#graph-DSF3_EMERGENCY"
    RTS_DSF3_LATE   = "#graph-RTS-DSF3-LATE"
    SAME_EVEN       = "#graph-DSF3-SAME-EVEN"

    #tuple of package status
    packageStatus = ('betweenFCandStation', 'atStation', 'readyForDeparture', 'onRoadWithDA', 'delivered', 'attempted', 'undelivered', 'others')

    #create session and create soup object
    session = requests.Session()
    s = session.get("http://localhost:8000/checkout/routingTools", headers=sessionHelper.headers)
    BSObj = BeautifulSoup(s.text, 'lxml')

    #get all routes for cluster and return dictionary of routes
    def getRoutes(cluster):
        #routes = BSObj.select(cluster)[0].find_all("text", attrs={"style":"text-anchor: end;", "x":"-9", "y":"0"})
        routes = BSObj.select(cluster)[0].find_all("text", attrs={"dy":".32em", "style":"text-anchor: end;"})
        routesDict = OrderedDict()
        for route in routes:
            routesDict[route.text] = {}
        return routesDict

    #get the values from the status of each route; return array of tuples
    def getValueOfStatus(cluster):
        data = []
        sort = []

        values = BSObj.select(cluster)[0].find_all("text", attrs={"dy":".40em", "text-anchor":"middle", "font-size":"12px"})
        count = 0
        for value in values:
            count += 1
            sort.append(value.text)
            if count == 8:
                count = 0
                data.append(tuple(sort))
                sort = []
        return data

    def createClusterData(getValueOfStatus, getRoutes, packageStatus):
        newObject = {}
        for data, route in zip(getValueOfStatus, getRoutes):
            newObject[route] ={}
            for value, status in zip(data, packageStatus):
                newObject[route][status] = value
        return newObject

    #use multiple methods to create object of allroutes data from routingTools
    def getRouteToolsData(cluster):
        valueOfStatus = getValueOfStatus(cluster)
        routes = getRoutes(cluster)

        clusterData = createClusterData(valueOfStatus, routes, packageStatus)
        return clusterData

    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)

    if request.method =='GET':

        samedayData        = getRouteToolsData(SAME_EVEN)
        emergencyData      = getRouteToolsData(DSF3_EMERGENCY)

        drivers = Driver.objects.filter(checkin=True, isAssigned=True, checkout=False)
        return render(request, 'checkout/index.html', {'drivers':drivers, 'samedayData':samedayData, 'emergencyData':emergencyData})

    #POST request
    if request.method == 'POST':
        driver_id = request.POST.get('driver_id')
        driver = Driver.objects.get(id=driver_id)
        if driver.checkout == False:
            driver.checkout = True
            driver.save(update_fields=['checkout'])
        else:
            driver.checkout = False
            driver.save(update_fields=['checkout'])

    return HttpResponse(request)

#checkout
def getDPScan(request):
    session = stations.getAmazonSession()
    driverId = request.GET.get('driverId')
    driver = Driver.objects.get(id=driverId)
    tbas = Tba.objects.filter(driver=driver)

    print session
    tbaList = []
    error = []
    count = 0
    for tba in tbas:
        s = session.get(tba.link, headers=stations.headers)
        BSObj = BeautifulSoup(s.text, 'lxml')
        driverName = BSObj.find(string=re.compile("DA Name:"))
        if driverName != None:
            driverList = driverName.split(" ")
            if driverList[2] == driver.first_name and driverList[3] == driver.last_name:
                count += 1
            else:
                error.append(tba)

        driver.packageScan = count
        driver.save(update_fields=['packageScan'])

    return redirect('checkout')

def routingTools(request):
    return render(request, 'checkout/routingtool.html')
