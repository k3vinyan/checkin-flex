# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from flex import sessionHelper
from datetime import datetime
from pytz import timezone
import pytz
from drivers.models import Driver
# Create your views here.
def index(request):
    if request.method == 'GET':

        date = datetime.now(tz=pytz.utc)
        date = date.astimezone(timezone('US/Pacific'))
        todayHour = date.strftime('%H')
        timePicker = None

        if request.GET.get('time'):
            timePicker = request.GET.get('time').split(":")
            timePickerHour = int(timePicker[0])
            timePickerMin = timePicker[1][0] + timePicker[1][1]
            timePickerPeriod = timePicker[1][2] + timePicker[1][3]
            if timePickerPeriod == "PM" and timePickerHour != 12:
                timePickerHour += 12
        drivers = Driver.objects.all()
        checkinDrivers = []
        for driver in drivers:
            driverTime = driver.startTime.split(":")
            driverHour = int(driverTime[0])
            driverMin = int(driverTime[1].split(" ")[0])
            driverPeriod = driverTime[1].split(" ")[1]


            if driverPeriod == "pm" and driverHour != 12:
                driverHour += 12
            if timePicker != None:
                if driverHour >= timePickerHour and driver.checkin == False:
                    checkinDrivers.append(driver)
            else:
                if driverHour >= todayHour and driver.checkin == False:
                    checkinDrivers.append(driver)
        return render(request, 'checkin/index.html', {'drivers':checkinDrivers})
    else:
        return redirect('../')


def isCheckin(request):
    #POST request
    if request.method == 'POST':
        driver_id = request.POST.get('driver-id')
        driver = Driver.objects.get(id=driver_id)
        if driver.checkin == False:
            driver.checkin = True
            driver.isNoShow = False
            driver.save(update_fields=['isNoShow'])
            driver.save(update_fields=['checkin'])
        else:
            driver.checkin = False
            driver.save(update_fields=['checkin'])
        return HttpResponse(request)



def noShow(request):
    if request.method == "POST":
        driver_id = request.POST.get('driver-id');
        driver = Driver.objects.get(id=driver_id)
        if driver.isNoShow == False:
            driver.isNoShow = True;
            driver.checkin = False
            driver.save(update_fields=['isNoShow'])
            driver.save(update_fields=['checkin'])
        else:
            driver.isNoShow = False
            driver.save(update_fields=['isNoShow'])

    return HttpResponse(request)
