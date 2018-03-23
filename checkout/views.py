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
    session = requests.Session()
    s = session.get("http://localhost:8000/checkout/routingTools", headers=sessionHelper.headers)
    BSObj = BeautifulSoup(s.text, 'lxml')

    mainTable = BSObj.select("#mainTable")
    tr = mainTable[0].find_all("tr")

    count = 0
    driverData = {
        'company': "",
        'route': "",
        'driver': "",
        'serviceType': "",
        'cubicSize': "",
        'departureTime': "",
        'returnTime': "",
        'vehicleStop': "",
        'packagePerStop': "",
        'totalPackage': "",
        'actualPackage': "",
        'expectedPackage': ""
    }
    drivers = []

    count = 0;
    for t in tr:
        test = t.select("td")
        print "----------------------------"
        print count
        for item in test:
            if count == 0:
                driverData['company'] = item.text
                count += 1
            if count == 1:
                driverData['route'] = item.text
                count += 1
            if count == 2:
                driverData['driver'] = item.text
                count += 1
            if count == 3:
                driverData['serviceType'] = item.text
                count += 1
            if count == 4:
                driverData['cubicSize'] = item.text
                count += 1
            if count == 5:
                driverData['departureTime'] = item.text
                count += 1
            if count == 6:
                driverData['returnTime'] = item.text
                count += 1
            if count == 7:
                driverData['vehicleStop'] = item.text
                count += 1
            if count == 8:
                driverData['packagePerStop'] = item.text
                count += 1
            if count == 9:
                driverData['totalPackage'] = item.text
                count += 1
            if count == 10:
                driverData['actualPackage'] = item.text
                count += 1
            if count > 10 and count < 16:
                count += 1
            if count == 16:
                drivers.append(driverData)
                count = 0
            print driverData
        print "----------------------------"

    print drivers
    #get all routes for cluster and return dictionary of routes
    def getRoutes(cluster):
        #routes = BSObj.select(cluster)[0].find_all("text", attrs={"style":"text-anchor: end;", "x":"-9", "y":"0"})
        routes = BSObj.select(cluster)[0].find_all("text", attrs={"dy":".32em", "style":"text-anchor: end;"})
        routesDict = OrderedDict()
        for route in routes:
            routesDict[route.text] = {}
        return routesDict

    #get the values from the status of each route; return array of tuples
    # def getValueOfStatus(cluster):
    #     data = []
    #     sort = []
    #
    #     values = BSObj.select(cluster)[0].find_all("text", attrs={"dy":".40em", "text-anchor":"middle", "font-size":"12px"})
    #     count = 0
    #     for value in values:
    #         count += 1
    #         sort.append(value.text)
    #         if count == 8:
    #             count = 0
    #             data.append(tuple(sort))
    #             sort = []
    #     return data
    #
    # def createClusterData(getValueOfStatus, getRoutes, packageStatus):
    #     newObject = {}
    #     for data, route in zip(getValueOfStatus, getRoutes):
    #         newObject[route] ={}
    #         for value, status in zip(data, packageStatus):
    #             newObject[route][status] = value
    #     return newObject
    #
    # #use multiple methods to create object of allroutes data from routingTools
    # def getRouteToolsData(cluster):
    #     valueOfStatus = getValueOfStatus(cluster)
    #     routes = getRoutes(cluster)
    #
    #     clusterData = createClusterData(valueOfStatus, routes, packageStatus)
    #     return clusterData

    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)

    if request.method =='GET':

        # samedayData        = getRouteToolsData(SAME_EVEN)
        # emergencyData      = getRouteToolsData(DSF3_EMERGENCY)
        #
        # drivers = Driver.objects.filter(checkin=True, isAssigned=True, checkout=False)
        # return render(request, 'checkout/index.html', {'drivers':drivers, 'samedayData':samedayData, 'emergencyData':emergencyData})
        return render(request, 'checkout/index.html')

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
