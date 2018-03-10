# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from bs4 import BeautifulSoup
from flex import sessionHelper
from drivers.models import Driver
from routes.models import Route
from django.template.loader import render_to_string
from datetime import datetime
import pytz
from pytz import timezone

# Create your views here.
def index(request):

    #need session prior to homepage
    if request.method == 'GET':
        if sessionHelper.isAuthSession():
            drivers = Driver.objects.all()
            routes = Route.objects.values()

            unassignRoutes = []
            assignRoutes = []
            notArrivedDrivers = []
            arrivedDrivers = []
            assignDrivers = []
            unassignClusters = {}

            date = datetime.now(tz=pytz.utc)
            date = date.astimezone(timezone('US/Pacific'))
            todayHour = date.strftime('%H')

            for route in routes:
                if route['isAssigned'] == False:
                    unassignRoutes.append(route)
                    cluster = route['cluster']
                    if cluster not in unassignClusters:
                        unassignClusters[cluster] = {'count': 1}
                    else:
                        unassignClusters[cluster]['count'] += 1

            for driver in drivers:
                driverTime = driver.startTime.split(":")
                driverHour = int(driverTime[0])
                driverMin = int(driverTime[1].split(" ")[0])
                driverPeriod = driverTime[1].split(" ")[1]

                if driver.checkin == False and driver.isNoShow == True and driverHour >= todayHour:
                    notArrivedDrivers.append(driver)
                elif driver.checkin == True and driver.isAssigned == False and driver.isNoShow == False:
                    arrivedDrivers.append(driver)
                elif driver.checkin == True and driver.isAssigned == True and driver.checkout == False and driver.isNoShow == False:
                    assignDrivers.append(driver)


            totalUnassignRoutes =  len(unassignRoutes)
            totalAssignRoutes = len(assignRoutes)
            totalNotArrivedDrivers = len(notArrivedDrivers)
            totalArrivedDrivers = len(arrivedDrivers)
            totalAssignDrivers = len(assignDrivers)
            totalRoutes = len(routes)
            totalDrivers = len(drivers)
            totalUnassignDrivers = len(notArrivedDrivers) + len(arrivedDrivers)


            return render(request, 'home/index.html',
                {
                    'unassignRoutes':unassignRoutes,
                    'assignRoutes':assignRoutes,
                    'totalNotArrivedDrivers':totalNotArrivedDrivers,
                    'totalArrivedDrivers':totalArrivedDrivers,
                    'totalAssignDrivers':totalAssignDrivers,
                    'totalAssignRoutes':totalAssignRoutes,
                    'totalUnassignRoutes':totalUnassignRoutes,
                    'totalRoutes':totalRoutes,
                    'totalDrivers':totalDrivers,
                    'unassignClusters':unassignClusters,
                    'totalUnassignDrivers':totalUnassignDrivers,
                    'totalAssignDrivers':totalAssignDrivers
                })
        else:
            return render(request, 'home/login.html')

    #create session and redirect to homepage
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        s = sessionHelper.getAmazonSession(email, password)
        response = redirect('/')

        for cookie in s.cookies:
            response.set_cookie(cookie.name, cookie.value, domain='dsf3-flex.herokuapp.com')


        return response
    else:
        return render(request, 'home/login.html', {'error': 'email or password is incorrect'})
