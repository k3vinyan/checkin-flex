# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests
from flex import sessionHelper

# Create your views here.
def index(request):

    # if request.method == 'GET':
    #     if sessionHelper.isAuthSession():
    #         return render(request, 'drivers/index.html')
    #     else:
    #         return redirect('../')

    session = requests.Session()
    s = session.get("http://localhost:8000/drivers/roster", headers=sessionHelper.headers)
    BSObj = BeautifulSoup(s.text, 'lxml')
    print BSObj
    daIDs   = BSObj.find(id="cspDATable").find_all(attrs={'data-bind': 'text: transporterId'})
    daNames = BSObj.find(id="cspDATable").find_all(attrs={'data-bind': 'text: DAName'})
    shiftLengths = BSObj.find(id="cspDATable").find_all(attrs={'data-bind': 'text: duration'})
    startTimes = BSObj.find(id="cspDATable").find_all(attrs={'data-bind': 'text: startTime'})
    endTimes = BSObj.find(id="cspDATable").find_all(attrs={'data-bind': 'text: endTime'})


    for iD, name, sl, st, et  in zip(daIDs, daNames, shiftLengths, startTimes, endTimes):
        name = name.text.split(" ")
        firstName = name[0]
        lastName = name[1]
        try:
            Block.objects.get(startTime=st.text)
        except:
            block = Block(startTime=st.text, endTime=et.text, shiftLength=sl.text)
            block.save()
        try:
            Driver.objects.get(DPID=iD.text)
        except ObjectDoesNotExist:
            block = Block.objects.get(startTime=st.text)
            driver = Driver(DPID=iD.text,
                            first_name = firstName,
                            last_name = lastName,
                            shiftLength = sl.text,
                            startTime = st.text,
                            endTime = et.text,
                            block = block
                            )
            driver.save()


    if request.method == 'GET':
        blocks = Block.objects.order_by('startTime').all()
        drivers = Driver.objects.order_by('startTime', 'first_name').all()

        total = {}

        for driver in drivers:
            for block in blocks:
                if block.startTime == driver.startTime:
                        try:
                            total[block.startTime]
                        except KeyError:
                            total[block.startTime] = 0
                        total[block.startTime] += 1


        return render(request, 'operations/add_drivers.html', {'drivers':drivers, 'blocks':blocks, 'total':total})

    if request.method == 'POST':
        drivers = request.POST.get('drivers')
        drivers = drivers.split('\n')

        for driver in drivers:
            d = driver.strip()
            fullname = d.split(' ')
            try:
                firstName = fullname[0]
                lastName = fullname[1]
            except IndexError:
                print("Index out of range")
                break

            d = Driver(first_name=firstName, last_name=lastName)
            d.save()

def addDrivers(request):





        return redirect("/drivers/add_drivers")

def roster(request):
    return render(request, 'drivers/roster.html')
