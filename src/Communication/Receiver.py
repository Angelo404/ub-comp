from urllib2 import Request,urlopen
from pi_switch import RCSwitchReceiver
import logging

def opened_door():
    logging.info("Door opened!")
    sendStateChange("Sensors:Door:Bedroom", "open")

def sendStateChange(key, value):
    request = Request("http://localhost:5000/API/update/{}/{}".format(key, value))
    response = urlopen(request)
    responseText = response.read()
    logging.debug(responseText)


receiver = RCSwitchReceiver()
receiver.enableReceive(2)
logging.basicConfig(filename="/home/pi/receiver_log.log", level=logging.DEBUG, format="%(asctime)s %(message)s")

while True:
    if receiver.available():
        received_value = receiver.getReceivedValue()
        logging.debug("Received value: {}".format(received_value))
        if received_value:
            if received_value == 2876233:
                opened_door()

            receiver.resetAvailable()


