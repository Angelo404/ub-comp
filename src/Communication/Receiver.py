from urllib2 import Request,urlopen
from pi_switch import RCSwitchReceiver

def opened_door():
    print "Door opened!"
    sendStateChange("Sensors:Door:Bedroom", "open")

def sendStateChange(key, value):
    request = Request("http://localhost:5000/API/update/{}/{}".format(key, value))
    response = urlopen(request)
    responseText = response.read()
    print responseText


receiver = RCSwitchReceiver()
receiver.enableReceive(2)

while True:
    if receiver.available():
        received_value = receiver.getReceivedValue()
        if received_value:
            if received_value == 2876233:
                opened_door()

            receiver.resetAvailable()


