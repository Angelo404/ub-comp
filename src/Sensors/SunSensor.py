from urllib2 import Request,urlopen
import logging
import json
import time
import urllib
from datetime import datetime

def sendStateChange(key, value):
    value = str(value)
    value = str.replace(value, " ", "+")
    print "Updating {}/{}".format(key,value)
    callUrl = "http://localhost:5000/API/update/{}/{}".format(key, value)
    request = Request(callUrl)
    response = urlopen(request)
    responseText = response.read()
    logging.debug(responseText)

def datetime_from_utc_to_local(utc_datetime_string):
    utc_datetime_string = utc_datetime_string[:-6]
    utc_datetime = datetime.strptime(utc_datetime_string, "%Y-%m-%dT%H:%M:%S")
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset

request = Request('http://api.sunrise-sunset.org/json?lat=53.219156&lng=6.562857&formatted=0')
response = urlopen(request)
responseText = response.read()

jsonObject = json.loads(responseText)
print responseText
if (jsonObject["status"] == "OK"):

    sunRise = datetime_from_utc_to_local(str( jsonObject["results"]["sunrise"]))
    sunSet = datetime_from_utc_to_local(str(jsonObject["results"]["sunset"]))
    sendStateChange("Sensors:Sun:Rise", sunRise)
    sendStateChange("Sensors:Sun:Set", sunSet)