from bs4 import BeautifulSoup
from django.http import HttpResponse
from urllib2 import urlopen, HTTPError, URLError, HTTPRedirectHandler
import requests, re

URLS = {
    "SEARCH": 'https://www.amazonlogistics.com/comp/packageSearch',
    "SIGNIN": "https://www.amazonlogistics.com/ap/signin",
    "BASE": "https://www.amazonlogistics.com/"
}

userSession = {
    "session": None
}

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US, en;q=0.9",
    "Content-Type":"application/x-www-form-urlencoded",
    "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"
}

searchForm = {
    'dateType':"shipDate",
    'shipStartDate':"02/07/2018",
    'shipStartTime':"00:00",
    'shipEndDate':"02/10/2018",
    'shipEndTime':"00:00",
    'deliveryStartDate':"02/09/2018",
    'deliveryStartTime':"00:00",
    'deliveryEndDate':"02/10/2018",
    'deliveryEndTime':"00:00",
    'scheduledStartDateBegin':"02/09/2018",
    'scheduledStartTimeBegin':"00:00",
    'scheduledStartDateEnd':"02/10/2018",
    'scheduledStartTimeEnd':"00:00",
    'shipStatusIdList':"AT_STATION",
    'shipmentStationHolder':"1002821",
    'shipmentAssociateHolder':"ALL",
    'shipType':"ALL",
    'shipOption':"ALL",
    'shipmentSearchId':"",
    'shipmentSearchIds':"",
    'shipmentSearchPhone':"",
    'downloadToken': "",
    'downloadToken': "",
    'ec_i':"ShipmentListTable",
    'ShipmentListTable_crd':"5000",
    'ShipmentListTable_p':"1",
    'ShipmentListTable_s_merchantId':"",
    'ShipmentListTable_a_manifestTrackingId':"shipmentTrackingId",
    'ShipmentListTable_a_shipOption':"shipOptionName",
    'ShipmentListTable_a_shipType':"shipmentTitle",
    'ShipmentListTable_a_stationName':"holderStationName",
    'ShipmentListTable_a_associateHolder':"holderEmployeeName",
    'ShipmentListTable_rd':"50",
    'action':"ajaxSearch"
}

#get session from comp
def getAmazonSession(username, password):
    session = requests.Session()
    s = session.get(URLS['SEARCH'], headers=headers)

    BSObj = BeautifulSoup(s.text, 'lxml')
    hiddenInput = BSObj.select('input[type="hidden"]')
    params = {}
    for item in hiddenInput:
        try:
            params[item['name']] = item['value']
        except KeyError:
            params[item['name']] = ""

    params['email'] = username
    params['password'] = password

    s = session.post(URLS['SIGNIN'], data=params, headers=headers)
    userSession['session'] = s

    return s

#check if response return correct page since 200 status code still returnn
#for correct and incorrect email/password
def isAuthSession():
    try:
        session = userSession['session']
        if session == None:
            return False
    except:
        return False

    BSObj = BeautifulSoup(session.text, 'lxml')
    createAccountSubmitId = BSObj.find(id="createAccountSubmit")

    #return false if incorrect html response
    if createAccountSubmitId:
        return False
    else:
        return True
